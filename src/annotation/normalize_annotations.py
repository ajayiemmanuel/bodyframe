"""Normalize BODYFRAME spatial annotations from canonical native CVAT values.

Native CVAT is the canonical raw spatial source. Normalized BODYFRAME rows are
the analysis representation; interoperability exports do not override them.
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from typing import Any


KEYPOINT_NAMES = (
    "nose",
    "left_eye",
    "right_eye",
    "left_ear",
    "right_ear",
    "left_shoulder",
    "right_shoulder",
    "left_elbow",
    "right_elbow",
    "left_wrist",
    "right_wrist",
    "left_hip",
    "right_hip",
    "left_knee",
    "right_knee",
    "left_ankle",
    "right_ankle",
)


def _flag(value: Any) -> bool:
    if isinstance(value, str):
        token = value.strip().lower()
        if token in {"", "0", "false", "no"}:
            return False
        if token in {"1", "true", "yes"}:
            return True
        raise ValueError(f"Unsupported CVAT flag value: {value!r}")
    return bool(value)


def _coordinate(value: Any) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("Keypoint coordinates must be finite")
    return number


def anatomical_side(keypoint_name: str) -> str:
    """Return subject-anatomical side for a BODYFRAME keypoint."""

    if keypoint_name.startswith("left_"):
        return "left"
    if keypoint_name.startswith("right_"):
        return "right"
    return "midline"


def normalize_cvat_keypoint(
    keypoint_name: str,
    x: Any,
    y: Any,
    *,
    outside: Any = False,
    occluded: Any = False,
) -> dict[str, Any]:
    """Map one native CVAT point to BODYFRAME/COCO visibility semantics.

    Outside points receive COCO visibility 0 and blank normalized coordinates.
    Occluded but localized points retain coordinates and receive 1. Directly
    visible points retain coordinates and receive 2.
    """

    if keypoint_name not in KEYPOINT_NAMES:
        raise ValueError(f"Unknown BODYFRAME keypoint: {keypoint_name!r}")
    is_outside = _flag(outside)
    is_occluded = _flag(occluded)
    if is_outside:
        x_px = y_px = None
        visibility_state = "outside"
        coco_visibility = 0
        in_frame = "no"
    else:
        x_px, y_px = _coordinate(x), _coordinate(y)
        visibility_state = "occluded" if is_occluded else "directly_visible"
        coco_visibility = 1 if is_occluded else 2
        in_frame = "yes"
    return {
        "keypoint_name": keypoint_name,
        "x_px": x_px,
        "y_px": y_px,
        "visibility_state": visibility_state,
        "coco_visibility": coco_visibility,
        "anatomical_side": anatomical_side(keypoint_name),
        "in_frame": in_frame,
    }


def normalize_keypoint_rows(records: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Validate and normalize exactly one complete 17-keypoint skeleton.

    Input records use ``keypoint_name``, ``x``, ``y``, ``outside``, and
    ``occluded``. Output is ordered by the established BODYFRAME keypoint order.
    """

    indexed: dict[str, Mapping[str, Any]] = {}
    for record in records:
        name = str(record["keypoint_name"])
        if name in indexed:
            raise ValueError(f"Duplicate keypoint: {name}")
        indexed[name] = record
    missing = [name for name in KEYPOINT_NAMES if name not in indexed]
    extra = [name for name in indexed if name not in KEYPOINT_NAMES]
    if missing or extra:
        raise ValueError(f"Keypoint set mismatch; missing={missing}, extra={extra}")
    return [
        normalize_cvat_keypoint(
            name,
            indexed[name].get("x"),
            indexed[name].get("y"),
            outside=indexed[name].get("outside", False),
            occluded=indexed[name].get("occluded", False),
        )
        for name in KEYPOINT_NAMES
    ]


def normalize_manual_bbox(
    x_min: float,
    y_min: float,
    x_max: float,
    y_max: float,
    *,
    image_width: float,
    image_height: float,
) -> dict[str, float | str]:
    """Validate a manual ``person_bbox`` and calculate its dimensions.

    The function never derives a box from pose keypoints and never changes the
    supplied coordinates.
    """

    values = tuple(float(value) for value in (x_min, y_min, x_max, y_max))
    x_min, y_min, x_max, y_max = values
    if not all(math.isfinite(value) for value in values):
        raise ValueError("Bounding-box coordinates must be finite")
    if image_width <= 0 or image_height <= 0:
        raise ValueError("Image dimensions must be positive")
    if not (0 <= x_min < x_max <= image_width and 0 <= y_min < y_max <= image_height):
        raise ValueError("Manual bounding box must be ordered and within the image")
    width = x_max - x_min
    height = y_max - y_min
    return {
        "bbox_x_min": x_min,
        "bbox_y_min": y_min,
        "bbox_x_max": x_max,
        "bbox_y_max": y_max,
        "bbox_width": width,
        "bbox_height": height,
        "bbox_area": width * height,
        "bbox_source": "person_bbox (native CVAT)",
    }
