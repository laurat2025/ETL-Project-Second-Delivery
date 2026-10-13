import pandas as pd

def validar_calidad_datos(df: pd.DataFrame, nombre_dataset: str) -> bool:
    print(f"Ejecutando suite de calidad para: {nombre_dataset}")
    total_filas = len(df)
    pasa_volumen = total_filas >= 10000
    print(f"-> Validación de volumetría (>10k filas): {pasa_volumen} (Total actual: {total_filas} filas)")
    
    pasa_nulos = True
    if 'comuna' in df.columns:
        nulos_comuna = df['comuna'].isnull().sum()
        pasa_nulos = nulos_comuna == 0
        print(f"-> Validación nulos en 'comuna': {pasa_nulos} (Nulos encontrados: {nulos_comuna})")
        
    exito_general = pasa_volumen and pasa_nulos
    print(f"=== RESULTADO VALIDACIÓN [{nombre_dataset}]: {'APROBADO ✅' if exito_general else 'RECHAZADO ❌'} ===")
    return exito_general
