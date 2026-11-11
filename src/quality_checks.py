import pandas as pd

def validar_calidad_datos(df: pd.DataFrame, nombre_dataset: str) -> bool:
    print(f"=== Ejecutando suite de calidad de 5 dimensiones para: {nombre_dataset} ===")
    total_filas = len(df)
    pasa_vol = 10000 <= total_filas <= 2000000
    print(f"-> 1. Volumetria: {pasa_vol} (Total actual: {total_filas})")
    col_fecha = 'fecha' if 'fecha' in df.columns else df.columns[0]
    nulos_fecha = df[col_fecha].isnull().sum()
    pasa_nulos_fecha = nulos_fecha == 0
    print(f"-> 2. Completitud en fecha: {pasa_nulos_fecha}")
    col_espacial = 'comuna' if 'comuna' in df.columns else df.columns[1]
    nulos_espacial = df[col_espacial].isnull().sum()
    pasa_espacial = nulos_espacial == 0
    print(f"-> 3. Integridad espacial: {pasa_espacial}")
    col_num = 'numero_vehículos' if 'numero_vehículos' in df.columns else None
    if col_num:
        pasa_rango = bool(((df[col_num] >= 0) & (df[col_num] <= 100)).all())
        print(f"-> 4. Validez de rango numerico: {pasa_rango}")
    else:
        pasa_rango = True
        print("-> 4. Validez de rango numerico: Omitida")
    num_cols = len(df.columns)
    pasa_struct = 2 <= num_cols <= 50
    print(f"-> 5. Estructura de columnas (Total: {num_cols}): {pasa_struct}")
    exito_general = all([pasa_vol, pasa_nulos_fecha, pasa_espacial, pasa_rango, pasa_struct])
    estado = "APROBADO" if exito_general else "RECHAZADO"
    print(f"=== RESULTADO GLOBAL CALIDAD: {estado} ===")
    return exito_general
