<<<<<<< HEAD
# Guía General de Entregas

Esta guía se aplica a **TODOS** los ejercicios del curso.

---

## Estructura de Carpetas por Alumno

Cada alumno debe crear **UNA carpeta personal** dentro de la carpeta de entrega del ejercicio correspondiente.

### Formato del Nombre

```
apellido_nombre
```

**Reglas:**
- Todo en minúsculas
- Sin tildes ni caracteres especiales
- Separado por guión bajo `_`
- Formato: `apellido_nombre` (apellido primero)

**Ejemplos válidos:**
- `garcia_maria/`
- `lopez_juan/`
- `martinez_ana/`
- `rodriguez_carlos/`

**Ejemplos NO válidos:**
- ❌ `María García/` (mayúsculas, tildes, espacios)
- ❌ `maria_garcia/` (nombre primero)
- ❌ `garcia-maria/` (guión en lugar de guión bajo)

---

## Ubicación de las Entregas

```
entregas/
├── 1.1_sqlite/                  # Ejercicio 1.1
│   ├── garcia_maria/            # Carpeta del alumno
│   │   ├── archivo1.py
│   │   ├── archivo2.md
│   │   └── ...
│   └── lopez_juan/              # Otro alumno
│       └── ...
│
├── 2.1_postgresql_hr/           # Ejercicio 2.1
│   └── garcia_maria/
│       └── ...
│
└── ...                          # Más ejercicios
=======
# Como Entregar tus Trabajos

Esta guia te explica **paso a paso** como entregar. No necesitas saber Git avanzado.

---

## Resumen en 30 segundos

```
1. Haces fork del repo (solo una vez)
2. Trabajas en TU fork
3. Subes tus cambios a TU fork
4. El profesor revisa TU fork automaticamente (sin PR)
```

**NO necesitas crear Pull Request.** El sistema automatico evalua
tu archivo **PROMPTS.md** directamente en tu fork.

---

## Diagrama del Flujo

```mermaid
flowchart TB
    subgraph Profesor["REPOSITORIO DEL PROFESOR"]
        P1["github.com/TodoEconometria/ejercicios-bigdata<br/><br/>Aqui estan los ejercicios<br/>NO modificas nada aqui"]
    end

    subgraph Alumno["TU FORK (tu copia)"]
        A1["github.com/TU_USUARIO/ejercicios-bigdata<br/><br/>Aqui trabajas y subes tu codigo"]
    end

    subgraph Local["TU PC"]
        L1["Carpeta ejercicios-bigdata/<br/><br/>Aqui programas"]
    end

    subgraph Sistema["SISTEMA AUTOMATICO"]
        S1["Script del profesor<br/><br/>Revisa todos los forks<br/>Genera notas automaticas"]
    end

    Profesor -->|"1. Fork (copiar)"| Alumno
    Alumno -->|"2. Clone (descargar)"| Local
    Local -->|"3. Push (subir)"| Alumno
    Alumno -->|"4. Revision automatica"| Sistema

    style Profesor fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style Alumno fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style Local fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style Sistema fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
>>>>>>> upstream/main
```

---

<<<<<<< HEAD
## Múltiples Archivos por Alumno

### ✅ Permitido

- Subir **múltiples archivos** dentro de tu carpeta
- Actualizar archivos (hacer nuevos commits)
- Agregar archivos adicionales (capturas, PDFs, etc.)
- Organizar en subcarpetas si lo necesitas

**Ejemplo:**
```
entregas/01_bases_de_datos/garcia_maria/
└── 1.1_sqlite/
    ├── solucion_modelo_a.py
    ├── solucion_modelo_b.py
    ├── ANALISIS_DATOS.md
    ├── consultas.sql
    ├── capturas/
    │   ├── screenshot1.png
    │   └── screenshot2.png
    └── notas_personales.txt
```

### ❌ NO Permitido

- ❌ Subir archivos `.db` (bases de datos binarias)
- ❌ Subir archivos `.csv` grandes (datos)
- ❌ Subir archivos temporales (`.pyc`, `__pycache__/`, `.DS_Store`)
- ❌ Subir carpetas `venv/`, `node_modules/`

---

## Opciones de Entrega

### Opción 1: Archivos Sueltos (Recomendada)

Sube tus archivos directamente en tu carpeta:

```bash
git add entregas/X.X_ejercicio/tu_apellido_nombre/
git commit -m "Entrega X.X - Tu Nombre"
git push origin tu-rama
```

### Opción 2: Archivo ZIP

Si prefieres, puedes comprimir todo en un ZIP:

```
entregas/01_bases_de_datos/garcia_maria.zip
```

**Nota:** La Opción 1 es preferida porque permite revisión más fácil.

---

## Workflow Completo de Entrega

### Paso 1: Fork del Repositorio (Solo la primera vez)

1. Ve a: https://github.com/TodoEconometria/ejercicios-bigdata
2. Haz clic en **"Fork"** (arriba a la derecha)
3. Ahora tienes tu copia: `https://github.com/TU_USUARIO/ejercicios-bigdata`

### Paso 2: Clonar TU Fork

```bash
=======
## Paso 1: Crear tu Fork (solo una vez)

Un "fork" es tu copia personal del repositorio.

1. Ve a: [github.com/TodoEconometria/ejercicios-bigdata](https://github.com/TodoEconometria/ejercicios-bigdata)
2. Click en el boton **"Fork"** (arriba a la derecha)
3. Click en **"Create fork"**
4. Listo! Ahora tienes `github.com/TU_USUARIO/ejercicios-bigdata`

!!! success "Solo haces esto UNA VEZ"
    Tu fork es tuyo para siempre. Todos tus trabajos van ahi.

---

## Paso 2: Descargar a tu PC (solo una vez)

```bash
# En tu terminal (CMD, PowerShell, o Terminal)
cd Documentos
>>>>>>> upstream/main
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
```

<<<<<<< HEAD
### Paso 3: Sincronizar con el Repositorio Original

**IMPORTANTE:** Antes de cada nueva entrega, sincroniza tu fork.

👉 **[Ver guía completa de sincronización](https://todoeconometria.github.io/ejercicios-bigdata/git-github/sincronizar-fork/)**

```bash
# Añadir upstream (solo la primera vez)
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git

# Sincronizar
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Paso 4: Crear Rama para tu Entrega

```bash
git checkout -b apellido-ejercicio-X.X
```

**Ejemplo:**
```bash
git checkout -b garcia-ejercicio-1.1
```

### Paso 5: Crear tu Carpeta de Entrega

```bash
mkdir -p entregas/X.X_ejercicio/apellido_nombre
```

**Ejemplo:**
```bash
mkdir -p entregas/01_bases_de_datos/garcia_maria/1.1_sqlite
```

### Paso 6: Completar tus Archivos

Copia plantillas o crea tus archivos desde cero en tu carpeta:

```bash
# Ver qué archivos necesitas entregar
cat ejercicios/01_bases_de_datos/X.X_ejercicio/README.md
```

### Paso 7: Verificar Archivos

```bash
# Ver tus archivos
ls -la entregas/X.X_ejercicio/apellido_nombre/

# Ver estado de Git
git status
```

### Paso 8: Commit

```bash
# Agregar archivos
git add entregas/X.X_ejercicio/apellido_nombre/

# Commit con mensaje descriptivo
git commit -m "Entrega X.X - Nombre Apellido"
```

**Ejemplos de mensajes:**
- `"Entrega 1.1 - María García"`
- `"Entrega 2.1 PostgreSQL HR - Juan López"`

### Paso 9: Push a TU Fork

```bash
git push origin apellido-ejercicio-X.X
```

### Paso 10: Crear Pull Request

1. Ve a TU fork en GitHub
2. Verás un banner: **"apellido-ejercicio-X.X had recent pushes"**
3. Haz clic en **"Compare & pull request"**
4. **Título del PR:** `[X.X] Apellido Nombre - Título del Ejercicio`
5. Completa el checklist automático
6. Haz clic en **"Create pull request"**

---

## Validación Automática

Cuando crees tu PR, un bot automático verificará:

- ✅ Formato del nombre de carpeta
- ✅ Archivos obligatorios presentes
- ✅ Sin archivos prohibidos
- ⚠️ Si tu fork está desactualizado (>5 commits atrás)

**Si tu fork está desactualizado:**
El bot te avisará y agregará una etiqueta. Debes sincronizar antes de continuar.

---

## Actualizar tu PR (Correcciones)

Si el profesor pide correcciones o quieres actualizar:

```bash
# Edita tus archivos localmente

# Commit de nuevo
git add entregas/X.X_ejercicio/apellido_nombre/
git commit -m "Correcciones solicitadas"

# Push (actualiza automáticamente el PR)
git push origin apellido-ejercicio-X.X
=======
Cambia `TU_USUARIO` por tu nombre de usuario de GitHub.

!!! info "Ahora tienes la carpeta"
    Busca en `Documentos/ejercicios-bigdata/`. Ahi trabajaras siempre.

---

## Paso 3: Crear tu carpeta de entrega

Dentro de tu carpeta del repositorio, crea tu carpeta personal:

```
Para Trabajo Final:
entregas/trabajo_final/apellido_nombre/

Para ejercicios de BD:
entregas/01_bases_de_datos/1.1_sqlite/apellido_nombre/
```

!!! warning "Formato del nombre"
    - Todo en **minusculas**
    - Sin tildes ni espacios
    - Formato: `apellido_nombre`
    - Ejemplo: `garcia_maria`, `lopez_juan`

### Para el Trabajo Final, copia la plantilla:

```bash
# Desde la carpeta del repositorio:
cp -r trabajo_final/plantilla/ entregas/trabajo_final/tu_apellido_nombre/
```

Esto te crea todos los archivos que necesitas completar.

---

## Paso 4: Trabajar y documentar tus prompts

### El archivo mas importante: PROMPTS.md

Dentro de tu carpeta encontraras `PROMPTS.md`. Este archivo es **LO QUE SE EVALUA**.

```
entregas/trabajo_final/garcia_maria/
├── PROMPTS.md          ← OBLIGATORIO - Tus prompts de IA
├── docker-compose.yml  ← Tu infraestructura
├── pipeline.py         ← Tu codigo
└── ... otros archivos
```

### Que va en PROMPTS.md

| Seccion | Que poner |
|---------|-----------|
| **Prompt A, B, C** | Tus prompts REALES copiados tal cual (con errores y todo) |
| **Blueprint** | Al final, pedirle a la IA un resumen profesional |

!!! danger "MUY IMPORTANTE"
    **NO corrijas tus prompts.** Si escribiste "como ago q sparck lea el csv"
    con errores, pega ESO. El sistema detecta si "limpiaste" tus prompts.

    Los prompts perfectos en la Parte 1 = SOSPECHOSO.

---

## Paso 5: Subir tu trabajo

Cuando termines (o quieras guardar avances):

```bash
# Desde la carpeta del repositorio
git add .
git commit -m "Entrega Trabajo Final - Garcia Maria"
git push
```

!!! tip "Que hace cada comando"
    - `git add .` → Prepara todos tus archivos
    - `git commit -m "..."` → Guarda con un mensaje
    - `git push` → Sube a tu fork en GitHub

---

## Paso 6: Verificar tu entrega

1. Ve a tu fork: `github.com/TU_USUARIO/ejercicios-bigdata`
2. Navega a `entregas/trabajo_final/tu_apellido_nombre/`
3. Verifica que estan todos tus archivos

!!! success "Listo!"
    No necesitas hacer nada mas. El sistema automatico revisa tu archivo
    **PROMPTS.md** y genera notas basado en tu proceso de aprendizaje.

---

## Mantener tu Fork Actualizado

El profesor agrega ejercicios nuevos. Tu fork NO se actualiza solo.

### Metodo Facil (desde GitHub)

1. Ve a tu fork en GitHub
2. Si ves un banner amarillo "This branch is X commits behind", haz click
3. Click en **"Sync fork"** → **"Update branch"**
4. En tu PC: `git pull`

### Metodo Terminal

```bash
# Agregar el repo del profesor como "upstream" (solo una vez)
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git

# Actualizar
git fetch upstream
git merge upstream/main
git push
```

!!! tip "Cuando sincronizar"
    Hazlo **cada lunes** antes de clase para tener los ejercicios nuevos.

---

## Estructura de Entrega - Trabajo Final

```
entregas/trabajo_final/apellido_nombre/
│
├── PROMPTS.md              ← LO MAS IMPORTANTE (se evalua esto)
│
├── 01_README.md            ← Tu pregunta de investigacion
├── 02_INFRAESTRUCTURA.md   ← Explicacion de tu Docker
├── 03_RESULTADOS.md        ← Graficos e interpretacion
├── 04_REFLEXION_IA.md      ← 3 momentos clave
├── 05_RESPUESTAS.md        ← Preguntas de comprension
│
├── docker-compose.yml      ← Tu YAML funcional
├── pipeline.py             ← Tu codigo ETL + analisis
├── requirements.txt        ← Dependencias
│
└── .gitignore              ← Excluir datos grandes
>>>>>>> upstream/main
```

---

<<<<<<< HEAD
## Preguntas Frecuentes

### ¿Puedo ver las entregas de otros compañeros?

Sí, los PRs son públicos. Pero **NO copies**, el sistema detecta plagios.

### ¿Cuántas veces puedo actualizar mi PR?

Las que necesites antes de la fecha límite. Cada push actualiza el PR automáticamente.

### ¿Qué pasa si me equivoco en el nombre de la carpeta?

El bot de validación te avisará. Puedes renombrar y hacer push de nuevo:

```bash
git mv entregas/X.X/nombre_incorrecto entregas/X.X/apellido_nombre
git commit -m "Corregir nombre de carpeta"
git push origin tu-rama
```

### No sé usar Git, ¿hay otra forma?

Puedes usar **GitHub Desktop** (interfaz gráfica) o pregunta al profesor.

### ¿Puedo organizar mis archivos en subcarpetas?

Sí, siempre que todo esté dentro de `entregas/X.X/apellido_nombre/`.

---

## Ayuda y Recursos

**Si tienes problemas:**
1. Revisa esta guía de nuevo
2. Consulta la guía específica del ejercicio
3. Pregunta a tus compañeros
4. Pregunta al profesor en clase

**Recursos útiles:**
- [Guía Git y GitHub](https://todoeconometria.github.io/ejercicios-bigdata/git-github/)
- [Sincronizar Fork](https://todoeconometria.github.io/ejercicios-bigdata/git-github/sincronizar-fork/)
- [Crear Pull Requests](https://todoeconometria.github.io/ejercicios-bigdata/git-github/pull-requests/)
- [Tutorial Git en español](https://git-scm.com/book/es/v2)

---

## Importante

- ⏰ Respeta las fechas límite (cada ejercicio tiene la suya)
- 🔒 NO subas información personal (contraseñas, tokens)
- 🚫 NO copies código de compañeros
- ✅ Sincroniza tu fork ANTES de cada entrega
- 📝 Lee las instrucciones específicas de cada ejercicio

---

**Última actualización:** 2025-12-17
=======
## Que NO Subir

El `.gitignore` ya protege esto, pero recuerda:

- ❌ Archivos de datos (`.csv`, `.parquet`, `.db`)
- ❌ Carpeta `venv/` o `.venv/`
- ❌ Carpeta `__pycache__/`
- ❌ Archivos `.env` con credenciales
- ❌ Archivos mayores a 10MB

---

## Como se Evalua (Sistema por PROMPTS)

!!! danger "LO MAS IMPORTANTE: PROMPTS.md"
    **El archivo PROMPTS.md es lo que se evalua.** No el codigo, no el YAML,
    sino TUS PROMPTS de IA documentados.

El sistema automatico revisa:

```
1. Lee la lista de alumnos (forks registrados)
2. Para cada fork:
   - Verifica que existe PROMPTS.md (OBLIGATORIO)
   - Analiza calidad y autenticidad de los prompts
   - Detecta si los prompts fueron "limpiados" por IA
   - Revisa coherencia entre prompts y codigo entregado
   - Calcula nota automatica basada en proceso de aprendizaje
3. Genera reporte con:
   - Ranking de todos
   - Destacados (posible bonus)
   - Sospechosos (requieren verificacion)
```

### Alertas Automaticas

| Alerta | Significado |
|--------|-------------|
| ⭐ DESTACADO | Trabajo excepcional, revisar para bonus |
| ✅ NORMAL | Cumple requisitos, nota automatica |
| ⚠️ REVISAR | Algo no cuadra, el profesor verificara |
| ❌ RECHAZADO | Copia detectada o requisitos no cumplidos |

---

## Problemas Comunes

### "No tengo la plantilla"

```bash
# Actualiza tu fork primero
git fetch upstream
git merge upstream/main

# Ahora copia la plantilla
cp -r trabajo_final/plantilla/ entregas/trabajo_final/tu_apellido/
```

### "Git me pide usuario y contrasena"

Usa tu cuenta de GitHub. Si falla, configura:

```bash
git config --global user.email "tu@email.com"
git config --global user.name "Tu Nombre"
```

### "Mis cambios no aparecen en GitHub"

Verifica que hiciste los 3 pasos:

```bash
git add .                    # 1. Preparar
git commit -m "mensaje"      # 2. Guardar
git push                     # 3. Subir  ← Este es el que sube
```

### "Quiero empezar de nuevo"

```bash
# Borrar tu carpeta y copiar plantilla de nuevo
rm -rf entregas/trabajo_final/tu_apellido/
cp -r trabajo_final/plantilla/ entregas/trabajo_final/tu_apellido/
```

---

## Fechas y Plazos

| Entrega | Fecha limite |
|---------|--------------|
| Trabajo Final | [Ver calendario del curso] |

!!! warning "Entregas tardias"
    El sistema revisa en la fecha indicada. Lo que no este en tu fork
    para esa fecha, no se evalua.

---

## Resumen Visual

```
┌─────────────────────────────────────────────────────────────────┐
│                    TU FLUJO DE TRABAJO                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Fork (una vez)                                              │
│     └── Creas tu copia en GitHub                                │
│                                                                 │
│  2. Clone (una vez)                                             │
│     └── Descargas a tu PC                                       │
│                                                                 │
│  3. Copias plantilla                                            │
│     └── cp -r trabajo_final/plantilla/ entregas/.../tu_nombre/  │
│                                                                 │
│  4. Trabajas con IA                                             │
│     └── Guardas prompts en PROMPTS.md (con errores y todo)      │
│                                                                 │
│  5. Subes cambios                                               │
│     └── git add . && git commit -m "..." && git push            │
│                                                                 │
│  6. Verificas en GitHub                                         │
│     └── Confirmas que tus archivos estan ahi                    │
│                                                                 │
│  7. Evaluacion automatica                                       │
│     └── El profesor revisa todos los forks sin que hagas nada   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Ayuda

Si tienes problemas:

1. Revisa esta guia de nuevo
2. Pregunta a un companero
3. Pregunta al profesor en clase
4. Revisa la [guia de sincronizacion](../git-github/sincronizar-fork.md)

---

**Ultima actualizacion:** 2026-02-04
>>>>>>> upstream/main
