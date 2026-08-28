"""Repeatability calculations used by the BODYFRAME Stage 4 pilot."""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence
from typing import Any


SMALL_N_KAPPA_LIMITATION = (
    "Kappa is exploratory for small samples and can be unstable or undefined "
    "when categories have little prevalence variation."
)


def categorical_exact_agreement(
    round_one: Iterable[Any], round_two: Iterable[Any]
) -> dict[str, int | float]:
    """Count elementwise exact matches between equally sized value sequences."""

    left, right = list(round_one), list(round_two)
    if len(left) != len(right):
        raise ValueError("Categorical sequences must have equal lengths")
    comparisons = len(left)
    matches = sum(a == b for a, b in zip(left, right))
    agreement = matches / comparisons if comparisons else math.nan
    return {
        "comparisons": comparisons,
        "exact_matches": matches,
        "exact_agreement": agreement,
    }


def _box(box: Sequence[float]) -> tuple[float, float, float, float]:
    if len(box) != 4:
        raise ValueError("Boxes must contain x_min, y_min, x_max, y_max")
    values = tuple(float(value) for value in box)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("Box coordinates must be finite")
    x_min, y_min, x_max, y_max = values
    if x_max <= x_min or y_max <= y_min:
        raise ValueError("Boxes must have positive width and height")
    return x_min, y_min, x_max, y_max


def bbox_iou(box_a: Sequence[float], box_b: Sequence[float]) -> float:
    """Return intersection-over-union for two corner-coordinate boxes."""

    ax1, ay1, ax2, ay2 = _box(box_a)
    bx1, by1, bx2, by2 = _box(box_b)
    intersection_width = max(0.0, min(ax2, bx2) - max(ax1, bx1))
    intersection_height = max(0.0, min(ay2, by2) - max(ay1, by1))
    intersection = intersection_width * intersection_height
    union = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - intersection
    return intersection / union


def keypoint_distance(point_a: Sequence[float], point_b: Sequence[float]) -> float:
    """Return Euclidean pixel distance between two localized keypoints."""

    if len(point_a) != 2 or len(point_b) != 2:
        raise ValueError("Points must contain x and y")
    ax, ay, bx, by = *(float(value) for value in point_a), *(float(value) for value in point_b)
    if not all(math.isfinite(value) for value in (ax, ay, bx, by)):
        raise ValueError("Keypoint coordinates must be finite")
    return math.hypot(ax - bx, ay - by)


def normalized_keypoint_distance(
    point_a: Sequence[float],
    point_b: Sequence[float],
    *,
    image_width: float,
    image_height: float,
) -> float:
    """Normalize pixel distance by the image diagonal."""

    diagonal = math.hypot(float(image_width), float(image_height))
    if not math.isfinite(diagonal) or diagonal <= 0:
        raise ValueError("Image dimensions must define a positive finite diagonal")
    return keypoint_distance(point_a, point_b) / diagonal
