import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.append('/content/Delivery_2')

from src.etl import (
    extraer_fuente_1_csv,
    extraer_fuente_2_api,
    extraer_fuente_3_csv_masivo,
    ejecutar_pipeline_etl,
)

default_args = {
    'owner': 'equipo_etl_uao',
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='pipeline_etl_cali_3_fuentes_ge',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    description='Pipeline automatizado con 3 fuentes, Great Expectations y SQLite',
) as dag:

    t1 = PythonOperator(task_id='extraer_fuente_1_csv_historico', python_callable=extraer_fuente_1_csv)
    t2 = PythonOperator(task_id='extraer_fuente_2_api_publica', python_callable=extraer_fuente_2_api)
    t3 = PythonOperator(task_id='extraer_fuente_3_csv_masivo', python_callable=extraer_fuente_3_csv_masivo)
    
    t_transform_val_load = PythonOperator(task_id='transformar_validar_y_cargar_dw', python_callable=ejecutar_pipeline_etl)

    [t1, t2, t3] >> t_transform_val_load
