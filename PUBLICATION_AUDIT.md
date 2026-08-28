# Publication Audit

## Result

**PASS** — the staging copy passed the publication-safety and integrity checks below.

## Scope

The audit covered all 51 files under `public_release/`, including Markdown,
CSV, Python, notebook JSON, configuration text, and PNG charts. Source project
files outside the staging directory were read only.

## Publication-safety checks

| Check | Result | Finding |
|---|---|---|
| Private or original image files | PASS | 0 staged; `sample_data/images/` is empty. |
| Raw CVAT archives or ZIP files | PASS | 0 staged. |
| Backups | PASS | 0 staged. |
| Absolute or user-home paths | PASS | 0 findings. |
| Personal username, email, or phone data | PASS | 0 findings. |
| Third-party source filenames | PASS | 0 findings. |
| EXIF or location values | PASS | 0 staged records or values. |
| Credentials, tokens, or secrets | PASS | 0 findings. |
| Temporary, debug, or scratch material | PASS | 0 findings. |
| Unexpected large binaries | PASS | 0 files over 5 MiB. |
| Private registry or image-dependent annotation rows | PASS | 0 staged; schemas contain definitions only. |

The intake implementation contains one intentional relative rule reference to
`data/private_images/originals/`. It is a path-validation pattern, not a local
absolute path, file listing, or data reference. The public `.gitignore` blocks
that directory and related private/raw locations.

## Integrity checks

- All nine staged Python files parse and import successfully;
  `src/intake_validation.py` also runs its `--help` interface.
- The five functional modules reproduce the established calculations: 18
  technical metric records, 255 keypoint visibility normalizations, 15 manual
  boxes, 84 categorical comparisons, three bbox IoUs, 25 comparable keypoint
  distances, 102 categorical coverage rows, and 17 keypoint coverage rows.
- The reproduced categorical result remains 80/84 exact matches. Regression
  checks read canonical inputs without writing or changing validated outputs.
- `notebooks/intake_validation.ipynb` is valid notebook JSON (nbformat 4), has
  executable code cells, and contains no stored outputs.
- All 17 staged PNG charts open and verify successfully with Pillow.
- `schemas/annotation_taxonomy.csv` contains 35 schema rows;
  `schemas/registry_schema.csv` contains 22 schema rows; neither contains data rows.
- `RELEASE_MANIFEST.md` covers the complete staging inventory.
- No Git repository was initialized and no commit or push was performed.

## Release gate

Code and documentation pass the sanitization audit. Publication remains subject
to license selection and any future sample-image redistribution review, as
recorded in `LICENSE_PENDING.md` and `sample_data/README.md`.
