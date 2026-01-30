# 🏗️ Infraestructura para el Trabajo Final

Para completar este proyecto, necesitarás acceder a la base de datos **PostgreSQL** desplegada en Docker.

## 🚀 Guía Rápida

1.  **Levantar Servicios:**
    Ejecuta el script de setup (como Administrador):
    ```powershell
    ../scripts/setup_cluster.ps1
    ```

2.  **Verificar Acceso:**
    *   **Postgres:** `localhost:5432`
    *   **Usuario:** `postgres`
    *   **Password:** `password`
    *   **Database:** `bigdata_db`

---

## 📘 Documentación Completa

Hemos preparado una guía detallada ("La Guía de Oro") que explica:
*   Cómo funciona el almacenamiento híbrido (SSD vs HDD).
*   Por qué usamos Docker.
*   Por qué elegimos PostgreSQL sobre Mongo/Cassandra.

👉 **[LEER LA GUÍA COMPLETA DE INFRAESTRUCTURA](../docs/infraestructura.md)**  
*(También disponible en la web del curso)*

---

## ❓ Preguntas Frecuentes

**¿Dónde están mis datos físicamente?**
Si usaste el modo SSD, están en `E:\BIGDATA_LAB_STORAGE\ejercicios_bigdata\datos`.
Si usaste modo local, están en `ejercicios_bigdata\datos`.

**¿Por qué no puedo conectar a Postgres?**
Asegúrate de que Docker Desktop esté corriendo y que ejecutaste el script de setup al menos una vez.
