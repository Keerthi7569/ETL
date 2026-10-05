import os
import psycopg
def load_records(records):
    conn = psycopg.connect("host=172.22.16.1 port=5432 dbname=etl_demo user=postgres", password=os.environ["PG_PASSWORD"])
    inserted = 0
    with conn.cursor() as cur:
        for r in records:
            cur.execute("INSERT INTO employees (employee_id, name, department, salary, joining_date) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (employee_id) DO NOTHING", (r["employee_id"], r["name"], r["department"], r["salary"], r["joining_date"]))
            inserted += cur.rowcount
    conn.commit()
    conn.close()
    return inserted
