from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"


def list_raw_files(pattern: str = "PRSA_Data_*.csv") -> list[Path]:
    """Return sorted raw dataset files."""
    return sorted(RAW_DIR.glob(pattern))


def load_raw_files(files: Iterable[Path] | None = None) -> pd.DataFrame:
    """Load and concatenate all raw station files."""
    selected = list(files) if files is not None else list_raw_files()
    frames = [pd.read_csv(path) for path in selected]
    if not frames:
        raise FileNotFoundError("No raw files were found under data/raw.")
    return pd.concat(frames, ignore_index=True)


def load_processed(filename: str = "beijing_unified_cleaned.csv") -> pd.DataFrame:
    """Load the processed unified dataset with parsed datetime index."""
    path = PROCESSED_DIR / filename
    return pd.read_csv(path, index_col="date", parse_dates=True)


def save_processed(df: pd.DataFrame, filename: str = "beijing_unified_cleaned.csv") -> Path:
    """Save processed dataset and return output path."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PROCESSED_DIR / filename
    df.to_csv(out_path)
    return out_path

