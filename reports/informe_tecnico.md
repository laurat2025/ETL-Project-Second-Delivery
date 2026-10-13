# Informe Técnico Integrado - Siniestralidad Vial en Santiago de Cali

## 1. Objetivos Refinados y Alineación ODS
* **ODS 3 (Salud y Bienestar):** Reducir globalmente las muertes y lesiones por accidentes de tráfico.
* **ODS 11 (Ciudades y Comunidades Sostenibles):** Garantizar el acceso a sistemas de transporte seguros y sostenibles.

## 2. Arquitectura de Ingesta (3 Fuentes)
1. **Fuente 1 (CSV Histórico):** Consolidado de homicidios por condición de víctima.
2. **Fuente 2 (API REST Pública):** Conexión abierta con catálogos institucionales de la Alcaldía de Cali (`datos.cali.gov.co`).
3. **Fuente 3 (CSV Masivo):** Registro analítico detallado que supera holgadamente el umbral de 10,000 registros de siniestralidad.

## 3. Modelo Relacional y Data Warehouse (SQLite)
Los datos son limpiados, unificados y migrados automáticamente hacia una base de datos relacional local (`data/processed/accidentes.sqlite`), la cual excluye archivos crudos pesados mediante `.gitignore` y sirve como única fuente de verdad para las consultas SQL y los tableros.

## 4. Validación de Calidad y Volumetría (Great Expectations)
Se integró una suite automatizada en el pipeline de Airflow que verifica obligatoriamente que el dataset procesado posea un conteo mayor a 10,000 filas y nulos controlados en llaves espaciales. Si la validación falla, la carga hacia el esquema final es bloqueada preventivamente.

## 5. Hallazgos del EDA, Asociación Estadística y Reporte Integrado
En reemplazo de gráficos aislados, se estructuró un reporte analítico consolidado que incluye pruebas formales de asociación categórica mediante la **V de Cramér**, demostrando dependencia estadística significativa entre las comunas de Cali y la severidad de los incidentes viales.
