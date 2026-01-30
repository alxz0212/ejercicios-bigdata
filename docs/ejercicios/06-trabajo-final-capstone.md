# Proyecto Final: Análisis de Desarrollo Global

Este es el proyecto integrador del curso. Requiere la aplicación de todas las competencias adquiridas: Ingeniería de Datos, Estadística y Machine Learning.

## Escenario
Actuarás como Consultor de Datos para un organismo internacional. Tu objetivo es auditar y clasificar el desempeño de 190 países basándote en la evidencia empírica del dataset *Quality of Government*.

## Arquitectura Técnica
El pipeline debe implementarse utilizando la infraestructura Docker del curso:

1. **Ingesta:** Carga eficiente de datos con Dask.
2. **Persistencia:** Almacenamiento en PostgreSQL (Data Warehouse).
3. **Modelado:** Clustering de países con Scikit-Learn.
4. **Reporte:** Generación de visualizaciones automáticas.

## Requisitos de Entrega
El trabajo debe entregarse en la carpeta `entregas/trabajo_final/` siguiendo esta estructura modular:

- `main.py`: Orquestador principal.
- `etl.py`: Lógica de extracción y carga.
- `c_analysis.py`: Lógica de clustering y visualización.
- `requirements.txt`: Dependencias.

Consulta la [Guía de Infraestructura](../infraestructura.md) para configurar tu entorno de base de datos antes de empezar.
