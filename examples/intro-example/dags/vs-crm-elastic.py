from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

#https://www.youtube.com/watch?v=IsWfoXY_Duk

args = {
    'owner': 'vincent stevenson',
    'start_date': days_ago(1) # make start date in the past
}

dag = DAG(
    dag_id='vs-crm-elastic-dag',
    default_args=args,
    schedule_interval='@daily' # make this workflow happen every day
)

def hello_world(**context):
    print('hello world!')

with dag:
    hello_world = PythonOperator(
        task_id='hello_world',
        python_callable=hello_world,
        provide_context=True
    )