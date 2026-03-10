# Resultados Basados en Normativa China (GB 3095) - Beijing Air Quality

Fecha de elaboración: 2026-03-09

## 1) Base regulatoria usada

### GB 3095-2012 (Grade II, referencia histórica)

- PM2.5 anual: 35 µg/m³
- PM2.5 24h: 75 µg/m³
- PM10 anual: 70 µg/m³
- PM10 24h: 150 µg/m³

### GB 3095-2026 (nuevo estándar; implementación por fases)

Fase 1 (2026-2030, Grade II):
- PM2.5 anual: 30 µg/m³
- PM2.5 24h: 60 µg/m³
- PM10 anual: 60 µg/m³
- PM10 24h: 120 µg/m³

Fase 2 (posterior, según hoja de ruta oficial):
- PM2.5 anual: 25 µg/m³
- PM2.5 24h: 50 µg/m³

## 2) Datos analizados

- Dataset: `data/processed/beijing_unified_cleaned.csv`
- Cobertura temporal: 2013-03-01 a 2017-02-28
- Registros: 420,768 (12 estaciones)

Nota: 2013 y 2017 son años parciales; para tendencia anual se prioriza 2014-2016.

## 3) Tendencias de concentración (ciudad)

PM2.5 medio anual (µg/m³):
- 2014: 86.18
- 2015: 79.31
- 2016: 72.08

Pendiente lineal 2014-2016: **-7.05 µg/m³ por año** (mejora clara, pero aún lejos del cumplimiento).

## 4) Cumplimiento anual (estación-año, años completos 2014-2016)

Total observaciones reguladas: 36 estación-año.

- PM2.5 <= 35: 0/36 (0.00%)
- PM2.5 <= 30: 0/36 (0.00%)
- PM2.5 <= 25: 0/36 (0.00%)
- PM10 <= 70: 0/36 (0.00%)
- PM10 <= 60: 0/36 (0.00%)

Conclusión: con este histórico, ninguna estación cumple los límites anuales de referencia evaluados.

## 5) Cumplimiento diario (estación-día)

Total: 17,532 estación-día.

PM2.5 (24h):
- >75: 40.35%
- >60: 50.33%
- >50: 58.09%

PM10 (24h):
- >150: 20.72%
- >120: 32.86%

Interpretación: al endurecer el estándar (75->60->50 en PM2.5), crece de forma sustancial la tasa de incumplimiento diario.

## 6) Evolución del incumplimiento diario por año

PM2.5 >60 (fase 1 GB 3095-2026):
- 2014: 55.27%
- 2015: 47.83%
- 2016: 46.13%

PM2.5 >75 (GB 3095-2012):
- 2014: 44.77%
- 2015: 38.77%
- 2016: 36.02%

Se observa mejora entre 2014 y 2016, pero el incumplimiento sigue alto.

## 7) Hotspots territoriales (PM2.5 diario >60)

Top estaciones por frecuencia de superación:
1. Dongsi: 54.41%
2. Gucheng: 53.80%
3. Wanliu: 53.59%
4. Wanshouxigong: 53.46%
5. Guanyuan: 52.98%
6. Tiantan: 52.36%

## 8) Estacionalidad e intradía

### Estacionalidad mensual (PM2.5 medio)

Más alto: diciembre (103.68), marzo (94.59), enero (93.76), noviembre (93.32).
Más bajo: agosto (53.47).

### Patrón horario

Horas más altas: 22:00, 21:00, 23:00, 00:00, 01:00.
Horas más bajas: 07:00, 06:00, 08:00, 16:00, 15:00.

## 9) Correlaciones con PM2.5 (Pearson)

- PM10: 0.879
- CO: 0.780
- NO2: 0.664
- SO2: 0.478
- WSPM: -0.271
- O3: -0.150
- TEMP: -0.132
- DEWP: 0.113
- PRES: 0.020
- RAIN: -0.014

Lectura operativa:
- El viento (WSPM) tiene relación inversa relevante con PM2.5 (mejor dispersión).
- PM2.5 co-varía fuertemente con PM10, CO y NO2 (fuentes de combustión y mezcla urbana).

## 10) Respuestas y soluciones priorizadas (alineadas a norma)

1. Plan de reducción por fases ligado a GB 3095-2026:
   - Meta intermedia: bajar episodios >60 (PM2.5 24h) en estaciones hotspot.
   - Meta estructural: cerrar brecha anual hacia 30 µg/m³ y luego 25 µg/m³.

2. Gestión invernal reforzada (octubre-marzo):
   - Controles adicionales de combustión y calefacción en meses de mayor riesgo.

3. Gestión horaria focalizada (21:00-01:00):
   - Inspección y fiscalización en ventanas de máxima concentración.

4. Priorización territorial:
   - Empezar por Dongsi, Gucheng, Wanliu, Wanshouxigong, Guanyuan y Tiantan.

5. Política multipolutante:
   - Diseñar medidas conjuntas PM2.5-PM10-NO2-CO para evitar mejoras parciales.

6. Ahoracasting operativo:
   - Usar baseline de persistencia + meteorología para activar alertas tempranas.

7. Intervención condicionada por meteorología:
   - Activar protocolos cuando baja velocidad de viento y estabilidad atmosférica.

8. KPI regulatorio mensual:
   - % días >60 y >50 (PM2.5), % días >120 (PM10), y tendencia anual por estación.

## 11) Fuentes regulatorias

- GB 3095-2012 (MEE, versión inglesa):
  https://english.mee.gov.cn/Resources/standards/Air_Environment/quality_standard1/201605/P020160511430661307629.pdf
- Entrevista técnica oficial MEE sobre GB 3095-2026 (24-feb-2025):
  https://www.mee.gov.cn/ywdt/zbft/202502/t20250224_1100154.shtml
- Nota oficial de implementación (20-feb-2025):
  https://www.mee.gov.cn/zcwj/gwywj/202502/t20250220_1099853.shtml
