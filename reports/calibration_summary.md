# BODYFRAME Stage 4 Calibration Summary

## Scope

This pilot measures intra-annotator repeatability across 3 matched images. Round 1 and Round 2 annotations remain unchanged.

## Categorical repeatability

| Metric | Result |
| --- | ---: |
| Matched images | 3 |
| Categorical comparisons | 84 |
| Exact matches | 80 |
| Exact categorical agreement | 95.24% |

Disagreements occurred only in `head_orientation` and `torso_visibility`. The exploratory kappa status is `unstable_small_n`. Kappa values are exploratory only because the sample is too small and many fields have no prevalence variation.

## Spatial repeatability

| Metric | Result |
| --- | ---: |
| Mean bounding-box IoU | 0.9917 |
| Median bounding-box IoU | 0.9941 |
| Keypoint visibility agreement | 100% |
| Coordinate-comparable keypoints | 25 |
| Mean keypoint distance | 44.60 px |
| Median keypoint distance | 28.56 px |
| Mean normalized distance | 0.008849 |
| Median normalized distance | 0.005666 |

## Spatial instability

Among coordinate-comparable records in `keypoint_repeatability.csv`:

- Highest disagreement: `right_shoulder` for `BF_S001_0003_ORIGINAL`, 179.05 px (normalized distance 0.035526).
- Lowest disagreement: `left_ear` for `BF_S001_0003_ORIGINAL`, 3.34 px (normalized distance 0.000662).

These values describe repeat placement differences only; the source annotations are neither modified nor reinterpreted.

## Interpretation and limitations

- This is intra-annotator repeatability, not inter-annotator reliability.
- Only 3 images were used.
- The images are upper-body-heavy.
- Full-body landmark repeatability has not been demonstrated.
- Inter-annotator reliability has not been tested.
- Kappa values are exploratory only.

The pilot supports the annotation architecture while identifying two categorical definitions for clarification. Larger and more varied samples, including full-body images and additional annotators, are required for reliability claims.
