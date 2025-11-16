import os

# ------------------ Root Path ------------------
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# ------------------ Data Paths ------------------
DATA_DIR = os.path.join(ROOT_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
CHUNK_SIZE = 50000  # can change later
FILE_EXTENSION = ".jsonl.gz"  # for auto-detection
MAX_CHUNKS = 20


def ensure_directories():
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
