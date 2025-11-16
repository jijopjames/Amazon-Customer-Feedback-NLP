# Amazon Customer Feedback NLP  
A modular, scalable NLP pipeline for analyzing Amazon product reviews using Python.

---

## 📌 Project Overview

This project aims to build an end-to-end NLP workflow capable of handling **large-scale Amazon customer feedback data**.

The system is designed to:

- Ingest large datasets using chunk-based loading  
- Preprocess text for NLP tasks  
- Build sentiment analysis models (baseline → ML → BERT)  
- Perform topic modeling 
- Support API + UI layers in future (FastAPI & Streamlit)  
- Maintain clean, production-style Python architecture

This repository currently includes the **foundation layer**: project structure, settings, utilities, and ingestion pipeline setup.

---

## 📁 Current Folder Structure

Amazon-Customer-Feedback-NLP/
│
├── app/ # (Future) FastAPI/Streamlit apps
│
├── config/
│ ├── init.py
│ ├── settings.py # Central config: RAW/PROCESSED paths, ROOT_DIR
│
├── data/
│ ├── raw/ # Raw dataset files (place downloads here)
│ ├── processed/ # Processed chunks output
│
├── models/ # (Future) Trained models: ML, BERT, vectorizers
│
├── src/
│ ├── 1_data_load/ # Data ingestion pipeline (next step)
│ │ ├── init.py
│ │ ├── (chunk_reader.py) # To be created
│ │ ├── (load_data.py) # To be created
│ │
│ ├── utils/
│ │ ├── init.py
│ │ ├── helper.py # Directory helpers, chunk saving, schema inference
│ │ ├── logger.py # (Optional) Logger - reserved for later stages
│
├── README.md
└──requirements.txt


---

## 📦 Dataset (Amazon Reviews 2023)

This project uses the **Amazon Reviews 2023** public dataset.  
The dataset contains millions of customer reviews across multiple categories such as:

- Electronics  
- Books  
- Beauty  
- Home & Kitchen  
- Toys  
- Office Products  
- and more…

Official Dataset Source:  
https://amazon-reviews-2023.github.io/

---

## 🔽 Current Dataset (Development Phase)

For now, to keep the pipeline lightweight and testable, **only the Electronics subset** is used:

`Electronics.jsonl.gz`

Format:
- JSON Lines (`.jsonl`)
- Gzip compressed (`.gz`)

This acts as your **initial ingestion and pipeline development dataset**.

---

## 📁 Future Support for Multiple Files

Later, the ingestion pipeline will support **multiple category files at once**, for example:

data/raw/
`Electronics.jsonl.gz
Books.jsonl.gz
Beauty.jsonl.gz
Home_and_Kitchen.jsonl.gz
Office_Products.jsonl.gz`

The ingestion logic (coming soon in `chunk_reader.py` and `load_data.py`) will:

- automatically detect all `.jsonl.gz` files in `data/raw/`
- load them one by one
- process and save chunks to `data/processed/`
- add a column such as `category` to distinguish datasets

This design allows the project to scale easily as more categories are added.

---