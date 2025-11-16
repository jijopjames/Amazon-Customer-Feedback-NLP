# Amazon Customer Feedback NLP  
A modular, scalable NLP pipeline for analyzing Amazon product reviews using Python.

---

## 📌 Project Overview

This repository provides the foundation for an end-to-end NLP workflow to analyze Amazon customer reviews. It focuses on a production-style, modular design so you can:

- Ingest very large datasets using chunk-based loading  
- Preprocess text for NLP tasks  
- Build sentiment analysis pipelines (baseline → ML → BERT)  
- Perform topic modeling and exploratory analysis  
- Add an API or UI (FastAPI / Streamlit) later

Current work includes project layout, configuration, utilities, and a chunked ingestion pipeline for the Amazon Reviews 2023 dataset.

---

## 📁 Current Folder Structure

```
Amazon-Customer-Feedback-NLP/
│
├── app/                             # (Future) FastAPI / Streamlit apps
│
├── config/
│   ├── __init__.py
│   └── settings.py                  # Project configuration: paths, CHUNK_SIZE, MAX_CHUNKS
│
├── data/
│   ├── raw/                         # (LOCAL ONLY) place downloads here (NOT in Git)
│   └── processed/                   # (LOCAL ONLY) ingestion output
│
├── models/                          # (Future) saved models, vectorizers
│
├── src/
│   ├── data_load/                   # Data ingestion pipeline
│   │   ├── __init__.py
│   │   ├── chunk_reader.py          # Reads .jsonl.gz in chunks
│   │   └── load_data.py             # Orchestrates ingestion and saves chunks
│   │
│   └── utils/
│       ├── __init__.py
│       ├── helper.py                # Directory helpers, save_processed_chunk, etc.
│       └── logger.py                # Optional (add later if needed)
│
├── README.md
└── requirements.txt
```

---

## 📦 Dataset (Amazon Reviews 2023)

This project uses the public **Amazon Reviews 2023** dataset.

Official source:  
https://amazon-reviews-2023.github.io/

### Current development subset

To keep development fast, the project currently uses:

```
Electronics.jsonl.gz
```

Place this file at:

```
data/raw/Electronics.jsonl.gz
```

Format:
- JSON Lines (`.jsonl`)
- gzip compressed (`.gz`)

This file acts as the starting point for ingestion.

---

## 📁 Future Support for Multiple Files

The ingestion pipeline is designed to scale and will later support multiple dataset files:

```
data/raw/
    Electronics.jsonl.gz
    Books.jsonl.gz
    Beauty.jsonl.gz
    Home_and_Kitchen.jsonl.gz
    Office_Products.jsonl.gz
```

The `data_load` module will:

- Automatically detect all `.jsonl.gz` files in `data/raw/`
- Process each file chunk-by-chunk
- Save output to `data/processed/`
- Add a `category` column based on filename  

This allows easy expansion to multi-category analysis.

---

## ⚠️ Data Storage Notice

Large datasets cannot be checked into GitHub.

GitHub limits files to **100 MB per file**, while Amazon datasets are multiple GB.

Therefore:

- `data/raw/` and `data/processed/` are **empty in GitHub**
- These folders are meant for **local use only**
- Download and store dataset files manually

```
# Data folders (local only)
data/raw/
data/processed/

---

## ⚙ Configuration (config/settings.py)

Suggested settings file:

```python
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(ROOT_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

CHUNK_SIZE = 50000          # number of rows per chunk
MAX_CHUNKS = 20             # stop after N chunks during development
FILE_EXTENSION = ".jsonl.gz"
```

Adjust these values for faster testing.

---

## 📝 Example Output

```
Files Found:
 - data/raw/Electronics.jsonl.gz

Starting ingestion...

=== Processing File: data/raw/Electronics.jsonl.gz ===
Category: Electronics
Chunk Size: 50000

Saved: data/processed/Electronics_chunk_0001.csv.gz (rows=50000)
Saved: data/processed/Electronics_chunk_0002.csv.gz (rows=50000)
...
Reached MAX_CHUNKS (20). Stopping early.

=== Ingestion Complete ===
```

---

## 🧪 Development Tips

- Use **small CHUNK_SIZE** (e.g., 1000) when debugging.
- Keep **MAX_CHUNKS low** during development (5–20).
- Optional: create a small sample dataset for fast iteration.
---

## 🧭 Next Steps

1. Build preprocessing pipeline (`clean_text.py`)  
2. Add sentiment baseline (VADER / TextBlob)  
3. Create EDA notebook  
4. Build TF-IDF + ML sentiment model  
5. Fine-tune BERT  
6. Add FastAPI + Streamlit UI  

---

## 👤 Author  
Jijo James — Data Analyst | Python | NLP  