# BODYFRAME Keypoint Schema

BODYFRAME uses one `person_pose` skeleton with 17 COCO-style keypoints in this normalized analysis order:

1. `nose`
2. `left_eye`
3. `right_eye`
4. `left_ear`
5. `right_ear`
6. `left_shoulder`
7. `right_shoulder`
8. `left_elbow`
9. `right_elbow`
10. `left_wrist`
11. `right_wrist`
12. `left_hip`
13. `right_hip`
14. `left_knee`
15. `right_knee`
16. `left_ankle`
17. `right_ankle`

Left and right always refer to the subject's anatomical left and right, never the viewer's.

## Visibility states

- **Visible**: landmark is directly visible and localized; COCO visibility `2`.
- **Occluded**: landmark is hidden but localized from image-supported evidence; COCO visibility `1`.
- **Outside**: landmark is cropped, off-frame, or not localizable; COCO visibility `0` and normalized x/y values are blank.

Do not infer hidden or off-frame coordinates. A manual `person_bbox` remains authoritative; a pose-derived box must not replace it.
