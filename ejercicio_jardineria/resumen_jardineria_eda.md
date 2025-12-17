# Reporte EDA: Base de Datos Jardinería

**Archivo analizado:** `jardineria.db`

**Tablas encontradas:** oficina, empleado, gama_producto, cliente, pedido, producto, detalle_pedido, pago

## Tabla: oficina
- **Dimensiones:** 20 filas x 8 columnas
- **Estructura y Tipos de Datos:**
```text
["<class 'pandas.core.frame.DataFrame'>", 'RangeIndex: 20 entries, 0 to 19', 'Data columns (total 8 columns):', ' #   Column            Non-Null Count  Dtype ', '---  ------            --------------  ----- ', ' 0   codigo_oficina    20 non-null     object', ' 1   ciudad            20 non-null     object', ' 2   pais              20 non-null     object', ' 3   region            20 non-null     object', ' 4   codigo_postal     20 non-null     object', ' 5   telefono          20 non-null     object', ' 6   linea_direccion1  20 non-null     object', ' 7   linea_direccion2  20 non-null     object']
```
- **Ejemplo de Datos (Primeras 3 filas):**
```text
codigo_oficina     ciudad      pais    region codigo_postal        telefono                        linea_direccion1 linea_direccion2
        OF-001       León   Austria Guipúzcoa         36573  +34807 425 140                   Ronda Valero Millán 4         Puerta 1
        OF-002 Valladolid Filipinas  Baleares         01808 +34947 96 10 95                  Cañada Petrona Farré 8          Apt. 74
        OF-003  Guipúzcoa Filipinas     Ávila         47951 +34 888 443 805 Urbanización de José Manuel Cañellas 27           Piso 4
```
- **Análisis de Calidad:**
  - ✅ No se detectaron valores nulos.
  - ✅ No hay filas completamente duplicadas.
- **Valores Únicos en Columnas de Texto (Top 5):**
  - `codigo_oficina`: 20 valores únicos. Ej: OF-001, OF-002, OF-003, OF-004, OF-005...
  - `ciudad`: 17 valores únicos. Ej: León, Valladolid, Guipúzcoa, Melilla, Valencia...
  - `pais`: 18 valores únicos. Ej: Austria, Filipinas, Lesotho, Belice, Bosnia y Herzegovina...
  - `region`: 16 valores únicos. Ej: Guipúzcoa, Baleares, Ávila, Navarra, Barcelona...
  - `codigo_postal`: 20 valores únicos. Ej: 36573, 01808, 47951, 12615, 34558...
  - `telefono`: 20 valores únicos. Ej: +34807 425 140, +34947 96 10 95, +34 888 443 805, +34848967671, +34 984 891 384...
  - `linea_direccion1`: 20 valores únicos. Ej: Ronda Valero Millán 4, Cañada Petrona Farré 8, Urbanización de José Manuel Cañellas 27, Urbanización de Noa Coll 17, Cuesta Rosenda Lledó 8 Puerta 9 ...
  - `linea_direccion2`: 14 valores únicos. Ej: Puerta 1, Apt. 74, Piso 4, Apt. 26, Puerta 3...

---
## Tabla: empleado
- **Dimensiones:** 20 filas x 9 columnas
- **Estructura y Tipos de Datos:**
```text
["<class 'pandas.core.frame.DataFrame'>", 'RangeIndex: 20 entries, 0 to 19', 'Data columns (total 9 columns):', ' #   Column           Non-Null Count  Dtype  ', '---  ------           --------------  -----  ', ' 0   codigo_empleado  20 non-null     int64  ', ' 1   nombre           20 non-null     object ', ' 2   apellido1        20 non-null     object ', ' 3   apellido2        20 non-null     object ', ' 4   extension        20 non-null     object ', ' 5   email            20 non-null     object ', ' 6   codigo_oficina   20 non-null     object ', ' 7   codigo_jefe      19 non-null     float64', ' 8   puesto           20 non-null     object ']
```
- **Ejemplo de Datos (Primeras 3 filas):**
```text
 codigo_empleado  nombre apellido1 apellido2 extension                     email codigo_oficina  codigo_jefe                          puesto
               1 Ciríaco    Ortuño  Carballo      0000        ecobos@example.com         OF-009          NaN                Director General
               2 Guiomar   Barriga      Rosa      3093 adelardomarti@example.net         OF-011          1.0 Ecónomo y mayordomos domésticos
               3    René   Almeida   Iglesia      5479  irmatrujillo@example.net         OF-011          1.0  Catador de alimentos y bebidas
```
- **Análisis de Calidad:**
  - **Valores Nulos detectados:**
```text
             Nulos  % Nulos
codigo_jefe      1      5.0
```
  - ✅ No hay filas completamente duplicadas.
- **Estadísticas Numéricas (Min, Max, Promedio):**
```text
      codigo_empleado  codigo_jefe
min               1.0     1.000000
max              20.0    17.000000
mean             10.5     5.526316
```
- **Valores Únicos en Columnas de Texto (Top 5):**
  - `nombre`: 20 valores únicos. Ej: Ciríaco, Guiomar, René, Evaristo, Pastora...
  - `apellido1`: 19 valores únicos. Ej: Ortuño, Barriga, Almeida, Morcillo, Manzanares...
  - `apellido2`: 20 valores únicos. Ej: Carballo, Rosa, Iglesia, Arnaiz, Godoy...
  - `extension`: 20 valores únicos. Ej: 0000, 3093, 5479, 8113, 6301...
  - `email`: 20 valores únicos. Ej: ecobos@example.com, adelardomarti@example.net, irmatrujillo@example.net, oteroemperatriz@example.net, maristela84@example.org...
  - `codigo_oficina`: 11 valores únicos. Ej: OF-009, OF-011, OF-002, OF-004, OF-001...
  - `puesto`: 20 valores únicos. Ej: Director General, Ecónomo y mayordomos domésticos, Catador de alimentos y bebidas, Catador de bebidas, Músico...

---
## Tabla: gama_producto
- **Dimensiones:** 20 filas x 4 columnas
- **Estructura y Tipos de Datos:**
```text
["<class 'pandas.core.frame.DataFrame'>", 'RangeIndex: 20 entries, 0 to 19', 'Data columns (total 4 columns):', ' #   Column             Non-Null Count  Dtype ', '---  ------             --------------  ----- ', ' 0   gama               20 non-null     object', ' 1   descripcion_texto  20 non-null     object', ' 2   descripcion_html   20 non-null     object', ' 3   imagen             20 non-null     object']
```
- **Ejemplo de Datos (Primeras 3 filas):**
```text
        gama                               descripcion_texto descripcion_html               imagen
Herramientas         Entrar principio mal principal estados. <html>...</html> img/Herramientas.jpg
    Frutales                         Baja expresión antonio. <html>...</html>     img/Frutales.jpg
Ornamentales Programas algunas jefe fútbol relaciones misma. <html>...</html> img/Ornamentales.jpg
```
- **Análisis de Calidad:**
  - ✅ No se detectaron valores nulos.
  - ✅ No hay filas completamente duplicadas.
- **Valores Únicos en Columnas de Texto (Top 5):**
  - `gama`: 20 valores únicos. Ej: Herramientas, Frutales, Ornamentales, Riego, Mobiliario...
  - `descripcion_texto`: 20 valores únicos. Ej: Entrar principio mal principal estados., Baja expresión antonio., Programas algunas jefe fútbol relaciones misma., Hospital veces puntos puede obra actividades., Encuentran educación aire mantener j verdad....
  - `descripcion_html`: 1 valores únicos. Ej: <html>...</html>...
  - `imagen`: 20 valores únicos. Ej: img/Herramientas.jpg, img/Frutales.jpg, img/Ornamentales.jpg, img/Riego.jpg, img/Mobiliario.jpg...

---
## Tabla: cliente
- **Dimensiones:** 20 filas x 14 columnas
- **Estructura y Tipos de Datos:**
```text
["<class 'pandas.core.frame.DataFrame'>", 'RangeIndex: 20 entries, 0 to 19', 'Data columns (total 14 columns):', ' #   Column                      Non-Null Count  Dtype  ', '---  ------                      --------------  -----  ', ' 0   codigo_cliente              20 non-null     int64  ', ' 1   nombre_cliente              20 non-null     object ', ' 2   nombre_contacto             20 non-null     object ', ' 3   apellido_contacto           20 non-null     object ', ' 4   telefono                    20 non-null     object ', ' 5   fax                         20 non-null     object ', ' 6   linea_direccion1            20 non-null     object ', ' 7   linea_direccion2            20 non-null     object ', ' 8   ciudad                      20 non-null     object ', ' 9   region                      20 non-null     object ', ' 10  pais                        20 non-null     object ', ' 11  codigo_postal               20 non-null     object ', ' 12  codigo_empleado_rep_ventas  20 non-null     int64  ', ' 13  limite_credito              20 non-null     float64']
```
- **Ejemplo de Datos (Primeras 3 filas):**
```text
 codigo_cliente                     nombre_cliente nombre_contacto apellido_contacto        telefono              fax              linea_direccion1 linea_direccion2    ciudad    region           pais codigo_postal  codigo_empleado_rep_ventas  limite_credito
              1                 Hermanos Díez S.L.         Cecilio          Manrique    +34878054223 +34 826 29 62 69 Paseo de Jose Angel Valera 30                  Guipúzcoa   Cáceres Arabia Saudita         50457                          11    43087.009996
              2 Supermercados Inteligentes S.L.N.E         Petrona            Arenas +34803 69 64 07  +34921 07 36 99       Plaza de Eloísa Reina 9                     Lleida    Cuenca        Somalia         30560                           6    12968.684451
              3   Construcción del Noroeste S.Com.      Jose Angel             Peiró   +34 988151941     +34873241004        Cañada Dafne Arnau 303                    Granada Barcelona           Cuba         27129                          19    15241.942886
```
- **Análisis de Calidad:**
  - ✅ No se detectaron valores nulos.
  - ✅ No hay filas completamente duplicadas.
- **Estadísticas Numéricas (Min, Max, Promedio):**
```text
      codigo_cliente  codigo_empleado_rep_ventas  limite_credito
min              1.0                         1.0     2108.044776
max             20.0                        20.0    49824.716103
mean            10.5                        10.8    28190.082755
```
- **Valores Únicos en Columnas de Texto (Top 5):**
  - `nombre_cliente`: 20 valores únicos. Ej: Hermanos Díez S.L., Supermercados Inteligentes S.L.N.E, Construcción del Noroeste S.Com., Villegas & Asociados S.L., Suministros Manzano y asociados S.L.U....
  - `nombre_contacto`: 19 valores únicos. Ej: Cecilio, Petrona, Jose Angel, Maxi, Bautista...
  - `apellido_contacto`: 19 valores únicos. Ej: Manrique, Arenas, Peiró, Garcés, Arjona...
  - `telefono`: 20 valores únicos. Ej: +34878054223, +34803 69 64 07, +34 988151941, +34928004932, +34 888 703 564...
  - `fax`: 20 valores únicos. Ej: +34 826 29 62 69, +34921 07 36 99, +34873241004, +34 843 50 19 43, +34 880 05 22 97...
  - `linea_direccion1`: 20 valores únicos. Ej: Paseo de Jose Angel Valera 30, Plaza de Eloísa Reina 9, Cañada Dafne Arnau 303, Calle de Yaiza Pelayo 505, Alameda de Angelina Tomas 4 Apt. 23 ...
  - `linea_direccion2`: 1 valores únicos. Ej: ...
  - `ciudad`: 17 valores únicos. Ej: Guipúzcoa, Lleida, Granada, Sevilla, Ávila...
  - `region`: 18 valores únicos. Ej: Cáceres, Cuenca, Barcelona, Baleares, Madrid...
  - `pais`: 20 valores únicos. Ej: Arabia Saudita, Somalia, Cuba, Guinea Ecuatorial, Federación de Rusia...
  - `codigo_postal`: 20 valores únicos. Ej: 50457, 30560, 27129, 08127, 13379...

---
## Tabla: pedido
- **Dimensiones:** 20 filas x 7 columnas
- **Estructura y Tipos de Datos:**
```text
["<class 'pandas.core.frame.DataFrame'>", 'RangeIndex: 20 entries, 0 to 19', 'Data columns (total 7 columns):', ' #   Column          Non-Null Count  Dtype ', '---  ------          --------------  ----- ', ' 0   codigo_pedido   20 non-null     int64 ', ' 1   fecha_pedido    20 non-null     object', ' 2   fecha_esperada  20 non-null     object', ' 3   fecha_entrega   20 non-null     object', ' 4   estado          20 non-null     object', ' 5   comentarios     20 non-null     object', ' 6   codigo_cliente  20 non-null     int64 ']
```
- **Ejemplo de Datos (Primeras 3 filas):**
```text
 codigo_pedido fecha_pedido fecha_esperada fecha_entrega      estado                                          comentarios  codigo_cliente
             1   2025-04-13     2025-06-22    2025-11-17   Rechazado                         Sean uno fuerte suelo todas.               3
             2   2025-09-05     2026-01-03    2025-09-24 En tránsito                 Visto señora contenido hermano este.              17
             3   2025-12-02     2025-12-05    2025-12-15   Rechazado Juez efectos autoridades sol favor aquí temas hijos.               5
```
- **Análisis de Calidad:**
  - ✅ No se detectaron valores nulos.
  - ✅ No hay filas completamente duplicadas.
- **Estadísticas Numéricas (Min, Max, Promedio):**
```text
      codigo_pedido  codigo_cliente
min             1.0            1.00
max            20.0           20.00
mean           10.5           10.45
```
- **Valores Únicos en Columnas de Texto (Top 5):**
  - `fecha_pedido`: 20 valores únicos. Ej: 2025-04-13, 2025-09-05, 2025-12-02, 2025-07-26, 2025-07-06...
  - `fecha_esperada`: 19 valores únicos. Ej: 2025-06-22, 2026-01-03, 2025-12-05, 2025-12-17, 2025-10-31...
  - `fecha_entrega`: 19 valores únicos. Ej: 2025-11-17, 2025-09-24, 2025-12-15, 2025-10-09, 2025-07-17...
  - `estado`: 4 valores únicos. Ej: Rechazado, En tránsito, Entregado, Pendiente...
  - `comentarios`: 20 valores únicos. Ej: Sean uno fuerte suelo todas., Visto señora contenido hermano este., Juez efectos autoridades sol favor aquí temas hijos., Ocasión tiene septiembre dirección ese organización grado., Aún habla gobierno objetivo fondo pequeño....

---
## Tabla: producto
- **Dimensiones:** 20 filas x 9 columnas
- **Estructura y Tipos de Datos:**
```text
["<class 'pandas.core.frame.DataFrame'>", 'RangeIndex: 20 entries, 0 to 19', 'Data columns (total 9 columns):', ' #   Column             Non-Null Count  Dtype  ', '---  ------             --------------  -----  ', ' 0   codigo_producto    20 non-null     object ', ' 1   nombre             20 non-null     object ', ' 2   gama               20 non-null     object ', ' 3   dimensiones        20 non-null     object ', ' 4   proveedor          20 non-null     object ', ' 5   descripcion        20 non-null     object ', ' 6   cantidad_en_stock  20 non-null     int64  ', ' 7   precio_venta       20 non-null     float64', ' 8   precio_proveedor   20 non-null     float64']
```
- **Ejemplo de Datos (Primeras 3 filas):**
```text
codigo_producto nombre    gama dimensiones                   proveedor                                        descripcion  cantidad_en_stock  precio_venta  precio_proveedor
      PROD-0001  Texto Campaña    10x20x30            Hnos Pineda S.L.            Mismos afirmó ellos niño visita estilo.                 18    411.102171        146.272207
      PROD-0002  Igual   Riego    10x20x30 Fernández y asociados S.A.D Creación existen lado sector imposible ésta pesar.                316    482.747456        124.189258
      PROD-0003    Sus    Ocho    10x20x30      Calatayud y Páez S.A.U               Cuba pasar él chile tampoco siempre.                391    108.346439        248.177523
```
- **Análisis de Calidad:**
  - ✅ No se detectaron valores nulos.
  - ✅ No hay filas completamente duplicadas.
- **Estadísticas Numéricas (Min, Max, Promedio):**
```text
      cantidad_en_stock  precio_venta  precio_proveedor
min               18.00     27.265597         11.184260
max              464.00    499.116988        289.123915
mean             263.85    224.086509        154.983838
```
- **Valores Únicos en Columnas de Texto (Top 5):**
  - `codigo_producto`: 20 valores únicos. Ej: PROD-0001, PROD-0002, PROD-0003, PROD-0004, PROD-0005...
  - `nombre`: 20 valores únicos. Ej: Texto, Igual, Sus, Etapa, Porque...
  - `gama`: 11 valores únicos. Ej: Campaña, Riego, Ocho, Única, Nuevas...
  - `dimensiones`: 1 valores únicos. Ej: 10x20x30...
  - `proveedor`: 20 valores únicos. Ej: Hnos Pineda S.L., Fernández y asociados S.A.D, Calatayud y Páez S.A.U, Díez y asociados S.L.N.E, Manufacturas Acosta y asociados S.L....
  - `descripcion`: 20 valores únicos. Ej: Mismos afirmó ellos niño visita estilo., Creación existen lado sector imposible ésta pesar., Cuba pasar él chile tampoco siempre., Mayores eran elementos antonio., Tomar diversas grupos color sol pasó....

---
## Tabla: detalle_pedido
- **Dimensiones:** 61 filas x 5 columnas
- **Estructura y Tipos de Datos:**
```text
["<class 'pandas.core.frame.DataFrame'>", 'RangeIndex: 61 entries, 0 to 60', 'Data columns (total 5 columns):', ' #   Column           Non-Null Count  Dtype  ', '---  ------           --------------  -----  ', ' 0   codigo_pedido    61 non-null     int64  ', ' 1   codigo_producto  61 non-null     object ', ' 2   cantidad         61 non-null     int64  ', ' 3   precio_unidad    61 non-null     float64', ' 4   numero_linea     61 non-null     int64  ']
```
- **Ejemplo de Datos (Primeras 3 filas):**
```text
 codigo_pedido codigo_producto  cantidad  precio_unidad  numero_linea
             1       PROD-0008         1      77.398704             1
             1       PROD-0015         3      81.734463             2
             1       PROD-0013         5      88.962936             3
```
- **Análisis de Calidad:**
  - ✅ No se detectaron valores nulos.
  - ✅ No hay filas completamente duplicadas.
- **Estadísticas Numéricas (Min, Max, Promedio):**
```text
      codigo_pedido   cantidad  precio_unidad  numero_linea
min        1.000000   1.000000      10.155737      1.000000
max       20.000000  20.000000      99.854390      5.000000
mean      10.819672  10.278689      55.296378      2.295082
```
- **Valores Únicos en Columnas de Texto (Top 5):**
  - `codigo_producto`: 20 valores únicos. Ej: PROD-0008, PROD-0015, PROD-0013, PROD-0018, PROD-0004...

---
## Tabla: pago
- **Dimensiones:** 20 filas x 5 columnas
- **Estructura y Tipos de Datos:**
```text
["<class 'pandas.core.frame.DataFrame'>", 'RangeIndex: 20 entries, 0 to 19', 'Data columns (total 5 columns):', ' #   Column          Non-Null Count  Dtype  ', '---  ------          --------------  -----  ', ' 0   id_transaccion  20 non-null     object ', ' 1   codigo_cliente  20 non-null     int64  ', ' 2   forma_pago      20 non-null     object ', ' 3   fecha_pago      20 non-null     object ', ' 4   total           20 non-null     float64']
```
- **Ejemplo de Datos (Primeras 3 filas):**
```text
                      id_transaccion  codigo_cliente    forma_pago fecha_pago       total
c15f4d7a-2c6c-484e-a240-f676c8a022a7              20       Tarjeta 2025-03-31 3839.951029
982706f8-60c8-4dcf-b280-54d58fe9d07f               3 Transferencia 2025-08-22 1367.074575
f4bc22a1-8d5c-44a8-9c45-e07f421c3e5b               5       Tarjeta 2025-05-03  582.611003
```
- **Análisis de Calidad:**
  - ✅ No se detectaron valores nulos.
  - ✅ No hay filas completamente duplicadas.
- **Estadísticas Numéricas (Min, Max, Promedio):**
```text
      codigo_cliente        total
min             3.00   177.196520
max            20.00  4468.022662
mean           11.55  1860.818268
```
- **Valores Únicos en Columnas de Texto (Top 5):**
  - `id_transaccion`: 20 valores únicos. Ej: c15f4d7a-2c6c-484e-a240-f676c8a022a7, 982706f8-60c8-4dcf-b280-54d58fe9d07f, f4bc22a1-8d5c-44a8-9c45-e07f421c3e5b, de8ea75b-9114-4517-a4fc-2c114876d349, b6319ec0-fc6f-433f-93a9-ed44004192df...
  - `forma_pago`: 4 valores únicos. Ej: Tarjeta, Transferencia, Cheque, PayPal...
  - `fecha_pago`: 19 valores únicos. Ej: 2025-03-31, 2025-08-22, 2025-05-03, 2025-02-09, 2024-12-29...

---
## Análisis de Relaciones
- **Columnas Comunes (Posibles Claves Foráneas):**
  - codigo_oficina, ciudad, pais, region, codigo_postal, telefono, linea_direccion1, linea_direccion2, nombre, gama, codigo_cliente, codigo_pedido, codigo_producto
## Análisis de Patrones Específicos
- **Proveedores Identificados (20):**
  - Hnos Pineda S.L., Fernández y asociados S.A.D, Calatayud y Páez S.A.U, Díez y asociados S.L.N.E, Manufacturas Acosta y asociados S.L., Juan Francisco Calleja Tello S.A., Industrias Montalbán S.L., Hermanos Trillo S.A., Manufacturas Garay S.A., Vilanova y Agustí S.A. ...
- **Colores:** No se detectó columna 'color' ni menciones obvias en descripciones.