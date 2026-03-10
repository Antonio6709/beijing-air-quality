from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def save_figure(name: str, reports_dir: Path, dpi: int = 150) -> Path:
    """Save current matplotlib figure under reports/ and return path."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = reports_dir / name
    plt.savefig(out_path, bbox_inches="tight", dpi=dpi)
    return out_path

