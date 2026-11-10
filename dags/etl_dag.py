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
    transformar_y_unificar_fuentes,
    validar_calidad_airflow_task,
    cargar_dw_sqlite,
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
    description='Pipeline ETL profesional con 3 fuentes, Great Expectations y SQLite',
) as dag:

    t1 = PythonOperator(task_id='extraer_fuente_1_csv_historico', python_callable=extraer_fuente_1_csv)
    t2 = PythonOperator(task_id='extraer_fuente_2_api_publica', python_callable=extraer_fuente_2_api)
    t3 = PythonOperator(task_id='extraer_fuente_3_csv_masivo', python_callable=extraer_fuente_3_csv_masivo)
    
    t_transform = PythonOperator(task_id='transformar_y_unificar_fuentes', python_callable=transformar_y_unificar_fuentes)
    t_validate = PythonOperator(task_id='validar_calidad_datos_ge', python_callable=validar_calidad_airflow_task)
    t_load = PythonOperator(task_id='cargar_dw_sqlite', python_callable=cargar_dw_sqlite)

    # Flujo secuencial atómico sin monolitos ni tareas de adorno
    [t1, t2, t3] >> t_transform >> t_validate >> t_load
