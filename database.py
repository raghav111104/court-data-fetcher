import sqlite3
from datetime import datetime

DB_NAME = "case_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            timestamp TEXT,
            raw_html TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, raw_html):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO queries (case_type, case_number, filing_year, timestamp, raw_html)
        VALUES (?, ?, ?, ?, ?)
    """, (case_type, case_number, filing_year, timestamp, raw_html))
    conn.commit()
    conn.close()
