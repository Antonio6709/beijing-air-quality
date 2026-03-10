# Beijing Air Quality

Proyecto de análisis de calidad del aire en Beijing con flujo reproducible en Python + SQL (DuckDB).

## Objetivo
Analizar patrones espacio-temporales de contaminantes (en especial PM2.5), generar visualizaciones para comunicación pública y proponer recomendaciones accionables para el Ayuntamiento.

## Estructura del repositorio

```text
beijing-air-quality/
├─ data/
│  ├─ raw/
│  └─ processed/
├─ notebooks/
│  ├─ 00_guia_navegacion.ipynb
│  ├─ 01_limpieza_y_unificacion.ipynb
│  ├─ 02_eda_y_visualizacion.ipynb
│  ├─ 03_sql_y_resumen_ejecutivo.ipynb
│  └─ 04_impacto_normativo_y_riesgos.ipynb
├─ src/
│  ├─ __init__.py
│  ├─ io_utils.py
│  ├─ cleaning.py
│  └─ plots.py
├─ reports/
│  ├─ *.png
│  ├─ resumen_ejecutivo.md
│  ├─ contexto_ambiental_beijing.md
│  └─ decalogo_recomendaciones.md
├─ README.md
└─ requirements.txt
```

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

1. Abrir Jupyter (`jupyter lab` o `jupyter notebook`).
2. Ejecutar en este orden:
   - `notebooks/00_guia_navegacion.ipynb`
   - `notebooks/01_limpieza_y_unificacion.ipynb`
   - `notebooks/02_eda_y_visualizacion.ipynb`
   - `notebooks/03_sql_y_resumen_ejecutivo.ipynb`
   - `notebooks/04_impacto_normativo_y_riesgos.ipynb`
3. Verificar que se generan/actualizan figuras en `reports/`.

## Resumen técnico del dataset

- Fuente: UCI Beijing Multi-Site Air-Quality Data.
- Cobertura temporal: **2013-03-01 00:00:00 a 2017-02-28 23:00:00**.
- Estaciones: **12**.
- Registros totales: **420,768**.
- Métricas rápidas (PM2.5, serie procesada actual):
  - Media global: **79.84 µg/m³**.
  - Horas > 35 µg/m³: **62.70%**.
  - Horas > 75 µg/m³: **39.07%**.

## Entregables incluidos

- Notebooks ejecutables de limpieza, EDA y SQL.
- Comparativa de suavizado (`rolling` vs `EWMA`).
- Análisis horario, semanal y estacional.
- Heatmap hora x día y banda de variabilidad (IQR).
- Resumen ejecutivo (`reports/resumen_ejecutivo.md`).
- Decálogo para Ayuntamiento (`reports/decalogo_recomendaciones.md`).
- Contexto ambiental realista actualizado (`reports/contexto_ambiental_beijing.md`).
- Resultados regulatorios frente a GB 3095 (`reports/resultados_normativa_china.md`).

## Nota metodológica

Los datos del proyecto cubren 2013-2017; para decisiones de política actual se deben contrastar con series recientes oficiales (incluidas en `reports/contexto_ambiental_beijing.md`).
