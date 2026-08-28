"""Coverage summaries used by BODYFRAME 0.5 dataset diagnostics."""

from __future__ import annotations

from collections.abc import Sequence

import pandas as pd


def _require_columns(frame: pd.DataFrame, columns: Sequence[str]) -> None:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def categorical_value_counts(
    annotations: pd.DataFrame, fields: Sequence[str]
) -> pd.DataFrame:
    """Return observed value counts, proportions, and diversity by field.

    Missing cells are excluded from observed categories. The input DataFrame is
    not modified.
    """

    _require_columns(annotations, fields)
    rows: list[dict[str, object]] = []
    total_rows = len(annotations)
    for field in fields:
        values = annotations[field].dropna()
        counts = values.value_counts(sort=False)
        unclear_count = int((values == "unclear").sum())
        not_visible_count = int((values == "not_visible").sum())
        distinct = int(values.nunique())
        for observed_value, observed_count in counts.items():
            rows.append(
                {
                    "field_name": field,
                    "observed_value": observed_value,
                    "observed_count": int(observed_count),
                    "observed_pct": float(observed_count / total_rows) if total_rows else 0.0,
                    "unclear_count": unclear_count,
                    "not_visible_count": not_visible_count,
                    "distinct_observed_categories": distinct,
                }
            )
    return pd.DataFrame.from_records(rows)


def keypoint_visibility_counts(keypoints: pd.DataFrame) -> pd.DataFrame:
    """Summarize visibility and valid-coordinate coverage by keypoint name."""

    required = ("keypoint_name", "visibility_state", "x_px", "y_px")
    _require_columns(keypoints, required)
    rows: list[dict[str, object]] = []
    for keypoint_name, group in keypoints.groupby("keypoint_name", sort=False):
        visibility = group["visibility_state"]
        valid_coordinates = (
            group["x_px"].notna()
            & group["y_px"].notna()
            & visibility.ne("outside")
        )
        total = len(group)
        rows.append(
            {
                "keypoint_name": keypoint_name,
                "visible_keypoint_count": int(visibility.eq("directly_visible").sum()),
                "occluded_keypoint_count": int(visibility.eq("occluded").sum()),
                "outside_keypoint_count": int(visibility.eq("outside").sum()),
                "distinct_visibility_states": int(visibility.dropna().nunique()),
                "valid_coordinate_count": int(valid_coordinates.sum()),
                "valid_coordinate_pct": float(valid_coordinates.mean()) if total else 0.0,
            }
        )
    return pd.DataFrame.from_records(rows)
