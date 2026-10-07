import csv, io
from .db import query

def county_csv(year):
    buf = io.StringIO()
    rows = query("summary_by_county.sql", year=year)
    w = csv.DictWriter(buf, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    return buf.getvalue()
# TODO: wire to /api/crashes/export once the dashboard refresh decides on formats
