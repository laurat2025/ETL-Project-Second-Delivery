# ETL-Project-Second-Delivery
# 🚦 Proyecto ETL: Segunda Entrega - Siniestralidad Vial en Santiago de Cali

Repositorio oficial para la segunda entrega del curso de **ETL (G51)** del programa de Ingeniería de Datos e Inteligencia Artificial de la **Universidad Autónoma de Occidente (UAO)**. El proyecto implementa un pipeline de datos automatizado, reproducible, validado y robusto enfocado en el análisis de accidentalidad vial y movilidad urbana en Santiago de Cali.

---

## 👥 Equipo de Trabajo
* **Laura Torres** – Arquitectura, Documentación y Coordinación
* **Juliana Serrano** – Análisis Exploratorio (EDA) y Validación Estadística
* **Juan López** – Desarrollo ETL, Orquestación y Carga en Data Warehouse

---

## 🎯 1. Requerimientos Refinados y Objetivos
El objetivo principal de este pipeline es extraer, transformar, validar y cargar datos de múltiples fuentes heterogéneas para analizar los patrones temporales, espaciales y las condiciones de las víctimas en los siniestros viales de Santiago de Cali.
* **Alineación con los ODS:**
  * **ODS 3 (Salud y Bienestar):** Meta 3.6 - Reducir globalmente las muertes y lesiones por accidentes de tráfico.
  * **ODS 11 (Ciudades y Comunidades Sostenibles):** Meta 11.2 - Proporcionar acceso a sistemas de transporte seguros y sostenibles.

---

## 📥 2. Ingesta de Datos: Arquitectura de 3 Fuentes
El pipeline implementa de forma automatizada **tres tareas distintas de extracción** en Apache Airflow, abarcando las tipologías exigidas:
1. **Fuente 1 (Archivo CSV - Primera Entrega):** Consolidado histórico de homicidios por condición de víctima (2004-2021) provisto por la Secretaría de Salud / Medicina Legal.
2. **Fuente 2 (API REST Pública):** Conexión en tiempo real con catálogos abiertos de la Alcaldía de Santiago de Cali (`datos.cali.gov.co`) sobre infraestructura y reportes viales.
3. **Fuente 3 (Archivo CSV Masivo Adicional):** Dataset detallado de incidentes viales que **supera holgadamente las 10,000 filas analíticas** (~10,500 registros), cumpliendo estrictamente con los requerimientos cuantitativos de volumetría.

---

## ⚙️ 3. Transformación de Datos
* Estandarización de nombres de columnas a minúsculas y eliminación de espacios.
* Normalización de formatos y limpieza de valores nulos o marcas institucionales.
* Enriquecimiento y cruce automatizado de las tres fuentes en un dataset unificado, consistente y listo para la validación.

---

## 🛡️ 4. Validación de Calidad y Volumetría
* Se implementó una suite de validación integrada directamente en el flujo de ejecución del pipeline.
* Valida reglas de integridad estrictas (ausencia de nulos en llaves espaciales como la comuna y verificación de que el volumétrico supere el umbral de las 10,000 filas).
* **Política de Carga:** El pipeline registra los resultados y **bloquea la carga** hacia el esquema final si los datos no cumplen con los umbrales de calidad establecidos.

---

## 🗄️ 5. Modelado y Carga de Datos (Data Warehouse)
* **Almacenamiento:** Base de datos relacional **SQLite** ubicada en `data/processed/accidentes.sqlite`.
* **Política de Versiones (.gitignore):** Los archivos de datos crudos y bases de datos locales están excluidos del control de versiones mediante `.gitignore` para optimizar espacio y mantener limpio el repositorio.
* **Modelo:** Estructurado bajo un esquema relacional con tablas staging, dimensiones normalizadas y una tabla de hechos central (`fact_siniestros`) que alimenta directamente las consultas analíticas.

---

## 📈 6. EDA Avanzado, V de Cramér y Reporte Integrado
* **Reporte Consolidado:** Se eliminaron las gráficas estáticas aisladas. Todas las visualizaciones se consolidan en un **reporte técnico integrado** dentro de la carpeta `reports/`, consumiendo exclusivamente las consultas SQL ejecutadas sobre el Data Warehouse en SQLite.
* **Prueba de Asociación Categórica (V de Cramér):** Incorpora el cálculo formal de la **V de Cramér** y pruebas de Chi-cuadrado para evaluar matemáticamente la dependencia estadística entre variables espaciales (comunas) y la gravedad de los siniestros viales.

---

## 🚀 7. Instrucciones de Instalación y Ejecución Local

### Requisitos Previos
* Python 3.11 o 3.12 instalado.
* Git para control de versiones.

### Pasos para Desplegar el Proyecto:

1. **Clonar el repositorio y abrir la terminal en la raíz:**
   ```bash
   git clone [https://github.com/juanH40-ING/Delivery_2.git](https://github.com/juanH40-ING/Delivery_2.git)
   cd Delivery_2
