# reporter.py
import csv
import json
import sqlite3
from typing import Iterable, Dict, Any
from datetime import datetime

def export_to_csv(records: Iterable[Dict[str, Any]], filename="execution_report.csv"):
    records = list(records)
    if not records:
        return
    keys = list(records[0].keys())
    # Format timestamps as ISO strings
    for r in records:
        if isinstance(r.get("timestamp"), (datetime,)):
            r["timestamp"] = r["timestamp"].isoformat()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(records)

def export_to_json(records: Iterable[Dict[str, Any]], filename="execution_report.json"):
    def default(o):
        if isinstance(o, datetime):
            return o.isoformat()
        raise TypeError

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(list(records), f, default=default, indent=2)

def export_to_sqlite(records: Iterable[Dict[str, Any]], dbfile="execution_reports.db", table="runs"):
    conn = sqlite3.connect(dbfile)
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT,
            status TEXT,
            timestamp TEXT,
            message TEXT
        )
    """)
    rows = []
    for r in records:
        ts = r["timestamp"].isoformat() if hasattr(r["timestamp"], "isoformat") else str(r["timestamp"])
        rows.append((r["test_name"], r["status"], ts, r.get("message")))
    cur.executemany(f"INSERT INTO {table} (test_name, status, timestamp, message) VALUES (?, ?, ?, ?)", rows)
    conn.commit()
    conn.close()