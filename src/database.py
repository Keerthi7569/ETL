import os
import psycopg
conn = psycopg.connect("host=172.22.16.1 port=5432 dbname=etl_demo user=postgres",password=os.environ["PG_PASSWORD"])
print("Database connection successful")
