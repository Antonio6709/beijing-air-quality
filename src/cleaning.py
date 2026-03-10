from __future__ import annotations

from typing import Iterable

import pandas as pd

NUMERIC_COLS = [
    "PM2.5",
    "PM10",
    "SO2",
    "NO2",
    "CO",
    "O3",
    "TEMP",
    "PRES",
    "DEWP",
    "RAIN",
    "WSPM",
]


def build_datetime_index(df: pd.DataFrame) -> pd.DataFrame:
    """Create datetime index from year/month/day/hour and drop redundant columns."""
    out = df.copy()
    out["date"] = pd.to_datetime(out[["year", "month", "day", "hour"]])
    out = out.set_index("date").drop(columns=["No", "year", "month", "day", "hour"], errors="ignore")
    return out


def interpolate_missing_by_station(
    df: pd.DataFrame,
    numeric_cols: Iterable[str] = NUMERIC_COLS,
) -> pd.DataFrame:
    """Interpolate numeric gaps independently per station to avoid cross-station leakage."""
    out = df.copy()
    cols = list(numeric_cols)
    idx_name = out.index.name or "date"
    out = out.reset_index().rename(columns={idx_name: "date"})
    out = out.sort_values(["station", "date"])
    out[cols] = (
        out.groupby("station", group_keys=False)[cols]
        .apply(lambda s: s.interpolate(method="linear", limit_direction="both"))
    )
    out["wd"] = out.groupby("station")["wd"].ffill().bfill()
    return out.set_index("date")


def winsorize_iqr(
    df: pd.DataFrame,
    cols: Iterable[str] = ("PM2.5", "PM10", "SO2", "NO2", "CO", "O3"),
    k: float = 1.5,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Cap extremes using IQR bounds; returns cleaned dataframe and bounds table."""
    out = df.copy()
    bounds = []
    for col in cols:
        q1 = out[col].quantile(0.25)
        q3 = out[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - k * iqr
        upper = q3 + k * iqr
        out[col] = out[col].clip(lower=lower, upper=upper)
        bounds.append({"variable": col, "q1": q1, "q3": q3, "lower": lower, "upper": upper})
    return out, pd.DataFrame(bounds)
