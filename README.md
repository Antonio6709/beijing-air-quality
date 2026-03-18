# 🏙️ Análisis Integral de Calidad del Aire en Beijing (2013-2017)

## 📌 Contexto de Salud Pública
Beijing es históricamente una de las ciudades con peor calidad del aire a nivel mundial. El contaminante más crítico es el PM2.5 (partículas finas <2.5 µm), capaz de penetrar profundamente en el torrente sanguíneo, representando un grave riesgo para la salud pública. Según la Organización Mundial de la Salud (OMS), la contaminación atmosférica es responsable de aproximadamente 7 millones de muertes prematuras anuales a nivel global.

Este proyecto analiza las mediciones horarias de 12 estaciones de monitoreo en Beijing entre 2013 y 2017, documentando la situación previa a las grandes mejoras recientes.

## 📏 Umbrales de Referencia
El análisis evalúa el cumplimiento frente a los siguientes estándares:
* **OMS (Air Quality Guidelines 2021):** PM2.5 ≤ 15 µg/m³ (media 24h).
* **China (GB 3095-2012):** PM2.5 ≤ 35 µg/m³ (media anual).

## 🛠️ Metodología y Alertas
* **Herramientas:** Python (Pandas, Seaborn, Matplotlib) para limpieza y Análisis Exploratorio Visual (EDA), combinado con SQL (DuckDB) para la extracción eficiente de métricas.
* **Alertas Tempranas (EWMA):** Para el modelado de alertas a corto plazo, se ha optado por el Suavizado Exponencial (EWMA) frente a las medias móviles tradicionales. El EWMA otorga mayor peso a las observaciones más recientes, lo que permite que el sistema reaccione mucho más rápido ante incrementos súbitos y peligrosos de la contaminación.

---

## 📂 Estructura del Repositorio
La organización de este proyecto sigue los estándares de la industria para asegurar que sea reproducible y profesional:

### 1. data/ - El Almacén de Información
En Data Science, la integridad de los datos es sagrada. Por ello, dividimos esta carpeta:
* **raw/**: Contiene los 12 archivos CSV originales descargados de la UCI. **Nunca se modifican**.
* **processed/**: Aquí guardamos el dataset unificado y limpio tras el proceso de carga, interpolación de nulos y ajuste de formatos temporales.

### 2. notebooks/ - El Laboratorio
Es el espacio de experimentación y análisis visual:
* **EDA (Análisis Exploratorio):** Identificación de valores nulos, creación de mapas de calor y matrices de correlación para entender el comportamiento de los contaminantes.
* **Features (Ingeniería de Variables):** Creación de nuevas variables (ej. medias móviles de 24h, distinción entre fin de semana y día laborable) para enriquecer el análisis.

### 3. src/ - El Motor (Utilidades)
Para mantener los Notebooks legibles, extraemos la lógica compleja a scripts de Python (`.py`):
* Contiene funciones reutilizables de limpieza, cálculos matemáticos o generación de plots específicos.
* Permite importar herramientas directamente al Notebook: `from src.cleaning import clean_data`.

### 4. reports/ - El Escaparate
Centralizamos todas las visualizaciones finales:
* Figuras generadas (`.png`, `.jpg`) listas para ser insertadas en el informe ejecutivo o presentación final.

### 5. Documentación - El Manual de Instrucciones
* **README.md**: Portada y guía rápida del proyecto.
* **requirements.txt**: Listado de librerías necesarias para que el código funcione en cualquier ordenador.
