# Bank Transactions ETL Pipeline

This project demonstrates a simple local ETL pipeline using Python and Pandas.

## Steps:
1. Read raw CSV file from `data/raw/`
2. Clean the data (remove nulls, fix column names)
3. Save cleaned file to `data/processed/`

## How to Run:
```bash
pip install -r requirements.txt
python src/clean_transactions.py