# Reflexión sobre Modelos de Datos

## 1. ¿Cuál modelo fue más fácil de implementar? ¿Por qué?
El **Modelo A (Catálogo Simple)** fue, sin duda, el más fácil y rápido de implementar.
*   **Razón:** No requirió ningún diseño previo ni análisis de relaciones. Simplemente se trató de un bucle que leía cada archivo CSV y lo volcaba directamente en una tabla con el mismo nombre. No hubo que pensar en claves foráneas, normalización de datos o integridad referencial. Es una traducción literal de "archivo a tabla".

## 2. ¿Qué ventajas encontraste en el Modelo A?
*   **Rapidez de Ingesta:** Es ideal para una carga inicial rápida de datos "crudos" (Raw Data) sin preocuparse por la estructura.
*   **Simplicidad:** El código para generarlo es muy corto y fácil de entender.
*   **Independencia:** Si un archivo CSV cambia su estructura (ej. añade una columna rara), no rompe el esquema de las otras tablas.
*   **Preservación del Dato Original:** Al no transformar nada, se mantiene la fidelidad exacta con la fuente original, lo cual es útil para auditorías o como capa de "Staging" en un Data Warehouse.

## 3. ¿Qué desventajas encontraste en el Modelo A?
*   **Redundancia Masiva:** Datos como el nombre del fabricante se repiten miles de veces como texto (ej. "Corsair" en cada fila de memoria, fuente, teclado, etc.). Esto desperdicia espacio.
*   **Consultas Complejas:** Si quiero saber "¿Cuántos productos de Corsair tengo en total?", tendría que hacer 25 consultas `SELECT` (una por cada tabla) y sumar los resultados, o hacer una `UNION` gigante. Es inmanejable.
*   **Inconsistencia:** No hay nada que impida que en la tabla `mouse` el fabricante sea "Logitech" y en `keyboard` sea "Logitech Inc.".
*   **Mantenimiento:** Cambiar el nombre de una categoría o fabricante implica actualizar miles de registros en múltiples tablas.

## 4. ¿En qué situación usarías el Modelo B sobre el A?
Usaría el **Modelo B (Normalizado)** en cualquier aplicación real de producción donde se requiera:
*   **Integridad de Datos:** Para asegurar que los productos pertenezcan a categorías y fabricantes válidos.
*   **Consultas Eficientes:** Para poder realizar búsquedas transversales (ej. "Todos los productos de color rojo") con una sola consulta SQL simple.
*   **Escalabilidad:** Si el catálogo crece, el modelo relacional maneja mejor las actualizaciones y evita anomalías de datos.
*   **Desarrollo de Software:** Es el estándar para conectar con backends de aplicaciones (APIs, webs) que necesitan una estructura predecible.

## 5. ¿El Modelo C es necesario para todos los casos? Justifica.
**No, no es necesario para todos los casos.**
*   **Justificación:** El Modelo C añade complejidad innecesaria si el objetivo es solo *analizar* el catálogo de productos (Data Analysis) o mostrar un catálogo de solo lectura. Las tablas de `clientes`, `pedidos` y `carritos` solo tienen sentido si existe un proceso transaccional de venta. Si solo estamos haciendo Business Intelligence sobre los productos existentes, el Modelo B es suficiente y más limpio.

## 6. ¿Qué pasaría si quisieras agregar una nueva columna "descuento" a todos los productos?
*   **En Modelo A:** Tendría que modificar **25 tablas**. Debería ejecutar 25 sentencias `ALTER TABLE` (una por cada categoría de producto: `ALTER TABLE cpu ADD COLUMN descuento...`, `ALTER TABLE mouse...`, etc.). Es propenso a errores si olvido una tabla.
*   **En Modelo B:** Tendría que modificar **1 sola tabla**. Solo ejecutaría `ALTER TABLE productos ADD COLUMN descuento...` y automáticamente todos los productos de todas las categorías tendrían ese campo disponible. Esta es una de las mayores ventajas de la normalización.

---

## Extras: Cosas que se pueden mejorar

### 1. Manejo de Atributos Específicos (Modelo EAV o JSON)
El Modelo B actual simplifica demasiado al unificar todo en la tabla `productos`. Perdemos información valiosa como `socket` (CPUs), `screen_size` (Monitores) o `wattage` (Fuentes).
*   **Mejora:** Podríamos añadir una columna `atributos_extra` de tipo JSON en la tabla `productos` para guardar estas características específicas sin romper el esquema rígido, o implementar un modelo Entidad-Atributo-Valor (EAV).

### 2. Normalización de Colores
En el análisis vimos que los colores están sucios ("Black", "Black/Red", "Matte Black").
*   **Mejora:** Un script de limpieza previo para estandarizar los colores antes de insertarlos en la base de datos mejoraría mucho la calidad de las consultas.

### 3. Índices
Para mejorar el rendimiento de las consultas en el Modelo B y C, sería fundamental añadir índices en las columnas que se usan para filtrar o unir, como `categoria_id`, `fabricante_id` y `precio`.
