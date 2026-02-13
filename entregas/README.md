<<<<<<< HEAD
# Entregas de Ejercicios

Esta carpeta contiene las entregas de todos los alumnos, organizadas por **módulo**.

---

## Estructura

```
entregas/
├── 01_bases_de_datos/       # MÓDULO 01: Todos los ejercicios de bases de datos
│   ├── 1.1_sqlite/          # Plantilla/ejemplo ejercicio 1.1
│   ├── 2.1_postgresql_hr/   # Plantilla/ejemplo ejercicio 2.1
│   ├── 2.2_postgresql_jardineria/
│   ├── 2.3_postgresql_tienda/
│   ├── 3.1_oracle_hr/
│   ├── 3.2_oracle_jardineria/
│   ├── 4.1_sqlserver_tienda/
│   ├── 5.1_analisis_excel/
│   └── apellido_nombre/     # ← Aquí creas TU carpeta con TODOS tus ejercicios del módulo
│
└── 02_limpieza_datos/       # MÓDULO 02: Pipeline ETL QoG
    └── apellido_nombre/     # ← Aquí creas TU carpeta para este módulo
```

**Importante:** Las carpetas numeradas (1.1, 2.1, etc.) son **plantillas/ejemplos**.
**TÚ creas** una carpeta `apellido_nombre/` dentro del módulo y organizas tus entregas ahí.

---

## Cómo Entregar

**ANTES de entregar, lee la guía general:**

👉 **[Guía General de Entregas](https://todoeconometria.github.io/ejercicios-bigdata/entregas/guia-entregas/)**

Cada carpeta de ejercicio también contiene un `README.md` con instrucciones específicas.

---

## Formato de Carpetas por Alumno

```
entregas/XX_modulo/apellido_nombre/
```

**Ejemplos:**

**Módulo 01 - Bases de Datos:**
```
entregas/01_bases_de_datos/garcia_maria/
├── 1.1_sqlite/
│   ├── README.md
│   └── queries.sql
├── 2.1_postgresql_hr/
│   ├── README.md
│   └── queries.sql
└── 5.1_analisis_excel/
    ├── README.md
    └── script.py
```

**Módulo 02 - Limpieza de Datos:**
```
entregas/02_limpieza_datos/garcia_maria/
├── README.md
├── src/
├── scripts/
└── sql/
```

**Reglas del nombre de carpeta:**
- Todo en minúsculas
- Sin tildes ni caracteres especiales
- Formato: `apellido_nombre` (apellido primero)
- Separado por guión bajo `_`

**Ejemplos válidos:**
- `garcia_maria/`
- `lopez_juan/`
- `rodriguez_carlos/`

**Ejemplos NO válidos:**
- ❌ `María García/` (mayúsculas, tildes)
- ❌ `maria_garcia/` (nombre primero)
- ❌ `garcia-maria/` (guión en lugar de guión bajo)

---

## Múltiples Archivos

✅ **Puedes subir:**
- Múltiples archivos dentro de tu carpeta
- Actualizar archivos (nuevos commits)
- Organizar en subcarpetas si lo necesitas

❌ **NO subas:**
- Archivos `.db`, `.sqlite` (bases de datos)
- Archivos `.csv` grandes (datos)
- Archivos temporales (`.pyc`, `__pycache__/`, `.DS_Store`)
- Carpetas `venv/`, `node_modules/`

---

## Importante

- ⏰ Cada ejercicio tiene su fecha límite
- 🔄 Sincroniza tu fork ANTES de cada entrega
- 🚫 NO copies código de compañeros
- 📝 Consulta las instrucciones específicas de cada ejercicio

---

**Dudas?** Consulta la [guía general](https://todoeconometria.github.io/ejercicios-bigdata/entregas/guia-entregas/) o pregunta al profesor.
=======
"""
═══════════════════════════════════════════════════════════════════════════════
GUÍA DE ENTREGAS
═══════════════════════════════════════════════════════════════════════════════

Autor/Instructor: Juan Marcelo Gutierrez Miranda
Afiliación: @TodoEconometria
Repositorio: https://github.com/TodoEconometria/ejercicios-bigdata

═══════════════════════════════════════════════════════════════════════════════
"""

# 📥 Zona de Entregas

Esta carpeta está destinada a recibir los ejercicios resueltos por los estudiantes.

## 📋 Instrucciones Rápidas

Para entregar tus ejercicios, sigue estrictamente la guía oficial paso a paso.  
Esto asegura que nuestros pipelines de integración continua (CI/CD) puedan validar tu código automáticamente.

👉 **GUÍA OFICIAL:** [todoeconometria.github.io/ejercicios-bigdata/entregas/guia-entregas/](https://todoeconometria.github.io/ejercicios-bigdata/entregas/guia-entregas/)

---

## 🏗️ Estructura Esperada

Debes subir tu solución en la carpeta correspondiente al módulo:

```plaintext
entregas/
├── 01_bases_de_datos/
│   └── TU_USUARIO_GITHUB/      <-- Crea una carpeta con tu usuario
│       ├── solucion.py
│       └── README.md
│
├── 02_limpieza_datos/
│   └── TU_USUARIO_GITHUB/
│       └── ...
│
└── ...
```

## ⚠️ Reglas Importantes

1. **NO subas datasets:** Ni archivos CSV, Parquet, o bases de datos SQLite (.db).
2. **NO subas entornos virtuales:** Ignora carpetas `.venv`, `env`, etc.
3. **Respeto al formato:** Usa los nombres de archivo solicitados en cada enunciado.

---

> _"El código limpio y bien organizado es la primera señal de un profesional de datos."_
>>>>>>> upstream/main
