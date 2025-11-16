# src/utils/helpers.py
from pathlib import Path
import pandas as pd
import time
import json
from typing import Any, Dict

# Import project paths from settings.py
from config.settings import RAW_DATA_DIR, PROCESSED_DATA_DIR


# -------------------- Directory Helpers --------------------


def ensure_dir(path: str):
    """Create directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def ensure_project_dirs():
    """Ensure raw/processed directories from settings exist."""
    ensure_dir(RAW_DATA_DIR)
    ensure_dir(PROCESSED_DATA_DIR)


# -------------------- Data Helpers --------------------


def save_processed_chunk(df: pd.DataFrame, out_dir: str, prefix: str, idx: int) -> str:
    """
    Save a processed dataframe chunk as a gzipped CSV.
    Returns the file path for logging or further processing.
    """
    ensure_dir(out_dir)
    filename = f"{prefix}_chunk_{idx:04d}.csv.gz"
    filepath = Path(out_dir) / filename
    df.to_csv(filepath, index=False, compression="gzip")
    return str(filepath)


def infer_csv_schema(path: str, nrows: int = 500) -> Dict[str, str]:
    """
    Read a small sample of a CSV file and return inferred dtypes.
    Useful for optimising large file loading.
    """
    sample = pd.read_csv(path, nrows=nrows)
    return {col: str(dtype) for col, dtype in sample.dtypes.items()}


# -------------------- Utility Helpers --------------------


def timeit(fn):
    """Decorator to measure execution time of any function."""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"[timeit] {fn.__name__} executed in {end - start:.2f}s")
        return result

    return wrapper


def write_json(data: Any, path: str):
    """Write Python object to JSON file (pretty format)."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
