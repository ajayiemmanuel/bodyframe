# Technical-quality implementation

`quality_metrics.py` packages the image measurements already used by the
validated Stage 2 audit. It calculates dimensions, file size, luminance,
clipping, Laplacian variance, and RGB means without assigning human scores or
pass/fail outcomes. One-off variant-generation and inspection helpers remain
excluded.
