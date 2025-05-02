from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import run_twitter_etl
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email': ['myemail@example.com'],  
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description="twitter etl"
)



run_etl = PythonOperator(
    task_id='run_twitter_etl',              
    python_callable=run_twitter_etl,       
    dag=dag                                
)
