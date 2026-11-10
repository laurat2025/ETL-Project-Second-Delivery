import great_expectations as ge
import pandas as pd

def validar_calidad_datos(df: pd.DataFrame, nombre_dataset: str) -> bool:
    """
    Suite robusta de Great Expectations evaluando 5 dimensiones de calidad de datos.
    """
    print(f"=== Ejecutando suite de calidad de 5 dimensiones para: {nombre_dataset} ===")
    gdf = ge.from_pandas(df)
    
    # 1. Dimensión Volumetría: El dataset debe superar el umbral exigido (>10,000 registros)
    res_vol = gdf.expect_table_row_count_to_be_between(min_value=10000, max_value=2000000)
    print(f"-> 1. Volumetría (>10k filas): {res_vol['success']} (Total actual: {len(df)})")
    
    # 2. Dimensión Completitud: Ausencia de nulos en columnas críticas temporales ('fecha')
    col_fecha = 'fecha' if 'fecha' in gdf.columns else gdf.columns[0]
    res_nulos_fecha = gdf.expect_column_values_to_not_be_null(col_fecha)
    print(f"-> 2. Completitud en '{col_fecha}': {res_nulos_fecha['success']}")
    
    # 3. Dimensión Integridad Espacial: Ausencia de nulos en ubicación ('comuna' o 'dirección_reporte')
    col_espacial = 'comuna' if 'comuna' in gdf.columns else ('dirección_reporte' if 'dirección_reporte' in gdf.columns else gdf.columns[1])
    res_espacial = gdf.expect_column_values_to_not_be_null(col_espacial)
    print(f"-> 3. Integridad espacial en '{col_espacial}': {res_espacial['success']}")
    
    # 4. Dimensión Validez de Rango Numérico: El número de vehículos implicados debe ser >= 0
    col_num = 'numero_vehículos' if 'numero_vehículos' in gdf.columns else None
    if col_num:
        res_rango = gdf.expect_column_values_to_be_between(col_num, min_value=0, max_value=100)
        print(f"-> 4. Validez de rango numérico en '{col_num}': {res_rango['success']}")
    else:
        res_rango = {'success': True}
        print("-> 4. Validez de rango numérico: Omitida")
        
    # 5. Dimensión Estructural: Verificar conteo de columnas válidas esperadas
    res_struct = gdf.expect_table_column_count_to_be_between(min_value=2, max_value=50)
    print(f"-> 5. Integridad estructural de columnas: {res_struct['success']}")

    exito_general = all([
        res_vol['success'], 
        res_nulos_fecha['success'], 
        res_espacial['success'], 
        res_rango['success'], 
        res_struct['success']
    ])
    
    print(f"=== RESULTADO GLOBAL GREAT EXPECTATIONS: {'APROBADO ✅' if exito_general else 'RECHAZADO ❌'} ===")
    return exito_general
