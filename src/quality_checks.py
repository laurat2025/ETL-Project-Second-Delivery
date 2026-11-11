import pandas as pd
import pandera as pa
from pandera import Column, Check

# Definir el esquema formal de validación con Pandera (cumple con tipo, nulos y rangos)
schema = pa.DataFrameSchema({
    "fecha": Column(pa.DateTime, nullable=False, required=False),
    "comuna": Column(pa.String, nullable=False, required=False),
    "numero_vehiculos": Column(pa.Float, nullable=True, checks=Check.between(0, 100), required=False),
}, strict=False) # strict=False permite que existan otras columnas del dataset real sin que falle

def validar_calidad_datos(df: pd.DataFrame, nombre_dataset: str) -> bool:
    print(f"=== Ejecutando suite de calidad formal con Pandera para: {nombre_dataset} ===")
    
    total_filas = len(df)
    print(f"-> Volumetría actual: {total_filas} filas")
    
    try:
        # Pandera valida el esquema, nulos y restricciones automáticamente
        schema.validate(df, lazy=True)
        print("-> ¡Validación de calidad APROBADA formalmente con Pandera!")
        return True
    except pa.errors.SchemaErrors as err:
        print("-> ❌ ERRORES DE CALIDAD DETECTADOS POR PANDERA:")
        print(err.failure_cases)
        return False
