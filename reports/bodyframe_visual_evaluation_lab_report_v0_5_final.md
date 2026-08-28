# BODYFRAME Visual Evaluation Lab Report v0.5 — Final

## Executive summary

BODYFRAME 0.5 now connects a three-image architecture/calibration pilot with a later 12-image coverage expansion. The combined release contains 15 registered and annotated originals, 15 manual person boxes, 15 skeletons, and 255 normalized keypoint rows. The expansion substantially improves pose, framing, orientation, and lower-body landmark coverage while preserving the original pilot's historical taxonomy and calibration scope.

Release-gate result: **PASS_WITH_DOCUMENTED_LIMITATIONS**. This supports a governed pilot release, not population-level, model-performance, fairness, or general reliability claims.

## Stage 1 — Intake and lineage

The 12 expansion originals are registered under S002–S011 and all passed the established intake pipeline. Together with the three S001 originals, the annotation dataset spans 11 subject groups. Immutable asset and source-image identifiers connect every categorical and spatial row to the registry.

## Stage 2 — Technical quality

The technical-quality audit remains the earlier 18-asset S001 experiment: three originals plus 15 controlled variants. Expansion images were not assigned new technical-quality scores or synthetic derivatives. Automated metrics remain evidence rather than automatic pass/fail thresholds.

## Stage 3 — Annotation system and expansion

The original three images established the `BF_ANNOT_V1` categorical and 17-keypoint spatial architecture. The 12-image expansion uses clarified `BF_ANNOT_V1.1`; pilot rows remain unchanged. The combined outputs contain 15 image rows, 15 authoritative manual bboxes, and 255 named keypoints.

CVAT for images 1.1 remains canonical. COCO BBox correctly represents manual boxes as xywh and omits skeletons. COCO Keypoints converts visible/Occluded/Outside to 2/1/0, retains numeric placeholders for some Outside points, and emits pose-derived boxes. BODYFRAME normalization blanks Outside coordinates and never substitutes pose-derived boxes for the manual person bbox.

## Stage 4 — Calibration boundary

Calibration is unchanged: one annotator repeated the original three images only. The prior 95.24% categorical agreement, 0.9917 mean bbox IoU, 100% keypoint-visibility agreement, and exploratory `unstable_small_n` kappa status apply only to that architecture pilot. The 12 expansion images did **not** receive Round 2 calibration, and inter-annotator reliability remains untested.

## Stage 5 — Post-expansion diagnostics

Categorical fields with more than one observed value increased from 5/28 to 27/28. Keypoints with 0% coordinate coverage fell from 8 to 0. Pooled valid-coordinate coverage changed as follows: wrists 0.0% → 76.7%; hips 0.0% → 80.0%; knees 0.0% → 66.7%; ankles 0.0% → 60.0%.

The expansion introduced 9 full-body annotations, 3 seated annotations, 1 rear-facing annotation, 7 non-neutral torso rotations, and 5 left/right-dominant support labels. It also provides dynamic-pose evidence through non-upright lean, non-neutral rotation, and `other` stance labels. Exclusive single-leg support is not explicitly encoded and is not claimed.

## Release criteria

- **PASS** — 15 registered/annotated originals.
- **PASS** — multiple subject groups.
- **PASS** — multiple framing categories.
- **PASS** — multiple body/head orientations.
- **PASS** — multiple stance/posture categories.
- **PASS** — lower-body keypoint coordinate coverage > 0.
- **PASS** — wrists/hips/knees/ankles represented.
- **PASS** — dynamic pose coverage.
- **PASS** — categorical taxonomy no longer nearly constant.
- **PASS** — expansion passed intake.
- **PASS** — spatial exports validated.
- **PASS** — remaining limitations documented.


## Remaining limitations

- Fifteen originals remain a small dataset.
- One annotator completed the expansion; no expansion Round 2 and no inter-annotator calibration exist.
- Some keypoints remain partially covered; the lowest are left_ankle (60.0%), right_ankle (60.0%), left_knee (66.7%), right_knee (66.7%).
- Single-leg support cannot be confirmed from the current taxonomy alone.
- The dataset cannot support population, fairness, general pose-performance, or broad reliability claims.

## Conclusion

BODYFRAME 0.5 passes the specified pilot release gates with documented limitations. The connected registry, intake, categorical, spatial, interoperability, and diagnostic outputs are ready for controlled downstream pilot use. Broader claims require more subjects, sessions, pose strata, and multi-annotator calibration.
