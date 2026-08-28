# BODYFRAME ID and Lineage Rules

## Identifier patterns

- Subject: `S###`
- Capture session: `CS###`
- Source image: `BF_S###_####`
- Original asset: `BF_S###_####_ORIGINAL`
- Derivative asset: `BF_S###_####_<VARIANT>_<LEVEL>`
- Managed original filename: `BF_S###_####.<ext>`
- Managed derivative filename: `BF_S###_####__<variant>_<level>.<ext>`

Assigned identifiers are immutable, unique, and never reused.

## Lineage

The canonical relationship is `subject → capture session → source image → asset → evaluation`.

- Every source image belongs to one subject and one capture session.
- Every asset references an existing `source_image_id`.
- Original assets have no parent.
- Every derivative has a valid `parent_asset_id`, and parent and derivative share the same `source_image_id`.
- Human reviews, annotations, and automated metrics join through immutable asset identifiers.
- Filesystem pointers are project-relative. Private storage values and source-provider filenames are not public-release data.
