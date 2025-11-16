import os
import gzip
import json
import pandas as pd
from typing import Iterator, List

from config.settings import RAW_DATA_DIR, CHUNK_SIZE, FILE_EXTENSION


def list_raw_files(extension: str = None) -> List[str]:
    """
    Gives a list of all raw dataset files in data/raw folder with matching extension.

    Args:
        extension (str): file extension as per FILE_EXTENSION declared in 'settings.py'

    Returns:
        List[str]: list of files that end with .jsonl.gz
    """
    extension = extension or FILE_EXTENSION

    return [
        os.path.join(RAW_DATA_DIR, f)
        for f in os.listdir(RAW_DATA_DIR)
        if f.endswith(extension)
    ]


def read_jsonl_gz(file_path: str, chunk_size: int = None) -> Iterator[pd.DataFrame]:
    """
    Reads a .jsonl.gz file and yields DataFrame chunks.

    Args:
        file_path (str): path of .jsonl.gz file
        chunk_size (int): number of rows per chunk

    Yields:
        pd.DataFrame: dataframe containing chunk_size rows or fewer
    """
    chunk_size = chunk_size or CHUNK_SIZE
    rows = []

    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue

            if len(rows) >= chunk_size:
                yield pd.DataFrame(rows)
                rows = []

    # yield last chunk
    if rows:
        yield pd.DataFrame(rows)


def detect_category(file_path: str) -> str:
    """
    Extracts the category name from a filename such as 'Electronics.jsonl.gz' → Electronics.

    Args:
        file_path (str): path to a .jsonl.gz file.

    Returns:
        str: category name
    """
    base = os.path.basename(file_path)
    return base.split(".")[0]
