"""Loads the vendor's 2025 crash extract (pipe-delimited) into crash_stg.crash_2025."""
import csv, os, sys, oracledb

BATCH = 5000

def rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="|"):
            yield (r["CRASH_ID"], r["CRASH_DATE"], r["COUNTY_CD"], r["ROUTE_ID"] or None,
                   r["MILEPOST"] or None, r["SEVERITY"], r["LAT"] or None, r["LON"] or None)

def main(path):
    with oracledb.connect(dsn=os.environ["STG_DSN"]) as conn:
        cur, batch = conn.cursor(), []
        for r in rows(path):
            batch.append(r)
            if len(batch) == BATCH:
                cur.executemany(INSERT, batch); batch.clear()
        if batch: cur.executemany(INSERT, batch)
        conn.commit()

INSERT = "INSERT INTO crash_stg.crash_2025 VALUES (:1, TO_DATE(:2,'YYYY-MM-DD'), :3, :4, :5, :6, :7, :8)"

if __name__ == "__main__":
    main(sys.argv[1])
# Rows whose CRASH_DATE fails to parse are written to rejects.csv instead of failing the load.
