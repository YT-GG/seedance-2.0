# V6 Release Readiness

Use this document when checking the active front page before merge.

## Current Release Surface

- README badge, update line, changelog pointer, eval metadata, validator expectations, examples, and active skill metadata must show `6.6.0`.
- Active docs should describe v6 sequence-state architecture, prompt compiler behavior, and Chinese reader paths.
- Historical version details belong in older `CHANGELOG.md` entries, `references/migrated/`, or Git history, not the active README surface.

## Front Page Checks

- The README is simplified for Chinese readers and links to `zh-QUICKSTART.md`, `zh-USAGE.md`, and `docs/README.zh.md`.
- The README explains the split between using the package as a Codex skill and editing or validating it in VS Code.
- Chinese rows link to active skill files and active vocabulary references.
- Non-Chinese translation skills and native-reader guides are no longer required in the simplified package.
- The old planning documents are no longer part of the active docs directory.
- The design doc describes current v6 front-page requirements.

## Validation

Run the repository validation suite from the README before publishing a release or merging a front-page update.
