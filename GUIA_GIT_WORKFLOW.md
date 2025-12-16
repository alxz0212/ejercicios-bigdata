# Guía de Flujo de Trabajo: Git y GitHub

Esta guía resume los pasos necesarios para trabajar colaborativamente en este proyecto, desde la descarga inicial hasta la entrega de tu solución mediante un Pull Request.

## 1. Clonar el Repositorio (Inicio)
Si estás en una PC nueva o no tienes el proyecto, el primer paso es descargarlo.

```bash
# 1. Copia la URL de tu repositorio desde GitHub
# 2. En tu terminal, ejecuta:
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# 3. Entra en la carpeta del proyecto
cd ejercicios-bigdata
```

---

## 2. Sincronizar y Cambiar de Rama
Este es el paso clave para trabajar sobre tu versión específica (`entrega-alexis`) y asegurarte de tener lo último que subiste desde otra PC.

```bash
# 1. Descarga toda la información reciente de GitHub (sin fusionar nada aún)
git fetch origin

# 2. Cámbiate a tu rama de trabajo.
# Si la rama ya existe en GitHub pero no en tu PC, este comando la "crea" localmente
# y la conecta automáticamente con la versión remota.
git checkout entrega-alexis
```

> **Nota:** Ahora tu entorno de trabajo (los archivos que ves en PyCharm) corresponden a lo que hay en la rama `entrega-alexis`.

---

## 3. Guardar y Subir Cambios (El ciclo diario)
Cada vez que hagas modificaciones en el código (editar archivos, agregar scripts), sigue estos pasos para guardarlos en la nube.

### A. Verificar qué has cambiado
```bash
git status
# Te mostrará en rojo los archivos modificados.
```

### B. Preparar los archivos (Stage)
```bash
# Agrega todos los archivos modificados al área de preparación
git add .
```

### C. Confirmar los cambios (Commit)
Guarda una "foto" de tus cambios con un mensaje descriptivo.
```bash
git commit -m "Descripción breve de lo que hiciste (ej: Agregué consultas modelo C)"
```

### D. Subir a GitHub (Push)
Envía tus commits locales a tu rama en el servidor.
```bash
git push origin entrega-alexis
```

---

## 4. Resumen Visual del Flujo
Aquí puedes ver cómo se mueven tus archivos según el comando que uses:

```text
+---------------------+       git add        +----------------------+
|   Tu PC (Editor)    | -------------------> |  Área de Preparación |
| (Working Directory) |                      |       (Stage)        |
+---------------------+                      +----------------------+
          ^                                             |
          | git pull                                    | git commit
          |                                             v
+---------------------+       git push       +----------------------+
|    GitHub (Nube)    | <------------------- |    Tu Rama Local     |
|   (Remote Repo)     |                      |    (Local Repo)      |
+---------------------+                      +----------------------+
```

**Explicación rápida:**
1.  **Working Directory:** Donde editas tus archivos (PyCharm).
2.  **Stage (`git add`):** Donde apartas los archivos que quieres guardar.
3.  **Local Repo (`git commit`):** Donde se guardan los cambios en tu disco duro (historial local).
4.  **Remote Repo (`git push`):** Donde se guardan los cambios en Internet (GitHub).

---

## 5. Crear un Pull Request (Entrega Final)
Cuando hayas terminado tu trabajo y quieras que otros (o el profesor) revisen tu solución e integren tus cambios a la rama principal (`main`).

1.  Ve a la página de tu repositorio en **GitHub.com**.
2.  Verás un aviso amarillo que dice **"entrega-alexis had recent pushes..."**. Haz clic en el botón verde **"Compare & pull request"**.
3.  Si no ves el aviso:
    *   Ve a la pestaña **"Pull requests"**.
    *   Haz clic en **"New pull request"**.
    *   **Base:** selecciona `main` (a donde van los cambios).
    *   **Compare:** selecciona `entrega-alexis` (de donde vienen los cambios).
4.  Escribe un título y una descripción de lo que has resuelto.
5.  Haz clic en **"Create pull request"**.

¡Listo! Ahora tu solución está visible para revisión y fusión.
