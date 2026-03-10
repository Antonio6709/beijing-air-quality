# Contexto Ambiental Relevante de Beijing (para un proyecto realista)

## 1) Evolución reciente oficial en Beijing

- Según información oficial publicada el **4 de enero de 2026**, Beijing cerró **2025** con concentración media anual de PM2.5 de **30.5 µg/m³** y **290 días** con buena calidad del aire.
- Según publicación oficial del **17 de octubre de 2025** (acumulado de enero a septiembre de 2025), el PM2.5 medio fue **31.4 µg/m³** y hubo **209 días** con buena calidad del aire.

Implicación para el proyecto: los datos históricos 2013-2017 muestran una situación más severa que la realidad reciente; hay que diferenciar claramente análisis histórico vs contexto operativo actual.

## 2) Referencias sanitarias internacionales

- La OMS (AQG 2021) fija para PM2.5:
  - **5 µg/m³** (media anual)
  - **15 µg/m³** (media 24h)

Implicación: incluso con mejoras recientes, Beijing puede seguir por encima de guías sanitarias estrictas.

## 3) Marco normativo chino actualizado

- El Ministerio de Ecología y Medio Ambiente (MEE) publicó el nuevo estándar **GB 3095-2026**, aplicable desde el **1 de marzo de 2026**.
- En la entrevista técnica oficial se indica endurecimiento de límites, incluyendo PM2.5 anual de **35 a 30 µg/m³** y transición posterior a **25 µg/m³**.

Implicación: el proyecto debe reportar resultados con doble marco (histórico GB 3095-2012 y transición GB 3095-2026).

## 4) Dinámicas físicas clave para interpretar picos

- Evidencia científica reciente muestra una contribución importante del transporte regional durante episodios fríos (orden de magnitud alto en ciertos eventos).
- Estudios recientes en China muestran diferencia marcada entre temporada de calefacción y no calefacción para PM2.5 y composición química.
- La OMM reporta que las tormentas de polvo siguen siendo un riesgo relevante en Asia Oriental y aumentan episodios de partículas.

Implicación: para un proyecto municipal realista no basta con tráfico local; deben modelarse meteorología, transporte regional y estacionalidad de calefacción.

## 5) Lección estratégica de política pública

- Estudios de largo plazo en Beijing muestran fuerte reducción de PM2.5 desde 2013, pero también alertan sobre compensaciones (por ejemplo, presión creciente en ozono), por lo que se requiere enfoque multipolutante.

Implicación: el dashboard y las recomendaciones no deben optimizar solo PM2.5; deben incluir al menos O3 y NO2 para evitar transferir el problema.

---

## Fuentes

1. Beijing Municipal Ecology and Environment (publicación 4 Jan 2026):
   - https://english.beijing.gov.cn/latest/news/202601/t20260104_3980494.html
2. Beijing Municipal Ecology and Environment (publicación 17 Oct 2025):
   - https://english.beijing.gov.cn/specials/chinafivensum/content_3005146.html
3. WHO AQG 2021 (valores guía PM2.5):
   - https://www.who.int/publications/i/item/9789240034228
4. MEE China, estándar GB 3095-2012 (referencia histórica):
   - https://english.mee.gov.cn/Resources/standards/Air_Environment/quality_standard1/201605/P020160511430661307629.pdf
5. MEE China, actualización GB 3095-2026 (entrevista técnica):
   - https://www.mee.gov.cn/ywdt/zbft/202502/t20250224_1100154.shtml
6. Transporte regional en Beijing (PubMed, 2024):
   - https://pubmed.ncbi.nlm.nih.gov/39352977/
7. Temporada de calefacción y PM2.5 (PubMed, 2025):
   - https://pubmed.ncbi.nlm.nih.gov/40246475/
8. OMM sobre tormentas de polvo en Asia Oriental:
   - https://wmo.int/media/news/east-asia-and-pacific-experience-unprecedented-hazardous-weather-2023
9. Tendencias multipolutante en Beijing (ACP, 2022):
   - https://acp.copernicus.org/articles/22/11967/2022/
