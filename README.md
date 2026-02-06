Readme editor ==> https://stackedit.io/app#

GitHub:

Al empezar el día	git fetch/pull (Para bajar lo que hicieron otros).

Al terminar una tarea	git add . sube todo, git add archivoX sube un archivo en concreto, git commit -m 'limpieza datos' (Para guardar tu "foto" local).

Para que otros lo vean	git push (Para subirlo a la nube).



\# Proyecto: Calidad del Aire en Beijing 🇨🇳

\*\*Analistas de Datos:\*\* \[Nombres de los integrantes]



Este repositorio contiene el análisis técnico y las recomendaciones estratégicas para el Ayuntamiento de Beijing sobre la gestión de la contaminación ambiental.



---



\## 📂 Estructura del Repositorio



La organización de este proyecto sigue los estándares de la industria para asegurar que sea reproducible y profesional:



\### 1. `data/` - El Almacén de Información

En Data Science, la integridad de los datos es sagrada. Por ello, dividimos esta carpeta:

\* \*\*`raw/`\*\*: Contiene los 12 archivos CSV originales descargados de la UCI. \*\*Nunca se modifican\*\*.

\* \*\*`processed/`\*\*: Aquí guardamos el dataset unificado y limpio tras el proceso de carga, interpolación de nulos y ajuste de formatos temporales.



\### 2. `notebooks/` - El Laboratorio

Es el espacio de experimentación y análisis visual:

\* \*\*EDA (Análisis Exploratorio):\*\* Identificación de valores nulos, creación de mapas de calor y matrices de correlación para entender el comportamiento de los contaminantes.

\* \*\*Features (Ingeniería de Variables):\*\* Creación de nuevas variables (ej. medias móviles de 24h, distinción entre fin de semana y día laborable) para enriquecer el análisis.



\### 3. `src/` - El Motor (Utilidades)

Para mantener los Notebooks legibles, extraemos la lógica compleja a scripts de Python (`.py`):

\* Contiene funciones reutilizables de limpieza, cálculos matemáticos o generación de plots específicos.

\* Permite importar herramientas directamente al Notebook: `from src.limpieza import limpiar\_datos`.



\### 4. `reports/` - El Escaparate

Centralizamos todas las visualizaciones finales:

\* Figuras generadas (`.png`, `.jpg`) listas para ser insertadas en el informe ejecutivo o presentación final.



\### 5. `Documentación` - El Manual de Instrucciones

\* \*\*`README.md`\*\*: Portada y guía rápida del proyecto.

\* \*\*`requirements.txt`\*\*: Listado de librerías necesarias para que el código funcione en cualquier ordenador.

