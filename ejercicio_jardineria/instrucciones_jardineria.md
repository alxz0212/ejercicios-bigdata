# 🌿 Proyecto de Gestión de Jardinería: Guía Paso a Paso

Este documento detalla el flujo de trabajo completo realizado para construir el sistema de gestión de datos para la empresa de jardinería.

---

## 🛠️ Tecnologías y Librerías Utilizadas

Para el desarrollo de este proyecto, se emplearon las siguientes herramientas del ecosistema Python:

*   **🐍 Python 3.x:** Lenguaje base del proyecto.
*   **🗄️ SQLite3:** Motor de base de datos relacional (incluido en Python) para el almacenamiento persistente y portable de la información.
*   **🐼 Pandas:** Utilizada para la manipulación de datos, lectura de consultas SQL y generación de DataFrames para el análisis.
*   **🎭 Faker:** Librería clave para la generación de datos sintéticos realistas (nombres, direcciones, fechas, etc.) en español.
*   **📊 Streamlit:** Framework para la creación rápida de la aplicación web interactiva (Dashboard).
*   **📈 Plotly Express / Graph Objects:** Librería de visualización para crear gráficos interactivos, mapas y diagramas avanzados.
*   **pathlib & os:** Módulos estándar para el manejo robusto de rutas de archivos, asegurando que el proyecto funcione en cualquier sistema operativo.

---

## 1. Diseño y Creación de la Base de Datos

El primer paso fue diseñar un modelo relacional robusto y poblarlo con datos para poder trabajar.

*   **Script:** `crear_bd_jardineria.py`
*   **Proceso:**
    1.  Se definieron 8 tablas interconectadas (`oficina`, `empleado`, `cliente`, `pedido`, etc.) respetando claves primarias y foráneas.
    2.  Se utilizó la librería `Faker` para generar datos sintéticos realistas.
    3.  Se insertaron automáticamente 20 registros de prueba en cada tabla para simular un entorno operativo.

## 2. Validación y Consultas SQL

Una vez creada la base de datos, verificamos su integridad y practicamos la extracción de información.

*   **Script:** `consultas_jardineria.py`
*   **Objetivo:** Resolver preguntas de negocio mediante SQL.
*   **Consultas Clave Realizadas:**
    *   Listado de clientes por ciudad.
    *   Detección de pedidos rechazados.
    *   Cálculo de los mejores clientes (Top Pagadores).
    *   Identificación de productos más caros por gama.
    *   Auditoría de empleados sin clientes asignados (`LEFT JOIN`).
    *   Generación de facturas detalladas con subtotales.

## 3. Análisis Exploratorio Automático (EDA)

Realizamos una "radiografía" técnica de los datos para entender su calidad y estructura mediante un script automatizado.

*   **Script:** `eda_exploratorio_jardineria.py`
*   **Salida:** `resumen_jardineria_eda.md`
*   **Hallazgos:**
    *   Conteo de filas y columnas por tabla.
    *   Detección de valores nulos y duplicados.
    *   Validación de tipos de datos.

## 4. Documentación y Modelado de Datos (Diagramas)

Basándonos en el EDA, elaboramos un documento de análisis profundo para documentar la lógica del negocio.

*   **Documento:** `Analisis_datos_jardineria.md`
*   **Contenido Clave:**
    *   **Diagramas Entidad-Relación (ER):** Se crearon 4 diagramas utilizando **Mermaid** para visualizar:
        1.  Visión Global del sistema.
        2.  Flujo de Ventas.
        3.  Estructura de RRHH.
        4.  Catálogo de Productos.
    *   **Justificación del Diseño:** Explicación de por qué el modelo relacional (1:N) es superior a una tabla plana para evitar redundancia.

## 5. Visualización Interactiva (Dashboard)

Finalmente, construimos una herramienta de gestión visual para la toma de decisiones.

*   **Script:** `dashboard_jardineria.py`
*   **Características del Dashboard:**
    *   **Navegación Multi-página:** Visión General, Ventas, Mapa y RRHH.
    *   **Mapa Interactivo:** Visualización geográfica de la cartera de clientes.
    *   **KPIs en Tiempo Real:** Métricas de ingresos, pedidos y stock.
    *   **Gráficos Avanzados:** Sunburst para distribución de personal y gráficos de barras para análisis de ventas.

### 📸 Captura del Dashboard

> **[INSERTA AQUÍ TU CAPTURA DE PANTALLA DEL DASHBOARD]**

---

## 🚀 Cómo Reproducir este Proyecto

Si deseas ejecutar este proyecto en tu máquina local, sigue estos comandos en orden:

1.  **Instalar dependencias:**
    ```bash
    pip install pandas streamlit plotly faker
    ```

2.  **Generar la base de datos (ETL):**
    ```bash
    python ejercicio_jardineria/crear_bd_jardineria.py
    ```

3.  **Ejecutar el Dashboard:**
    ```bash
    streamlit run ejercicio_jardineria/dashboard_jardineria.py
    ```

---
*Documentación generada por Alexis Mendoza Corne - 2025*
