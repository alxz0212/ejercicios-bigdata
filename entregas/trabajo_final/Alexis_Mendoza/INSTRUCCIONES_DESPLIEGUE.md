# GUÍA RÁPIDA DE DESPLIEGUE DESDE CERO (CHEAT SHEET)
**Proyecto:** Big Data & "Gran Juego" (Pipeline + ML + Dashboard)

---

## **PRERREQUISITOS**
1. Tener **Docker Desktop** instalado y corriendo.
2. Tener el código fuente descargado.
3. Abrir una terminal (PowerShell o CMD) y navegar a la carpeta del proyecto:
   ```powershell
   cd entregas/trabajo_final/Alexis_Mendoza
   ```
   > **IMPORTANTE:** Todos los comandos deben ejecutarse desde esta carpeta.

---

## **PASO 0: LEVANTAR LA INFRAESTRUCTURA** 🏗️
Enciende los servidores (Jupyter, Spark Master/Worker, Postgres). El flag `-d` lo hace en segundo plano.

**Comando:**
```bash
docker-compose up -d --build
```

Espera a que se construya la imagen y arranque todo.
> **NOTA:** La primera vez puede tardar entre 5 y 10 minutos (descarga de imágenes). Las siguientes veces será casi instantáneo.
>
> *Docker debe estar abierto antes de ejecutar cualquier comando*

---

## **PASO 1: PREPARACIÓN DE DATOS (IMPORTANTE)** 📥
Antes de iniciar, necesitas el dataset "Quality of Government" (Time-Series).
1. Crea la carpeta donde irán los datos raw.
2. Coloca el archivo `qog_std_ts_jan26.csv` dentro.

**Comando (PowerShell):**
```bash
docker exec jupyter_lab python /home/jovyan/work/src/download_data.py
```

---

## **PASO 2: INSTALAR DEPENDENCIAS (Automático)** 📦
Las dependencias (Streamlit, PySpark, etc.) ahora se instalan automáticamente al levantar el contenedor gracias al Dockerfile y `requirements.txt`.
**¡Ya no necesitas ejecutar nada aquí!**

---

## **PASO 3: EJECUTAR EL PIPELINE DE DATOS (ETL)** ⚙️
Procesa el CSV crudo y genera el archivo Parquet limpio.

**Comando:**
```bash
docker exec jupyter_lab python /home/jovyan/work/src/pipeline.py
```
Deberías ver "Proceso ETL completado con éxito".

---

## **PASO 4: ENTRENAR MODELO Y GENERAR GRÁFICOS (SPARK)** 📊
Calcula las correlaciones y entrena el Random Forest con PySpark.

**Comando:**
```bash
docker exec jupyter_lab spark-submit /home/jovyan/work/src/analysis.py
```
Esto generará las imágenes `.png` en la carpeta `notebooks/`.

---

## **PASO 5: EJECUTAR ANÁLISIS ECONOMÉTRICO (HAUSMAN)** 📉
Calcula Efectos Fijos vs Aleatorios para validar la hipótesis.

**Comando:**
```bash
docker exec jupyter_lab python /home/jovyan/work/src/econometric_analysis.py
```
Genera reporte en `notebooks/hausman_results.txt`.

---

## **PASO 6: LANZAR LA "SUPER WEB" (DASHBOARD)** 🚀
Inicia el servidor de Streamlit en segundo plano.

**Comando (Versión Clásica):**
```bash
docker exec -d -w /home/jovyan/work/src jupyter_lab streamlit run app_streamlit.py
```

**Comando (Versión PRO 3D) 🌟:**
```bash
docker exec -d -w /home/jovyan/work/src jupyter_lab streamlit run app_streamlit_pro.py
```

---

## **PASO 7: GENERAR DASHBOARD HTML (PORTÁTIL)** 🌍
Genera un archivo HTML único con todos los gráficos incrustados, ideal para enviar por correo o entregar sin necesidad de que el receptor tenga Docker instalado.

**Comando:**
```bash
docker exec jupyter_lab python /home/jovyan/work/src/export_dashboard.py
```
El archivo se generará en `dashboard.html`.

---

## **ACCESOS** 🌐

| Servicio | URL | Notas |
|----------|-----|-------|
| **DASHBOARD (Streamlit)** | http://localhost:8501 | Web interactiva con el Bot IA |
| **JUPYTER LAB** | http://localhost:8888 | Contraseña: `bigdata2024` |
| **SPARK MASTER** | http://localhost:8081 | Estado del cluster |
| **SPARK JOB UI** | http://localhost:4040 | Solo funciona **DURANTE** la ejecución de scripts |

---

## **CÓMO APAGAR TODO** 🛑
Cuando termines, elimina todo para limpiar tu máquina.

**Comando:**
```bash
docker-compose down
```

---

## **CÓMO ACTUALIZAR EN GITHUB** 🐙
Si haces cambios en el código y quieres subirlos a tu repositorio:

1. **Verificar estado:**
   ```bash
   git status
   ```

2. **Agregar cambios:**
   ```bash
   git add .
   ```

3. **Guardar cambios:**
   ```bash
   git commit -m "Mensaje explicando tus cambios"
   ```

4. **Subir a GitHub:**
   ```bash
   git push origin main
   ```

5. **(Opcional) Traer cambios remotos:**
   ```bash
   git pull origin main
   ```

---

## **TROUBLESHOOTING / EXTRAS** 🛠️

### ¿El Dashboard no se actualiza?
A veces Streamlit no detecta cambios. Para reiniciarlo:
1. Mata el proceso:
   ```bash
   docker exec jupyter_lab pkill -f streamlit
   ```
2. Inícialo de nuevo:
   ```bash
   docker exec -d jupyter_lab streamlit run /home/jovyan/work/src/app_streamlit.py
   ```

### ¿Error: "Ports are not available"?
Si el puerto (8080, 8081, etc.) está ocupado:
1. Abre `docker-compose.yml`.
2. Busca los `ports`.
3. Cambia el número de la IZQUIERDA. (Ej: `"8085:8080"`).
4. Ejecuta: `docker-compose up -d`.

---

## **EJECUCIÓN RECURRENTE** 🔄
Si ya instalaste todo una vez:

1. **Abrir Docker Desktop.**
2. **Levantar servicios:**
   ```bash
   docker-compose up -d
   ```
3. **Lanzar Dashboard:**
   ```bash
   docker exec -d jupyter_lab streamlit run /home/jovyan/work/src/app_streamlit_pro.py
   ```
4. **Ir a:** http://localhost:8501

---

## **SCRIPT AUTOMÁTICO** 🤖
Si no quieres escribir comandos de Git:
1. Busca el archivo `upload_to_github.bat` en esta misma carpeta.
2. Haz doble clic sobre él.
3. Sigue las instrucciones.
