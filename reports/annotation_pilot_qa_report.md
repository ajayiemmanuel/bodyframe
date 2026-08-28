# BODYFRAME Stage 3 Pilot QA Report

## Dataset

- 3 original images
- 3 image-level annotations
- 3 manual person bounding boxes
- 3 `person_pose` skeletons
- 51 normalized keypoint records
- Visibility totals: 23 directly visible, 2 occluded but localized, and 26 Outside

All three assets map to available original records in the BODYFRAME master registry. The validated spatial tables contain one manual box and one 17-keypoint skeleton per image.

## Pilot findings

- Anatomical left/right required explicit clarification: all side labels refer to the subject, not the viewer.
- Outside and Occluded required an explicit distinction. Occluded means hidden but localized; Outside means cropped out or not validly localized.
- Separating head orientation from body orientation proved useful because the two can differ in the same image.
- `standing` could remain inferable under some crops when visible body configuration supplied sufficient evidence.
- Weight distribution required lower-body or support evidence; upper-body evidence alone was insufficient.
- Hidden anatomy should not be inferred. Cropped joints, rotations, and foot orientations remain unlocalized or `not_visible`.
- The manual person bbox and pose-derived COCO Keypoints bbox are not equivalent. The manual `person_bbox` remains authoritative.

## Export findings

- COCO BBox represents boxes as `(x, y, width, height)` (`xywh`) instead of CVAT corner coordinates.
- COCO BBox omits skeleton annotations, although related categories may remain in metadata.
- COCO Keypoints converts CVAT visibility states to COCO codes: visible `2`, occluded `1`, Outside `0`.
- The required 17-keypoint order is preserved in the CVAT skeletons and COCO Keypoints category.
- Numeric coordinates for Outside points may survive in COCO, even though BODYFRAME normalization blanks them because they are not valid localizations.
- COCO Keypoints emits a pose-derived bbox based on non-Outside pose points; it must not replace the manual bbox.

## Limitations

- One subject
- Three images
- One annotator
- Similar capture conditions
- Upper-body-heavy crops
- No inter-annotator agreement measurement yet

## Conclusion

The pilot validates the Stage 3 annotation architecture, including the categorical taxonomy, manual bounding boxes, 17-keypoint pose model, visibility normalization, and export policy. Annotator calibration and reviewer reliability are handled in Stage 4.
