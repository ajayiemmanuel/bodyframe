# BODYFRAME Annotation Manual v1.1

## Project purpose

BODYFRAME Stage 3 records reproducible visual evidence at image and spatial levels. The system describes camera, framing, orientation, posture, visibility, occlusion, lighting, clothing fit, a manual person box, and a 17-landmark pose. It does not score attractiveness, body quality, posture quality, identity, comfort, or intent.

## Image-level annotation workflow

Use `BF_ANNOT_V1` and complete one record per registered asset in this order:

1. Inspect the whole image.
2. Annotate camera height, camera pitch, and framing.
3. Annotate body and head orientation separately.
4. Record stance and visible posture evidence.
5. Record regional visibility, occlusion level, and occlusion source.
6. Record lighting direction and visible clothing fit.
7. Complete conditional rotation, knee, foot, and elbow fields only where applicable and sufficiently visible.
8. Set confidence, the review flag, and concise factual notes.

Do not reconstruct timestamps. Record one only when captured during annotation.

## Categorical taxonomy usage

Use only the allowed values in the workbook taxonomy. Core fields are required for every annotation. Conditional fields are completed when applicable; otherwise use the defined missing-evidence label. Labels describe visible evidence, not appearance judgments or inferred intent.

`unclear` means the region is visible but cannot be classified confidently. `not_visible` means the relevant region cannot be seen. `not_applicable` means the field genuinely does not apply; it is not a substitute for missing evidence.

## Anatomical left and right

Every left/right label refers to the subject's anatomical left or right, never the viewer's. This convention applies to orientation, shoulder level, weight distribution, rotation, knees, feet, elbows, and keypoint names. If anatomical side cannot be resolved from visible evidence, use `unclear` where allowed and flag review when the uncertainty is consequential.

## BF_ANNOT_V1.1 clarifications

These clarifications originate from the BODYFRAME Stage 4 Calibration and Reviewer Reliability pilot. They refine two existing taxonomy fields without adding, removing, or renaming fields.

### `head_orientation`

- `three_quarter_left` and `three_quarter_right`: both sides of the face remain meaningfully visible, though asymmetrically.
- `profile_left` and `profile_right`: the face is approximately side-on, and the far side contributes little or no visible facial structure.

Do not apply a strict angular threshold; classify from the visible facial structure.

### `torso_visibility`

- `fully_visible`: the complete torso region required by the taxonomy is represented in-frame.
- `partially_visible`: some torso is visible, but part of the torso region itself is removed by crop or meaningful occlusion.

Round 1 and Round 2 annotations remain immutable and are not retroactively changed.

## Manual person bounding box

Create exactly one `person_bbox` for the annotated person. Enclose the visible person extent, exclude unrelated background where practical, and clamp the box to the image boundary when the crop truncates the subject. Do not extend the box beyond the canvas or infer hidden body extent. The manual `person_bbox` is authoritative for the BODYFRAME person bounding box. A pose-derived box from COCO Keypoints is not equivalent and must not replace it.

## Person-pose skeleton

Each `person_pose` skeleton contains exactly 17 keypoints in this order: `nose`, `left_eye`, `right_eye`, `left_ear`, `right_ear`, `left_shoulder`, `right_shoulder`, `left_elbow`, `right_elbow`, `left_wrist`, `right_wrist`, `left_hip`, `right_hip`, `left_knee`, `right_knee`, `left_ankle`, `right_ankle`.

Names and side labels must remain unchanged across files and exports.

## Keypoint placement and visibility

- Place a directly visible keypoint at the center of the visible anatomical landmark and assign COCO visibility `2`.
- Mark a keypoint `occluded` only when it is hidden but can still be localized from visible, image-supported context; retain the localized coordinate and assign COCO visibility `1`.
- Mark a keypoint `outside` when it lies beyond the crop or is not labeled/localizable. Assign COCO visibility `0`; normalized BODYFRAME x/y values must be blank (`null` in JSON).
- Do not infer coordinates for hidden anatomy. An occluded coordinate requires localizable evidence; otherwise use Outside.
- Cropping is not occlusion: cropped landmarks are Outside. Record crop as the image-level occlusion source when appropriate.

CVAT or COCO may retain numeric placeholders for Outside points. BODYFRAME normalization ignores those values and leaves coordinates blank.

## Crop-sensitive categorical rules

A broad stance such as `standing` may remain inferable under some upper-body crops when visible body configuration provides sufficient evidence. This limited stance inference does not authorize filling hidden joint states, pelvis rotation, foot orientation, or other unseen anatomy. Weight distribution requires visible lower-body or support evidence; when that evidence is absent, use `unclear`, not left/right dominance. Use `not_applicable` only when weight distribution genuinely has no meaningful application.

## Confidence and review

Set confidence after the full record is complete: `1` indicates low confidence, `2` substantial uncertainty, `3` generally confident with limited uncertainty, and `4` high confidence with clear evidence. Set `needs_review = yes` when ambiguity, left/right uncertainty, an Outside/Occluded decision, conflicting categorical and spatial evidence, or another inconsistency warrants a second review. Otherwise use `no`. Notes should identify the visible evidence or ambiguity without evaluation.

## Source-of-truth and export policy

- The locked `ImageAnnotationsTable` is the source for human image-level categorical values.
- The CVAT native export (`CVAT for images 1.1`) is the canonical raw spatial annotation source.
- The normalized BODYFRAME spatial and keypoint tables are the canonical analysis representation.
- COCO BBox and COCO Keypoints are interoperability exports; they may transform or omit native information.
- The unified BODYFRAME JSON is derived from the locked image-level table and normalized analysis tables.
- Never replace the manual `person_bbox` with the pose-derived bbox emitted by COCO Keypoints.
