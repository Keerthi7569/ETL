import os
import psycopg
def audit_success(read, inserted, rejected):
    conn = psycopg.connect("host=172.22.16.1 port=5432 dbname=etl_demo user=postgres", password=os.environ["PG_PASSWORD"])
    with conn.cursor() as cur:
        cur.execute("INSERT INTO etl_audit (pipeline_name, end_time, status, record_read, record_inserted, record_rejected) VALUES (%s, CURRENT_TIMESTAMP, %s, %s, %s, %s)", ("employee_etl", "SUCCESS", read, inserted, rejected))
    conn.commit()
    conn.close()
