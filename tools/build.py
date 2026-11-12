#!/usr/bin/env python3
"""Build podcast episodes from script files: Gemini TTS -> mp3 -> RSS feed.

Standard library only (plus ffmpeg/ffprobe on PATH).

Usage:
  python3 tools/build.py                 # build every `status: ready` episode not yet built
  python3 tools/build.py --force         # rebuild all ready episodes (re-synthesizes audio)
  python3 tools/build.py --dry-run       # no API calls; tones instead of speech (pipeline test)
  python3 tools/build.py --export-plain episodes/X.md   # print "Maya: ..." text for pasting into AI Studio
  python3 tools/build.py --lint          # check scripts only, no audio

Env:
  GEMINI_API_KEY   required unless --dry-run / --lint
  BASE_URL         public site root; defaults to the GitHub Pages URL derived from GITHUB_REPOSITORY
"""
import argparse
import base64
import datetime as dt
import email.utils
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API_URL = "https://generativelanguage.googleapis.com/v1beta/interactions"
TAG_RE = re.compile(r"<[a-z][a-z\- ]*>")
BACKCHANNEL_RE = re.compile(r"\|[^|]*\|")


def load_config():
    return json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(map(str, cmd))}\n{r.stderr[-2000:]}")
    return r.stdout


# ---------------------------------------------------------------- scripts

def parse_episode(path, cfg):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit(f"{path.name}: missing front matter block (--- ... ---)")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    turns = []
    for ln, line in enumerate(m.group(2).splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        mm = re.match(r"^([A-Za-z]+)\s*(?:\[([^\]]*)\])?\s*:\s*(.+)$", s)
        if not mm:
            raise SystemExit(f"{path.name}: body line {ln} is not 'SPEAKER [style]: text'")
        key = mm.group(1).upper()
        if key not in cfg["speakers"]:
            raise SystemExit(f"{path.name}: line {ln}: unknown speaker {key!r}; expected {list(cfg['speakers'])}")
        turns.append({
            "speaker": cfg["speakers"][key]["name"],
            "style": (mm.group(2) or "").strip(),
            "text": mm.group(3).strip(),
        })
    return meta, turns


def spoken_words(turns):
    n = 0
    for t in turns:
        txt = BACKCHANNEL_RE.sub(lambda m: m.group(0).strip("|"), TAG_RE.sub("", t["text"]))
        n += len(txt.split())
    return n


def lint(name, meta, turns, cfg):
    warns = []
    for field in ("title", "date", "paper", "link", "sources_read"):
        if not meta.get(field):
            warns.append(f"missing front-matter field: {field}")
    for i, t in enumerate(turns, 1):
        body = TAG_RE.sub("", t["text"])
        if re.search(r"\([^)]*\)|\*|\[|\]", body):
            warns.append(f"turn {i}: looks like a stage direction ((..), *..*, [..]); these may be read aloud")
        stray = [x for x in re.findall(r"<[^>]*>", t["text"]) if not TAG_RE.fullmatch(x)]
        if stray:
            warns.append(f"turn {i}: unusual tag(s) {stray}")
    words = spoken_words(turns)
    mins = words / cfg.get("words_per_minute", 150)
    note = f"{name}: {len(turns)} turns, {words} spoken words, ~{mins:.1f} min at {cfg.get('words_per_minute', 150)} wpm"
    return note, warns


def chunk_turns(turns, max_chars):
    chunks, cur, size = [], [], 0
    for t in turns:
        n = len(t["text"]) + 20
        if cur and size + n > max_chars:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(t)
        size += n
    if cur:
        chunks.append(cur)
    return chunks


# ---------------------------------------------------------------- TTS

def redact(node, depth=0):
    """Shape of an API response with long strings replaced, for error messages."""
    if isinstance(node, dict):
        return {k: redact(v, depth + 1) for k, v in node.items()}
    if isinstance(node, list):
        return [redact(v, depth + 1) for v in node[:5]]
    if isinstance(node, str) and len(node) > 80:
        return f"<str len={len(node)}>"
    return node


def find_audio(node):
    if isinstance(node, dict):
        d = node.get("data")
        if isinstance(d, str) and len(d) > 2000 and (
            node.get("type") == "audio" or str(node.get("mime_type", "")).startswith("audio")
        ):
            return d
        for v in node.values():
            r = find_audio(v)
            if r:
                return r
    elif isinstance(node, list):
        for v in node:
            r = find_audio(v)
            if r:
                return r
    return None


def gemini_chunk(turns, cfg, api_key, out_wav):
    speakers, seen = [], set()
    for s in cfg["speakers"].values():
        if s["name"] not in seen:
            seen.add(s["name"])
            speakers.append({"speaker": s["name"], "voice": s["voice"]})
    content = []
    for t in turns:
        ann = {"type": "speech_metadata", "speaker": t["speaker"]}
        if t["style"]:
            ann["style"] = t["style"]
        content.append({"type": "text", "text": t["text"], "annotations": [ann]})
    body = {
        "model": cfg["model"],
        "input": [{"type": "user_input", "content": content}],
        "response_format": {"type": "audio"},
        "generation_config": {"speech_config": {"mode": "conversational", "speakers": speakers}},
    }
    data = json.dumps(body).encode()
    last = None
    for attempt in range(5):
        req = urllib.request.Request(
            API_URL, data=data, method="POST",
            headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=900) as resp:
                payload = json.loads(resp.read())
            b64 = find_audio(payload)
            if not b64:
                raise SystemExit(
                    "No audio found in API response. Shape was:\n"
                    + json.dumps(redact(payload), indent=2)[:3000]
                )
            raw = base64.b64decode(b64)
            if raw[:4] == b"RIFF":
                out_wav.write_bytes(raw)
            else:  # headerless 24 kHz mono 16-bit PCM
                pcm = out_wav.with_suffix(".pcm")
                pcm.write_bytes(raw)
                run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", "24000", "-ac", "1",
                     "-i", str(pcm), str(out_wav)])
            return
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")[:1500]
            last = f"HTTP {e.code}: {msg}"
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(min(60, 5 * 2 ** attempt))
                continue
            raise SystemExit(f"Gemini TTS request rejected. {last}")
        except (urllib.error.URLError, TimeoutError) as e:
            last = str(e)
            time.sleep(min(60, 5 * 2 ** attempt))
    raise SystemExit(f"Gemini TTS failed after retries: {last}")


def tone_chunk(turns, cfg, out_wav):
    """Dry-run stand-in: a quiet tone as long as the chunk would take to speak."""
    secs = max(1.0, spoken_words(turns) / cfg.get("words_per_minute", 150) * 60)
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
         "-i", f"sine=frequency=220:sample_rate=24000:duration={secs:.2f}",
         "-af", "volume=0.1", "-ac", "1", "-c:a", "pcm_s16le", str(out_wav)])


# ---------------------------------------------------------------- audio

def encode_mp3(wavs, out_mp3, meta, cfg, tmp):
    silence = tmp / "gap.wav"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
         "-i", f"anullsrc=r=24000:cl=mono",
         "-t", str(cfg.get("pause_between_chunks_s", 0.35)), "-c:a", "pcm_s16le", str(silence)])
    lst = tmp / "list.txt"
    lines = []
    for i, w in enumerate(wavs):
        if i:
            lines.append(f"file '{silence}'")
        lines.append(f"file '{w}'")
    lst.write_text("\n".join(lines) + "\n")
    out_mp3.parent.mkdir(parents=True, exist_ok=True)
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ac", "1", "-ar", "44100",
         "-c:a", "libmp3lame", "-b:a", cfg.get("mp3_bitrate", "64k"),
         "-metadata", f"title={meta['title']}", "-metadata", f"artist={cfg['show']['author']}",
         "-metadata", f"album={cfg['show']['title']}", str(out_mp3)])


def duration_s(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "default=nw=1:nk=1", str(path)]).strip())


def make_cover(path, title):
    if path.exists():
        return True
    font = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    try:
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "color=c=0x1f3a5f:s=1400x1400",
             "-vf", f"drawtext=fontfile={font}:text='{title}':fontcolor=white:fontsize=170:"
                    f"x=(w-text_w)/2:y=(h-text_h)/2",
             "-frames:v", "1", "-q:v", "3", str(path)])
        return True
    except RuntimeError:
        return False


# ---------------------------------------------------------------- feed

def base_url():
    if os.environ.get("BASE_URL"):
        return os.environ["BASE_URL"].rstrip("/")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if repo:
        owner, name = repo.split("/")
        host = f"{owner.lower()}.github.io"
        return f"https://{host}" if name.lower() == host else f"https://{host}/{name}"
    return "https://example.invalid"


def build_feed(cfg, manifest, site, out_dir, has_cover):
    ns = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd", "atom": "http://www.w3.org/2005/Atom"}
    for p, u in ns.items():
        ET.register_namespace(p, u)
    feed_url = f"{site}/{cfg['feed_token']}/feed.xml"
    rss = ET.Element("rss", {"version": "2.0"})
    ch = ET.SubElement(rss, "channel")
    show = cfg["show"]

    def sub(parent, tag, text=None, **attrs):
        e = ET.SubElement(parent, tag, attrs)
        if text is not None:
            e.text = text
        return e

    sub(ch, "title", show["title"])
    sub(ch, "link", site)
    sub(ch, "description", show["description"])
    sub(ch, "language", show["language"])
    sub(ch, "{%s}link" % ns["atom"], href=feed_url, rel="self", type="application/rss+xml")
    sub(ch, "{%s}author" % ns["itunes"], show["author"])
    sub(ch, "{%s}explicit" % ns["itunes"], "false")
    sub(ch, "{%s}type" % ns["itunes"], "episodic")
    sub(ch, "{%s}block" % ns["itunes"], "Yes")  # private feed: ask directories not to list it
    cat = ET.SubElement(ch, "{%s}category" % ns["itunes"])
    cat.set("text", show.get("category", "Science"))
    if has_cover:
        sub(ch, "{%s}image" % ns["itunes"], href=f"{site}/{cfg['feed_token']}/cover.jpg")
    for ep in sorted(manifest, key=lambda e: e["pub_date"], reverse=True):
        it = ET.SubElement(ch, "item")
        sub(it, "title", ep["title"])
        sub(it, "description", ep["description"])
        sub(it, "{%s}summary" % ns["itunes"], ep["description"])
        sub(it, "guid", ep["slug"], isPermaLink="false")
        d = dt.datetime.fromisoformat(ep["pub_date"]).replace(tzinfo=dt.timezone.utc)
        sub(it, "pubDate", email.utils.format_datetime(d))
        sub(it, "enclosure", url=f"{site}/{cfg['feed_token']}/audio/{ep['file']}",
            length=str(ep["bytes"]), type="audio/mpeg")
        sub(it, "{%s}duration" % ns["itunes"], str(int(round(ep["duration_s"]))))
        sub(it, "{%s}explicit" % ns["itunes"], "false")
        sub(it, "{%s}episodeType" % ns["itunes"], "full")
    ET.indent(rss)
    out = out_dir / "feed.xml"
    ET.ElementTree(rss).write(out, encoding="utf-8", xml_declaration=True)
    return feed_url


def description_for(meta):
    parts = []
    if meta.get("summary"):
        parts.append(meta["summary"])
    parts.append(f"Paper: {meta['paper']}")
    parts.append(f"Link: {meta['link']}")
    parts.append(f"Sources the script was based on: {meta['sources_read']}")
    if meta.get("caveats"):
        parts.append(f"Caveats: {meta['caveats']}")
    parts.append("AI-generated: script written by Claude, voices synthesized by Gemini TTS. Check claims against the paper.")
    return "\n\n".join(parts)


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--lint", action="store_true")
    ap.add_argument("--export-plain", metavar="EPISODE_MD")
    ap.add_argument("--out", default=str(ROOT / "docs"))
    args = ap.parse_args()
    cfg = load_config()

    if args.export_plain:
        _, turns = parse_episode(Path(args.export_plain), cfg)
        for t in turns:
            print(f"{t['speaker']}: {t['text']}")
        return

    scripts = sorted((ROOT / "episodes").glob("*.md"))
    ready = []
    for p in scripts:
        meta, turns = parse_episode(p, cfg)
        note, warns = lint(p.stem, meta, turns, cfg)
        print(note)
        for w in warns:
            print(f"  warning: {w}")
        if meta.get("status", "draft") == "ready":
            ready.append((p, meta, turns))
    if args.lint:
        return

    out_dir = Path(args.out) / cfg["feed_token"]
    (out_dir / "audio").mkdir(parents=True, exist_ok=True)
    mpath = out_dir / "episodes.json"
    manifest = json.loads(mpath.read_text()) if mpath.exists() else []
    done = {e["slug"] for e in manifest}

    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not args.dry_run and any(p.stem not in done or args.force for p, _, _ in ready) and not api_key:
        raise SystemExit("GEMINI_API_KEY is not set (add it as a GitHub Actions secret).")

    for p, meta, turns in ready:
        slug = p.stem
        if slug in done and not args.force:
            print(f"skip {slug} (already built)")
            continue
        print(f"building {slug} ...")
        chunks = chunk_turns(turns, cfg.get("max_chunk_chars", 3000))
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            wavs = []
            for i, ch in enumerate(chunks):
                w = tmp / f"c{i:03d}.wav"
                print(f"  chunk {i + 1}/{len(chunks)} ({len(ch)} turns)")
                if args.dry_run:
                    tone_chunk(ch, cfg, w)
                else:
                    gemini_chunk(ch, cfg, api_key, w)
                wavs.append(w)
            mp3 = out_dir / "audio" / f"{slug}.mp3"
            encode_mp3(wavs, mp3, meta, cfg, tmp)
        entry = {
            "slug": slug,
            "title": meta["title"],
            "description": description_for(meta),
            "pub_date": meta["date"] + "T07:00:00",
            "file": f"{slug}.mp3",
            "bytes": mp3.stat().st_size,
            "duration_s": duration_s(mp3),
        }
        manifest = [e for e in manifest if e["slug"] != slug] + [entry]
        mpath.write_text(json.dumps(manifest, indent=2))
        print(f"  -> {mp3.name}: {entry['duration_s'] / 60:.1f} min, {entry['bytes'] / 1e6:.1f} MB")

    has_cover = make_cover(out_dir / "cover.jpg", cfg["show"]["title"])
    feed_url = build_feed(cfg, manifest, base_url(), out_dir, has_cover)
    (Path(args.out) / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    (Path(args.out) / "index.html").write_text("<!doctype html><title>.</title>")
    print(f"feed: {feed_url}")


if __name__ == "__main__":
    sys.exit(main())
