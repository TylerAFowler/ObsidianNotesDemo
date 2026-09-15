import os, oracledb
from pathlib import Path

SQL = Path(__file__).parent / "sql"

def query(name, **params):
    with oracledb.connect(dsn=os.environ["CRASH_DSN"]) as conn:
        cur = conn.cursor()
        cur.execute((SQL / name).read_text(), params)
        cols = [c[0].lower() for c in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]
