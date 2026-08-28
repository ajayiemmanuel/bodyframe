"""BODYFRAME spatial-annotation normalization helpers."""

from .normalize_annotations import (
    KEYPOINT_NAMES,
    normalize_cvat_keypoint,
    normalize_keypoint_rows,
    normalize_manual_bbox,
)

__all__ = [
    "KEYPOINT_NAMES",
    "normalize_cvat_keypoint",
    "normalize_keypoint_rows",
    "normalize_manual_bbox",
]
