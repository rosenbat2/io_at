# Script style guide (for whoever writes episodes: Claude, interactively or on a schedule)

Goal: a NotebookLM-like two-host conversation, but pitched at a PhD economist. Not cheerful explainer
radio. Two economists who both know industrial organization, one of whom has read the paper closely.

## Hosts
- **MAYA** knows the paper. Explains setting, data, design, results. Precise about what the paper does and does not claim.
- **THEO** is the sharp co-host. Asks the identification questions a referee would ask, pushes on magnitudes, external
  validity, and what a practitioner (agency economist, merger-review lawyer) should take away.

## Length and structure (target about 20 min = about 3,000 spoken words at 150 wpm)
Re-calibrate `words_per_minute` in config.json after the first real episode (measure actual minutes / words).
1. Cold open: the question and why anyone cares (30-60 s).
2. Setting and data. What is observed, what is not.
3. Empirical strategy. The counterfactual, and what has to be true for it to hold.
4. Results, with the paper's own numbers.
5. Threats and critiques. What would change the conclusion. Where the authors are candid and where they are not.
6. What it means for antitrust or IO practice, and how it connects to the neighboring literature.
7. One-line takeaway; tease nothing that is not in the next episode.

## Accuracy rules (non-negotiable)
- Every number, estimate, sample size, and date comes from a source actually read. If only the abstract was available,
  say so in `sources_read` and in `caveats`, and state no figures beyond the abstract.
- Prefer full text (NBER, SSRN, arXiv, author pages, university repositories). Do not "recall" results from memory.
- Mark the paper's own claims versus the hosts' commentary. Commentary should sound like commentary ("I'd worry that...").
- Never read long passages from the paper aloud. Paraphrase; at most a short phrase.
- Put the full citation, a stable link, what was read, and caveats in the front matter. They become the show notes.

## Markup (Gemini TTS)
- One turn per line: `MAYA [optional style]: text`. Style is delivery only (pace, emotion), never identity traits.
- Inline tags at the exact spot: `<short pause>`, `<long pause>`, `<laugh>`, `<sigh>`, `<breath>`. Use sparingly, a few per minute at most.
- Backchannels in pipes inside the other speaker's turn: `|mm-hm|`, `|right|`, `|oh, interesting|`. Keep them short.
- CAPITALIZE a word to add stress. Rarely.
- No stage directions in the text ((laughs), *sighs*): the transcript is read verbatim.
- Spell out numbers and symbols the way they should be said ("twenty ten", "five percent", "H H I").
- Keep turns short and varied. Real conversations have interruptions, half-agreements, and "wait, say that again".

## Front matter fields
title, date (YYYY-MM-DD), status (`draft` or `ready`; only `ready` builds), paper (full citation), link,
sources_read, summary (one or two sentences), caveats. All single-line.
