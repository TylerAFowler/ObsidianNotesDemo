import os, sys, oracledb
from pathlib import Path

CHECKS = ["county_codes.sql", "route_ids.sql"]

def main():
    with oracledb.connect(dsn=os.environ["STG_DSN"]) as conn:
        for name in CHECKS:
            n = len(conn.cursor().execute((Path(__file__).parent / "validation" / name).read_text()).fetchall())
            print(f"{name:20} {n:6} failures")

if __name__ == "__main__":
    sys.exit(main())
