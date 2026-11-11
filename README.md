# ETL-Project-Second-Delivery
## Siniestralidad Vial y Movilidad Urbana en Santiago de Cali

Repositorio oficial para la segunda entrega del curso de ETL (G51) del programa de **Ingeniería de Datos e Inteligencia Artificial** de la **Universidad Autónoma de Occidente (UAO)**. El proyecto implementa un pipeline de datos automatizado, reproducible, validado y robusto enfocado en el análisis de accidentalidad vial y movilidad urbana en Santiago de Cali.

## Equipo de Trabajo
* Laura Torres
* Juliana Toro Serrano
* Juan López
* Juan Carlos Hernandez

## 1. Requerimientos Refinados y Objetivos Analíticos
El objetivo principal de este pipeline es extraer, transformar, validar rigurosamente y cargar datos de múltiples fuentes heterogéneas para analizar los patrones temporales, espaciales y las condiciones de las víctimas en los siniestros viales de Santiago de Cali.

* **Alineación con los Objetivos de Desarrollo Sostenible (ODS):**
  * **ODS 3 (Salud y Bienestar):** Meta 3.6 - Reducir globalmente las muertes y lesiones por accidentes de tráfico mediante el análisis de zonas críticas y condiciones de riesgo.
  * **ODS 11 (Ciudades y Comunidades Sostenibles):** Meta 11.2 - Proporcionar acceso a sistemas de transporte seguros, accesibles y sostenibles a través de la explotación inteligente de datos públicos de movilidad.

## 2. Ingesta de Datos: Arquitectura de 3 Fuentes
El pipeline implementa de forma automatizada tareas independientes y atómicas orquestadas en **Apache Airflow** (eliminando monolitos y tareas de adorno), abarcando las siguientes tipologías exigidas:

1. **Fuente 1 (Archivo CSV - Primera Entrega):** Consolidado histórico de homicidios por condición de víctima (2004-2021) provisto por registros institucionales previos.
2. **Fuente 2 (API REST Pública):** Conexión automatizada en tiempo real con los catálogos de datos abiertos de la Alcaldía de Santiago de Cali (`datos.cali.gov.co`) sobre infraestructura y reportes viales.
3. **Fuente 3 (Archivo CSV Masivo Adicional):** Dataset detallado de siniestralidad masiva (`siniestralidad_2016_2024.csv`) que supera holgadamente el umbral analítico exigido, procesando más de **370,000 registros** reales.

## 3. Transformación y Limpieza de Datos
* **Normalización Estructural:** Estandarización sistemática de nombres de columnas a minúsculas, eliminación de espacios en blanco y sustitución de caracteres especiales.
* **Tratamiento Riguroso de Nulos:** Conversión robusta de formatos de fecha mediante `pd.to_datetime` (imputando valores por defecto seguros ante registros corruptos) y manejo de espacialidad asignando etiquetas claras como *"No Registrada"* en comunas o barrios faltantes.
* **Persistencia Intermedia Eficiente:** Uso estratégico de archivos en formato **Parquet** (`data/processed/`) para almacenar las etapas intermedias (fuentes extraídas y dataset unificado), optimizando el rendimiento de lectura y escritura.

## 4. Validación de Calidad y Volumetría (Pandera)
* **Suite Automatizada:** Se implementó una capa de validación integrada directamente en el flujo de ejecución de Airflow utilizando la librería **Pandera** para garantizar la conformidad de los esquemas de datos.
* **Evaluación de 5 Dimensiones Críticas:**
  1. *Volumetría:* Verificación de que el conteo total de filas se encuentre dentro de los rangos esperados.
  2. *Completitud de Fechas:* Comprobación de ausencia de nulos críticos en el campo temporal.
  3. *Integridad Espacial:* Validación de consistencia en las variables de ubicación geográfica (comunas/barrios).
  4. *Validez de Rangos Numéricos:* Control de límites lógicos en variables cuantitativas (ej. conteo de vehículos).
  5. *Estructura de Columnas:* Control estricto de tipos de datos y presencia de esquemas tabulares válidos.
* **Política de Carga Segura:** Si el dataset no supera las reglas de calidad establecidas, el pipeline se interrumpe y lanza un error crítico, evitando contaminar el Data Warehouse con datos corruptos.

## 5. Modelado y Carga de Datos: Arquitectura de Data Warehouse
* **Motor de Almacenamiento:** Base de datos relacional SQLite alojada en `data/processed/accidentes.sqlite`.
* **Diseño del Esquema (Estrella):** El almacenamiento final adopta un modelo relacional normalizado:
  * **`fact_siniestros` (Tabla de Hechos):** Centraliza los eventos granulares de accidentalidad procesados desde el dataset masivo unificado.
  * **`dim_victimas` (Tabla de Dimensión):** Almacena el contexto histórico de las condiciones de las víctimas (derivado de la Fuente 1).
  * **`dim_movilidad` (Tabla de Dimensión):** Contiene los metadatos de infraestructura y reportes institucionales (derivado de la Fuente 2).
* **Control de Versiones (`.gitignore`):** Los archivos de datos crudos en `data/raw/` y los binarios pesados del Data Warehouse están excluidos del control de versiones de Git para garantizar un repositorio ligero y limpio.

## 6. EDA Avanzado, V de Cramér y Reporte Integrado
* **Reporte Técnico Consolidado:** Las visualizaciones analíticas se agrupan en la carpeta `reports/`, alimentándose exclusivamente de consultas SQL ejecutadas directamente sobre el Data Warehouse en SQLite.
* **Prueba de Asociación Categórica (V de Cramér):** Incorpora el cálculo estadístico formal de la V de Cramér y pruebas de Chi-cuadrado para determinar con rigor matemático la dependencia entre las variables espaciales (comunas) y la severidad de los siniestros viales, utilizando transparentemente los datos reales del proyecto sin simulaciones artificiales.

## 7. Instrucciones de Instalación y Ejecución Local

### Requisitos Previos
* Python 3.11 o superior instalado en el sistema.
* Git configurado.

### Pasos para Desplegar el Proyecto:
1. Clonar el repositorio y acceder a la carpeta raíz desde la terminal:
   ```bash
   git clone [https://github.com/laurat2025/ETL-Project-Second-Delivery.git](https://github.com/laurat2025/ETL-Project-Second-Delivery.git)
   cd ETL-Project-Second-Delivery
