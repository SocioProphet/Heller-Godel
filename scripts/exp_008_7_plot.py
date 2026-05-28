#!/usr/bin/env python3
"""Render simple PNG plots for HG-EXP-008.7 without external dependencies."""

from __future__ import annotations

import argparse
import csv
import struct
import zlib
from collections import defaultdict
from math import log
from pathlib import Path


WIDTH = 900
HEIGHT = 520
MARGIN_LEFT = 70
MARGIN_RIGHT = 30
MARGIN_TOP = 40
MARGIN_BOTTOM = 70
COLORS = {
    "small": (31, 119, 180),
    "medium": (255, 127, 14),
    "large": (44, 160, 44),
}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack("!I", len(data)) + kind + data + struct.pack("!I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def write_png(path: Path, width: int, height: int, pixels: bytearray) -> None:
    raw = bytearray()
    stride = width * 3
    for y in range(height):
        raw.append(0)
        raw.extend(pixels[y * stride : (y + 1) * stride])
    data = b"\x89PNG\r\n\x1a\n"
    data += png_chunk(b"IHDR", struct.pack("!IIBBBBB", width, height, 8, 2, 0, 0, 0))
    data += png_chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    data += png_chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def set_pixel(pixels: bytearray, x: int, y: int, color: tuple[int, int, int]) -> None:
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        idx = (y * WIDTH + x) * 3
        pixels[idx : idx + 3] = bytes(color)


def draw_line(pixels: bytearray, x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int]) -> None:
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        set_pixel(pixels, x0, y0, color)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


def draw_point(pixels: bytearray, x: int, y: int, color: tuple[int, int, int]) -> None:
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            set_pixel(pixels, x + dx, y + dy, color)


def scale(value: float, lo: float, hi: float, out_lo: int, out_hi: int) -> int:
    if hi == lo:
        return (out_lo + out_hi) // 2
    return int(out_lo + (value - lo) * (out_hi - out_lo) / (hi - lo))


def render(rows: list[dict[str, str]], cost_field: str, out: Path) -> None:
    points: list[tuple[float, float, str]] = []
    for row in rows:
        cost = float(row[cost_field])
        if cost <= 0:
            continue
        points.append((float(row["omega"]), log(cost, 2), row["magnitude_band"]))
    if not points:
        raise ValueError("no plottable rows")

    x_lo = min(p[0] for p in points) - 0.2
    x_hi = max(p[0] for p in points) + 0.2
    y_lo = min(p[1] for p in points) - 0.5
    y_hi = max(p[1] for p in points) + 0.5
    pixels = bytearray([255] * WIDTH * HEIGHT * 3)
    black = (0, 0, 0)
    grey = (220, 220, 220)

    # Axes and grid.
    x_axis_y = HEIGHT - MARGIN_BOTTOM
    y_axis_x = MARGIN_LEFT
    draw_line(pixels, y_axis_x, MARGIN_TOP, y_axis_x, x_axis_y, black)
    draw_line(pixels, y_axis_x, x_axis_y, WIDTH - MARGIN_RIGHT, x_axis_y, black)
    for omega in range(int(x_lo) + 1, int(x_hi) + 1):
        x = scale(omega, x_lo, x_hi, MARGIN_LEFT, WIDTH - MARGIN_RIGHT)
        draw_line(pixels, x, MARGIN_TOP, x, x_axis_y, grey)
    for i in range(6):
        yv = y_lo + i * (y_hi - y_lo) / 5
        y = scale(yv, y_lo, y_hi, x_axis_y, MARGIN_TOP)
        draw_line(pixels, y_axis_x, y, WIDTH - MARGIN_RIGHT, y, grey)

    # Points.
    for omega, log_cost, band in points:
        x = scale(omega, x_lo, x_hi, MARGIN_LEFT, WIDTH - MARGIN_RIGHT)
        y = scale(log_cost, y_lo, y_hi, x_axis_y, MARGIN_TOP)
        draw_point(pixels, x, y, COLORS.get(band, black))

    # Mean fitted lines by band.
    grouped: dict[str, dict[float, list[float]]] = defaultdict(lambda: defaultdict(list))
    for omega, log_cost, band in points:
        grouped[band][omega].append(log_cost)
    for band, by_omega in grouped.items():
        color = COLORS.get(band, black)
        means = sorted((omega, sum(vals) / len(vals)) for omega, vals in by_omega.items())
        for (x0v, y0v), (x1v, y1v) in zip(means, means[1:]):
            x0 = scale(x0v, x_lo, x_hi, MARGIN_LEFT, WIDTH - MARGIN_RIGHT)
            y0 = scale(y0v, y_lo, y_hi, x_axis_y, MARGIN_TOP)
            x1 = scale(x1v, x_lo, x_hi, MARGIN_LEFT, WIDTH - MARGIN_RIGHT)
            y1 = scale(y1v, y_lo, y_hi, x_axis_y, MARGIN_TOP)
            draw_line(pixels, x0, y0, x1, y1, color)

    write_png(out, WIDTH, HEIGHT, pixels)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=Path("data/exp_008_7_results.csv"))
    parser.add_argument("--out-dir", type=Path, default=Path("figures"))
    args = parser.parse_args()

    rows = load_rows(args.csv)
    render(rows, "usp_ops", args.out_dir / "exp_008_7_usp_cost.png")
    render(rows, "period_ops", args.out_dir / "exp_008_7_period_cost.png")
    print(f"wrote plots to {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
