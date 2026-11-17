from flask import Flask, jsonify, request
from .db import query

app = Flask(__name__)

@app.get("/api/crashes/summary")
def summary():
    year = int(request.args.get("year", 2024))
    rows = query("summary_by_county.sql", year=year)
    return jsonify(rows)
YEARS = list(range(2019, 2026))   # 2025 added for the refresh
