# Annotation implementation

`normalize_annotations.py` packages the validated Stage 3 visibility,
17-keypoint ordering, anatomical-side, and manual bounding-box rules. It
normalizes explicit native values only; it does not parse private exports,
rewrite human labels, infer Outside coordinates, or derive a replacement box
from pose points.
