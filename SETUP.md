# One-time setup (about 15 minutes)

1. **Gemini API key.** Go to https://aistudio.google.com/apikey, create a key. For reliable use turn on billing for the
   project (about $0.30-0.60 per 20-minute episode at current preview pricing; verify on Google's pricing page).
2. **GitHub repo.** Create a new **public** repo (public is required for free GitHub Pages). Pick a boring name.
   Do not add a README or .gitignore (leave it empty).
3. **Add the key as a secret.** Repo -> Settings -> Secrets and variables -> Actions -> New repository secret.
   Name: `GEMINI_API_KEY`. Value: the key.
4. **Enable Pages.** Repo -> Settings -> Pages -> Build and deployment -> Source: **GitHub Actions**.
5. **Put these files in the repo** (either connect GitHub to Claude so it can push, or upload them yourself:
   repo page -> Add file -> Upload files -> drag the *contents* of this folder in, including the hidden `.github` folder -> Commit).
6. **Run it once.** Repo -> Actions -> "Build episodes" -> Run workflow. The first run builds the 2-minute pilot.
   It also runs automatically whenever a new `ready` script is pushed to `episodes/`.
7. **Subscribe in Castro.** Copy the feed URL printed at the end of the run log ("feed: https://...") and
   in Castro: Discover tab -> paste the URL into the search field (older versions: "Paste URL", top right) -> tap the show -> Subscribe.

Notes
- The feed URL contains a random folder name (`feed_token` in config.json). It is unlisted, not access-controlled: the repo is
  public, so anyone who finds the repo can find the audio.
- Episodes are committed to the repo as mp3s (~10 MB per 20-minute episode). GitHub recommends staying under about 1 GB of
  Pages content, so roughly 100 episodes; after that, move audio to cheap object storage.
- Voices, model, and speaking-rate calibration live in `config.json`. Model names for Gemini TTS change; if a run fails with
  a "model not found" error, update `model` there.
