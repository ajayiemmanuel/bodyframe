# BODYFRAME Methodology

## Intake

Registered assets are checked for existence, readability, extension/format agreement, MIME type, size, dimensions, aspect ratio, orientation, bit depth, colour mode, ICC profile, optional EXIF fields, SHA-256, exact duplicates, filename rules, folder rules, and required metadata. EXIF is recorded when present but is not mandatory.

## Technical quality

The validated Stage 2 pilot reviewed 3 originals and 15 controlled variants. Automated metrics were retained as evidence and compared with blinded human judgements; no arbitrary metric-based pass/fail threshold was introduced.

## Annotation

Image-level annotations use evidence-only categorical labels. Spatial annotation uses one manual `person_bbox` and one 17-keypoint `person_pose`. CVAT native export is canonical; normalized BODYFRAME tables are canonical for analysis. Visible, Occluded, and Outside map to COCO visibility 2, 1, and 0. Outside coordinates are blanked during normalization.

## Calibration

The same annotator repeated the original three-image pilot. This measured intra-annotator repeatability only. The later 12-image expansion did not receive Round 2 calibration, and inter-annotator reliability has not been tested.

## Dataset diagnostics

The combined v0.5 release contains 15 original images, 15 categorical records, 15 manual boxes, 15 skeletons, and 255 normalized keypoint rows. Categorical fields with more than one observed value increased from 5/28 to 27/28. Pooled valid-coordinate coverage reached 76.7% for wrists, 80.0% for hips, 66.7% for knees, and 60.0% for ankles. These are pilot diagnostics, not general model-performance claims.
