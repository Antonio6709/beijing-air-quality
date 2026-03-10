# Resumen Ejecutivo - Calidad del Aire en Beijing

## 1) Objetivo y enfoque

Se integró análisis en **Python** (limpieza, visualización, baseline predictivo) y **SQL (DuckDB)** para obtener hallazgos accionables y trazables para gestión municipal.

- Datos analizados: PRSA multiestación (12 estaciones, 2013-03-01 a 2017-02-28).
- Registros: 420,768 observaciones horarias.
- Flujo: limpieza reproducible -> EDA temporal -> consultas SQL -> recomendaciones.

## 2) Hallazgos principales (SQL + Python)

### Calidad global

- PM2.5 medio histórico del dataset: **79.84 µg/m³**.
- Horas con PM2.5 > 35 µg/m³: **62.70%**.
- Horas con PM2.5 > 75 µg/m³: **39.07%**.

### Hotspots espaciales

Top estaciones por PM2.5 medio:

1. Dongsi (86.14)
2. Nongzhanguan (85.08)
3. Wanshouxigong (85.07)
4. Gucheng (84.07)

Observación: zonas urbanas/mixtas concentran mayor carga media que estaciones periféricas (p. ej. Dingling, Huairou).

### Estacionalidad

- Meses más cargados: **diciembre (103.68)**, **marzo (94.59)**, **enero (93.76)**, **noviembre (93.32)**.
- Mes más bajo: **agosto (53.47)**.

Interpretación: patrón compatible con calefacción estacional, condiciones de dispersión adversas en invierno y episodios de transición primaveral.

### Patrón intradía y semanal

- Máximos horarios típicos: franja nocturna (**21:00-00:00**).
- Mínimos relativos: mañana-media tarde.
- Promedio por día: **sábado > viernes > domingo** y **lunes** el más bajo en este histórico.

Interpretación: señal compatible con mezcla de actividad urbana, meteorología y acumulación regional.

### Suavizado operativo

- Se comparó media móvil 24h vs EWMA 24h.
- Recomendación técnica: usar EWMA para monitoreo operativo por mejor sensibilidad a cambios recientes.
- Recomendación de rigor: en entrega final reportar métrica de desfase (lag) y error para justificar formalmente la elección.

### Baseline de ahoracasting

- Se implementó baseline de persistencia (`PM2.5_t ≈ PM2.5_t-1`) como línea base de referencia para modelos posteriores.

## 3) Contexto realista (situación reciente y normativa)

- Beijing reportó para **2025** PM2.5 medio anual de **30.5 µg/m³** y **290 días** de buena calidad del aire (publicación oficial 4 de enero de 2026).
- El estándar chino se endurece con **GB 3095-2026** (vigente desde 1 de marzo de 2026), incluyendo ajuste del límite anual de PM2.5.
- La guía OMS sigue siendo más exigente (5 µg/m³ anual y 15 µg/m³ en 24h).

Conclusión de política: hay mejora estructural, pero persiste brecha relevante frente a objetivos sanitarios estrictos; la gestión debe ser multipolutante y coordinada regionalmente.

## 4) Decisiones metodológicas documentadas

- Interpolación de faltantes por estación (evita fuga entre sensores).
- Relleno de `wd` por estación con `ffill/bfill`.
- Tratamiento de outliers en contaminantes por capping IQR.
- Visualizaciones temporales con línea, heatmap y banda de confianza (IQR diario).

## 5) Riesgos y siguientes pasos

- Riesgo 1: extrapolar decisiones actuales solo con serie 2013-2017.
- Riesgo 2: optimizar PM2.5 sin vigilar O3.
- Riesgo 3: no incorporar meteorología/transporte regional en alertas.

Siguiente fase sugerida:

1. Añadir variables meteorológicas externas (viento regional, capa límite, polvo).
2. Construir nowcasting de 1-6h con evaluación formal (MAE/RMSE/recall episodios).
3. Operar tablero con umbrales duales (normativa local + salud pública).

## 6) Referencias

Ver `reports/contexto_ambiental_beijing.md`.
