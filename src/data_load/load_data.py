import os
import pandas as pd

from config.settings import PROCESSED_DATA_DIR, CHUNK_SIZE, MAX_CHUNKS
from src.data_load.chunk_reader import list_raw_files, read_jsonl_gz, detect_category
from src.utils.helper import ensure_dir


def save_chunk(df: pd.DataFrame, category: str, chunk_index: int) -> str:
    """
    Saves a processed chunk as a compressed CSV file.
    """
    ensure_dir(PROCESSED_DATA_DIR)

    file_name = f"{category}_chunk_{chunk_index:04d}.csv.gz"
    file_path = os.path.join(PROCESSED_DATA_DIR, file_name)

    df.to_csv(file_path, index=False, compression="gzip")

    return file_path


def process_file(file_path: str, chunk_size: int = CHUNK_SIZE) -> None:
    """
    Reads a .jsonl.gz file in chunks and saves them.
    Stops early when MAX_CHUNKS is reached.
    """
    category = detect_category(file_path)
    print(f"\n=== Processing File: {file_path} ===")
    print(f"Category: {category}")
    print(f"Chunk Size: {chunk_size}\n")

    chunk_index = 1

    for chunk_df in read_jsonl_gz(file_path, chunk_size):
        if chunk_index > MAX_CHUNKS:
            print(f"\nReached MAX_CHUNKS ({MAX_CHUNKS}). Stopping early.\n")
            break

        chunk_df["category"] = category

        saved_path = save_chunk(chunk_df, category, chunk_index)
        print(f"Saved: {saved_path}  (rows={len(chunk_df)})")

        chunk_index += 1

    print(f"\nCompleted processing of: {category}\n")


def run_ingestion():
    """
    Orchestrates ingestion: finds raw files → processes each one.
    """
    raw_files = list_raw_files()

    if not raw_files:
        print("No raw dataset files found in data/raw/")
        return

    print("Files Found:")
    for f in raw_files:
        print(" -", f)

    print("\nStarting ingestion...\n")

    for file_path in raw_files:
        process_file(file_path)

    print("\n=== Ingestion Complete ===\n")


if __name__ == "__main__":
    run_ingestion()
