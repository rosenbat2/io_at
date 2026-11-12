# IO Papers podcast pipeline

Script (markdown) -> Gemini TTS (two voices) -> ffmpeg mp3 -> RSS feed -> GitHub Pages -> Castro.

- `episodes/*.md`: one script per episode (front matter + `MAYA:` / `THEO:` turns). See `STYLE.md`.
- `tools/build.py`: builds every `status: ready` episode not yet built. `--dry-run` tests the pipeline with tones, `--lint` checks scripts.
- `.github/workflows/build.yml`: runs the builder on GitHub, commits audio + feed to `docs/`, deploys Pages.
- `config.json`: show metadata, model, voices, feed folder token.
- `SETUP.md`: one-time setup.
