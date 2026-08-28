# BODYFRAME Dataset Card v0.5 — Final

## Dataset purpose

BODYFRAME is a governed visual-evaluation laboratory spanning file intake, technical image quality, image-level annotation, spatial annotation, calibration, and dataset diagnostics. Version 0.5 contains **15 registered and annotated original images** across **11 subject groups**. It remains a small research dataset and is not a representative population sample.

## Dataset composition and lineage

The canonical lineage is `subject → capture session → source image → asset → variant → evaluation`. The master registry contains **15 originals and 20 derivatives (35 assets total)**. The original three-image S001 set established the architecture, technical-quality workflow, annotation system, and calibration pilot. A later 12-image expansion added S002–S011 to improve categorical and spatial coverage.

All 12 expansion originals passed the established Stage 1 intake pipeline. The combined annotation release contains 15 image-level rows, 15 authoritative manual person boxes, 15 person-pose skeletons, and 255 normalized keypoint rows.

## Annotation taxonomy

The pilot's locked historical rows retain `BF_ANNOT_V1`; expansion rows use `BF_ANNOT_V1.1`. Version 1.1 clarifies `head_orientation` and `torso_visibility` without adding or removing taxonomy fields. Labels describe visible evidence, use the subject's anatomical left/right, and distinguish `unclear`, `not_visible`, and `not_applicable`.

Categorical fields with more than one observed value increased from **5/28** in the pilot to **27/28** in the combined dataset. Full-body, seated, rear-facing, asymmetric-support, non-neutral rotation, and broader framing/lighting/occlusion configurations are now represented.

## Spatial annotations

CVAT for images 1.1 is the canonical raw spatial source. Normalized BODYFRAME tables are the canonical analysis representation; COCO BBox and COCO Keypoints remain interoperability exports. Each image has one manual `person_bbox` and one named 17-keypoint `person_pose`. Pose-derived COCO boxes do not replace manual boxes.

All 17 landmarks now have nonzero valid-coordinate coverage. Pooled wrist, hip, knee, and ankle coverage changed from 0.0%, 0.0%, 0.0%, and 0.0% in the pilot to 76.7%, 80.0%, 66.7%, and 60.0% in v0.5.

## Technical quality and calibration scope

Stage 2 remains a controlled 18-asset technical-quality experiment derived from the original S001 images; the expansion originals were not given new synthetic technical variants or Stage 2 human scores. Stage 4 repeatability also remains limited to the original three images and one annotator. The 12 expansion images did **not** receive Round 2 calibration, so expansion-scale repeatability and inter-annotator reliability are unmeasured.

## Intended use

- Validate connected intake, registry, annotation, export, and diagnostic workflows.
- Exercise categorical and spatial coverage analysis on a small multi-subject set.
- Support carefully scoped pilot experiments that acknowledge the dataset's size and calibration limits.

## Inappropriate use

- Do not make population, fairness, biometric, identity, attractiveness, health, body-quality, or posture-quality claims.
- Do not treat this dataset as evidence of general pose-model accuracy or annotation reliability.
- Do not infer single-leg support solely from a left/right-dominant weight label.

## Privacy and governance

Original images remain private. Analysis outputs use immutable BODYFRAME identifiers. Publication or model-use decisions require the project's existing consent, access-control, and publication-status review.

## Remaining limitations

- Only 15 originals and one categorical/spatial annotator.
- Round 2 calibration covers only the original three-image pilot; no expansion calibration and no inter-annotator reliability.
- Single-leg support is not explicitly encoded.
- Some keypoints have partial rather than universal coordinate coverage; the lowest are left_ankle (60.0%), right_ankle (60.0%), left_knee (66.7%), right_knee (66.7%).
- Capture, subject, and pose coverage remains too small for broad generalization.

## Release status

BODYFRAME 0.5 release-gate result: **PASS_WITH_DOCUMENTED_LIMITATIONS**. The data and export architecture pass the specified pilot release criteria, with the limitations above carried forward as explicit constraints.
