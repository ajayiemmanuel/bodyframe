"""Technical image measurements used by the BODYFRAME 0.5 audit.

The returned measurements are evidence only. They do not assign human scores
or technical pass/fail decisions.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image


LUMINANCE_WEIGHTS = np.asarray((0.2126, 0.7152, 0.0722), dtype=np.float64)


def laplacian_variance(grayscale: np.ndarray) -> float:
    """Return variance of the four-neighbour 3×3 Laplacian response.

    BODYFRAME computes this on Pillow ``L`` grayscale pixels and excludes the
    one-pixel image border. The value is sharpness evidence, not a quality score.
    """

    pixels = np.asarray(grayscale, dtype=np.float64)
    if pixels.ndim != 2 or pixels.shape[0] < 3 or pixels.shape[1] < 3:
        raise ValueError("grayscale must be a two-dimensional array at least 3×3")
    response = (
        pixels[:-2, 1:-1]
        + pixels[2:, 1:-1]
        + pixels[1:-1, :-2]
        + pixels[1:-1, 2:]
        - 4.0 * pixels[1:-1, 1:-1]
    )
    return float(np.var(response))


def compute_image_metrics(image_path: str | Path) -> dict[str, Any]:
    """Measure one readable image without modifying it.

    Brightness uses Rec. 709 luminance on a 0–255 scale. Clipping values are
    proportions, with shadows at luminance <= 5 and highlights at >= 250.
    """

    path = Path(image_path)
    file_size_bytes = path.stat().st_size
    with Image.open(path) as image:
        image.load()
        width_px, height_px = image.size
        rgb_image = image.convert("RGB")
        rgb = np.asarray(rgb_image, dtype=np.float64)
        grayscale = np.asarray(image.convert("L"), dtype=np.float64)

    luminance = rgb @ LUMINANCE_WEIGHTS
    channel_means = np.mean(rgb, axis=(0, 1))
    return {
        "file_size_bytes": int(file_size_bytes),
        "width_px": int(width_px),
        "height_px": int(height_px),
        "mean_brightness": float(np.mean(luminance)),
        "brightness_std": float(np.std(luminance)),
        "shadow_clip_pct": float(np.mean(luminance <= 5.0)),
        "highlight_clip_pct": float(np.mean(luminance >= 250.0)),
        "laplacian_variance": laplacian_variance(grayscale),
        "red_mean": float(channel_means[0]),
        "green_mean": float(channel_means[1]),
        "blue_mean": float(channel_means[2]),
    }
