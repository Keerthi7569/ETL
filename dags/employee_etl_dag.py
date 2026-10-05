from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG("employee_etl_pipeline", start_date=datetime(2026, 1, 1), schedule="@daily", catchup=False) as dag:

    etl_pipeline = BashOperator(
        task_id="etl_pipeline",
        bash_command="cd /home/keerthinambula/automated-etl-airflow/src && /home/keerthinambula/airflow/airflow_venv/bin/python pipeline.py",
    )

    elt_transformation = BashOperator(
        task_id="elt_transformation",
        bash_command="cd /home/keerthinambula/automated-etl-airflow/src && /home/keerthinambula/airflow/airflow_venv/bin/python elt.py",
    )

    etl_pipeline >> elt_transformation
