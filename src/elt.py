import os
import psycopg

conn = psycopg.connect("host=172.22.16.1 port=5432 dbname=etl_demo user=postgres", password=os.environ["PG_PASSWORD"])

with conn.cursor() as cur:
    cur.execute("CREATE OR REPLACE VIEW employee_analytics AS SELECT department, COUNT(*) AS employee_count, ROUND(AVG(salary),2) AS average_salary FROM employees GROUP BY department ORDER BY department")

conn.commit()
conn.close()

print("ELT transformation completed successfully")
