================================================================================
INICIO DEL ANÁLISIS EXPLORATORIO DE DATOS (EDA)
================================================================================

--- Archivo: case-accessory.csv ---
1. Análisis Básico:
   - Dimensiones: 8 filas, 4 columnas
   - Filas duplicadas: 0
   - Ejemplo de datos (primeras 3 filas):
                          name  price            type  form_factor
0  NZXT HUE 2 RGB Lighting Kit    NaN  LED Controller         2.50
1                    NZXT Hue+    NaN  LED Controller         2.50
2                     NZXT Hue  29.95  LED Controller         5.25

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 8
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 7 (87.50%)
     - Valores únicos: 1
     - Rango numérico: Min=29.95, Max=29.95, Promedio=29.95
   - Columna: 'type'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 2
   - Columna: 'form_factor'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 3
     - Rango numérico: Min=2.50, Max=5.25, Promedio=4.34

--- Archivo: case-fan.csv ---
1. Análisis Básico:
   - Dimensiones: 2181 filas, 8 columnas
   - Filas duplicadas: 136
   - Ejemplo de datos (primeras 3 filas):
                                      name  price  size          color       rpm airflow noise_level   pwm
0      Corsair iCUE SP120 RGB ELITE 3-Pack  69.98   120  Black / White  400,1500     NaN         NaN  True
1       Lian Li Uni Fan SL-Infinity 3-Pack  84.99   120          Black       NaN  0,61.3        0,29  True
2  Noctua NF-A12x25 PWM chromax.black.swap  34.95   120          Black  450,2000   60.09        22.6  True

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 1164
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 1263 (57.91%)
     - Valores únicos: 451
     - Rango numérico: Min=4.49, Max=156.99, Promedio=31.18
   - Columna: 'size'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 15
     - Rango numérico: Min=40.00, Max=230.00, Promedio=122.87
   - Columna: 'color'
     - Tipo: object
     - Nulos: 21 (0.96%)
     - Valores únicos: 61
   - Columna: 'rpm'
     - Tipo: object
     - Nulos: 58 (2.66%)
     - Valores únicos: 273
   - Columna: 'airflow'
     - Tipo: object
     - Nulos: 91 (4.17%)
     - Valores únicos: 826
   - Columna: 'noise_level'
     - Tipo: object
     - Nulos: 134 (6.14%)
     - Valores únicos: 548
   - Columna: 'pwm'
     - Tipo: bool
     - Nulos: 0 (0.00%)
     - Valores únicos: 2
     - Rango numérico: Min=0.00, Max=1.00, Promedio=0.49

--- Archivo: case.csv ---
1. Análisis Básico:
   - Dimensiones: 5486 filas, 8 columnas
   - Filas duplicadas: 174
   - Ejemplo de datos (primeras 3 filas):
                    name  price           type  color  psu             side_panel  external_volume  internal_35_bays
0  Corsair 4000D Airflow  94.99  ATX Mid Tower  Black  NaN  Tinted Tempered Glass             48.6                 2
1         Deepcool CC560  63.98  ATX Mid Tower  Black  NaN         Tempered Glass             41.7                 2
2           NZXT H5 Flow  79.98  ATX Mid Tower  Black  NaN         Tempered Glass             47.0                 1

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 3565
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 4446 (81.04%)
     - Valores únicos: 538
     - Rango numérico: Min=29.99, Max=899.99, Promedio=145.91
   - Columna: 'type'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 13
   - Columna: 'color'
     - Tipo: object
     - Nulos: 35 (0.64%)
     - Valores únicos: 82
   - Columna: 'psu'
     - Tipo: float64
     - Nulos: 4975 (90.69%)
     - Valores únicos: 41
     - Rango numérico: Min=60.00, Max=1350.00, Promedio=393.02
   - Columna: 'side_panel'
     - Tipo: object
     - Nulos: 1952 (35.58%)
     - Valores únicos: 5
   - Columna: 'external_volume'
     - Tipo: float64
     - Nulos: 1434 (26.14%)
     - Valores únicos: 694
     - Rango numérico: Min=2.90, Max=257.30, Promedio=44.12
   - Columna: 'internal_35_bays'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 16
     - Rango numérico: Min=0.00, Max=20.00, Promedio=3.21

--- Archivo: cpu-cooler.csv ---
1. Análisis Básico:
   - Dimensiones: 2166 filas, 6 columnas
   - Filas duplicadas: 15
   - Ejemplo de datos (primeras 3 filas):
                                       name  price       rpm noise_level  color   size
0     Cooler Master Hyper 212 Black Edition  36.99  800,2000      6.5,26    NaN    NaN
1  Cooler Master MASTERLIQUID ML240L RGB V2  99.47  650,1800        6,27  Black  240.0
2                 be quiet! Dark Rock Pro 4  69.90      1500   12.8,24.3  Black    NaN

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 1890
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 1347 (62.19%)
     - Valores únicos: 489
     - Rango numérico: Min=8.16, Max=697.50, Promedio=108.25
   - Columna: 'rpm'
     - Tipo: object
     - Nulos: 117 (5.40%)
     - Valores únicos: 274
   - Columna: 'noise_level'
     - Tipo: object
     - Nulos: 206 (9.51%)
     - Valores únicos: 609
   - Columna: 'color'
     - Tipo: object
     - Nulos: 916 (42.29%)
     - Valores únicos: 48
   - Columna: 'size'
     - Tipo: float64
     - Nulos: 1290 (59.56%)
     - Valores únicos: 6
     - Rango numérico: Min=120.00, Max=420.00, Promedio=261.69

--- Archivo: cpu.csv ---
1. Análisis Básico:
   - Dimensiones: 1353 filas, 8 columnas
   - Filas duplicadas: 194
   - Ejemplo de datos (primeras 3 filas):
                   name   price  core_count  core_clock  boost_clock  tdp                graphics   smt
0   AMD Ryzen 7 7800X3D  389.00           8         4.2          5.0  120                  Radeon  True
1     AMD Ryzen 5 5600X  147.72           6         3.7          4.6   65                     NaN  True
2  Intel Core i7-13700K  364.99          16         3.4          5.4  125  Intel UHD Graphics 770  True

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 907
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 754 (55.73%)
     - Valores únicos: 470
     - Rango numérico: Min=14.00, Max=4355.00, Promedio=283.03
   - Columna: 'core_count'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 16
     - Rango numérico: Min=1.00, Max=64.00, Promedio=5.22
   - Columna: 'core_clock'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 50
     - Rango numérico: Min=1.10, Max=4.70, Promedio=3.11
   - Columna: 'boost_clock'
     - Tipo: float64
     - Nulos: 683 (50.48%)
     - Valores únicos: 38
     - Rango numérico: Min=2.10, Max=6.00, Promedio=4.10
   - Columna: 'tdp'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 51
     - Rango numérico: Min=20.00, Max=280.00, Promedio=84.35
   - Columna: 'graphics'
     - Tipo: object
     - Nulos: 773 (57.13%)
     - Valores únicos: 47
   - Columna: 'smt'
     - Tipo: bool
     - Nulos: 0 (0.00%)
     - Valores únicos: 2
     - Rango numérico: Min=0.00, Max=1.00, Promedio=0.45

--- Archivo: external-hard-drive.csv ---
1. Análisis Básico:
   - Dimensiones: 519 filas, 7 columnas
   - Filas duplicadas: 46
   - Ejemplo de datos (primeras 3 filas):
                          name    price     type                                   interface  capacity  price_per_gb  color
0  Western Digital My Book Duo  1049.99  Desktop  USB Type-A 3.2 Gen 1, USB Type-C 3.2 Gen 1     36000         0.029  Black
1  Western Digital My Book Duo   829.99  Desktop  USB Type-A 3.2 Gen 1, USB Type-C 3.2 Gen 1     24000         0.035  Black
2          Toshiba Canvio Desk      NaN  Desktop                        USB Type-A 3.2 Gen 1      3000           NaN    NaN

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 150
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 301 (58.00%)
     - Valores únicos: 154
     - Rango numérico: Min=27.14, Max=1049.99, Promedio=181.98
   - Columna: 'type'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 2
   - Columna: 'interface'
     - Tipo: object
     - Nulos: 10 (1.93%)
     - Valores únicos: 20
   - Columna: 'capacity'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 30
     - Rango numérico: Min=120.00, Max=36000.00, Promedio=2973.11
   - Columna: 'price_per_gb'
     - Tipo: float64
     - Nulos: 301 (58.00%)
     - Valores únicos: 105
     - Rango numérico: Min=0.01, Max=3.77, Promedio=0.12
   - Columna: 'color'
     - Tipo: object
     - Nulos: 278 (53.56%)
     - Valores únicos: 15

--- Archivo: fan-controller.csv ---
1. Análisis Básico:
   - Dimensiones: 37 filas, 7 columnas
   - Filas duplicadas: 0
   - Ejemplo de datos (primeras 3 filas):
                       name   price  channels  channel_wattage    pwm form_factor color
0         NZXT Sentry Mix 2  199.95         6             30.0   True        5.25   NaN
1  Thermaltake Commander FT   44.91         5             10.0   True        5.25   NaN
2           Kingwin FPX-001   15.99         4              8.0  False         3.5   NaN

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 37
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 33 (89.19%)
     - Valores únicos: 4
     - Rango numérico: Min=15.99, Max=199.95, Promedio=82.70
   - Columna: 'channels'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 4
     - Rango numérico: Min=1.00, Max=6.00, Promedio=4.86
   - Columna: 'channel_wattage'
     - Tipo: float64
     - Nulos: 2 (5.41%)
     - Valores únicos: 14
     - Rango numérico: Min=0.01, Max=60.00, Promedio=22.69
   - Columna: 'pwm'
     - Tipo: bool
     - Nulos: 0 (0.00%)
     - Valores únicos: 2
     - Rango numérico: Min=0.00, Max=1.00, Promedio=0.54
   - Columna: 'form_factor'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 3
   - Columna: 'color'
     - Tipo: object
     - Nulos: 33 (89.19%)
     - Valores únicos: 1

--- Archivo: headphones.csv ---
1. Análisis Básico:
   - Dimensiones: 2746 filas, 8 columnas
   - Filas duplicadas: 36
   - Ejemplo de datos (primeras 3 filas):
                    name    price         type frequency_response  microphone  wireless enclosure_type           color
0        HiFiMAN Susvara  5999.00  Circumaural               6,75       False     False           Open  Silver / Brown
1     HP HyperX Cloud II    77.98  Circumaural              15,25        True     False         Closed     Black / Red
2  Razer BlackShark V2 X    49.99  Circumaural              12,28        True     False         Closed   Black / Green

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 2406
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 2075 (75.56%)
     - Valores únicos: 414
     - Rango numérico: Min=3.99, Max=5999.00, Promedio=147.95
   - Columna: 'type'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 4
   - Columna: 'frequency_response'
     - Tipo: object
     - Nulos: 592 (21.56%)
     - Valores únicos: 199
   - Columna: 'microphone'
     - Tipo: bool
     - Nulos: 0 (0.00%)
     - Valores únicos: 2
     - Rango numérico: Min=0.00, Max=1.00, Promedio=0.50
   - Columna: 'wireless'
     - Tipo: bool
     - Nulos: 0 (0.00%)
     - Valores únicos: 2
     - Rango numérico: Min=0.00, Max=1.00, Promedio=0.13
   - Columna: 'enclosure_type'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 3
   - Columna: 'color'
     - Tipo: object
     - Nulos: 14 (0.51%)
     - Valores únicos: 88

--- Archivo: internal-hard-drive.csv ---
1. Análisis Básico:
   - Dimensiones: 5705 filas, 8 columnas
   - Filas duplicadas: 458
   - Ejemplo de datos (primeras 3 filas):
                   name   price  capacity  price_per_gb type   cache form_factor        interface
0       Samsung 980 Pro  129.99    2000.0         0.065  SSD  2048.0    M.2-2280  M.2 PCIe 4.0 X4
1  Samsung 970 Evo Plus   89.99    1000.0         0.090  SSD  1024.0    M.2-2280  M.2 PCIe 3.0 X4
2       Samsung 990 Pro  129.87    2000.0         0.065  SSD  2048.0    M.2-2280  M.2 PCIe 4.0 X4

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 1652
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 3541 (62.07%)
     - Valores únicos: 1194
     - Rango numérico: Min=12.64, Max=3187.50, Promedio=167.75
   - Columna: 'capacity'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 89
     - Rango numérico: Min=8.00, Max=22000.00, Promedio=1790.04
   - Columna: 'price_per_gb'
     - Tipo: float64
     - Nulos: 3541 (62.07%)
     - Valores únicos: 469
     - Rango numérico: Min=0.01, Max=6.49, Promedio=0.19
   - Columna: 'type'
     - Tipo: object
     - Nulos: 30 (0.53%)
     - Valores únicos: 13
   - Columna: 'cache'
     - Tipo: float64
     - Nulos: 3839 (67.29%)
     - Valores únicos: 15
     - Rango numérico: Min=2.00, Max=131072.00, Promedio=343.60
   - Columna: 'form_factor'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 9
   - Columna: 'interface'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 22

--- Archivo: keyboard.csv ---
1. Análisis Básico:
   - Dimensiones: 2970 filas, 8 columnas
   - Filas duplicadas: 142
   - Ejemplo de datos (primeras 3 filas):
                       name   price   style      switches backlit  tenkeyless connection_type  color
0       Corsair K60 RGB Pro   71.99  Gaming  Cherry Viola     RGB       False           Wired  Black
1  HP HyperX Alloy Core RGB   49.99  Gaming           NaN     RGB       False           Wired  Black
2             Logitech G19s  699.06  Gaming           NaN     NaN       False           Wired  Black

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 2084
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 2304 (77.58%)
     - Valores únicos: 379
     - Rango numérico: Min=7.95, Max=769.95, Promedio=106.28
   - Columna: 'style'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 6
   - Columna: 'switches'
     - Tipo: object
     - Nulos: 1285 (43.27%)
     - Valores únicos: 176
   - Columna: 'backlit'
     - Tipo: object
     - Nulos: 1408 (47.41%)
     - Valores únicos: 11
   - Columna: 'tenkeyless'
     - Tipo: bool
     - Nulos: 0 (0.00%)
     - Valores únicos: 2
     - Rango numérico: Min=0.00, Max=1.00, Promedio=0.30
   - Columna: 'connection_type'
     - Tipo: object
     - Nulos: 3 (0.10%)
     - Valores únicos: 9
   - Columna: 'color'
     - Tipo: object
     - Nulos: 15 (0.51%)
     - Valores únicos: 48

--- Archivo: memory.csv ---
1. Análisis Básico:
   - Dimensiones: 11734 filas, 8 columnas
   - Filas duplicadas: 794
   - Ejemplo de datos (primeras 3 filas):
                              name   price   speed modules  price_per_gb           color  first_word_latency  cas_latency
0      Corsair Vengeance LPX 16 GB   41.99  4,3200     2,8         2.624  Black / Yellow              10.000         16.0
1          Corsair Vengeance 32 GB  104.99  5,5600    2,16         3.281           Black              12.857         36.0
2  Corsair Vengeance RGB Pro 32 GB   94.99  4,3600    2,16         2.968           Black              10.000         18.0

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 3171
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 8719 (74.31%)
     - Valores únicos: 1331
     - Rango numérico: Min=7.09, Max=1674.47, Promedio=127.41
   - Columna: 'speed'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 79
   - Columna: 'modules'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 39
   - Columna: 'price_per_gb'
     - Tipo: float64
     - Nulos: 8719 (74.31%)
     - Valores únicos: 1316
     - Rango numérico: Min=0.79, Max=91.12, Promedio=5.06
   - Columna: 'color'
     - Tipo: object
     - Nulos: 632 (5.39%)
     - Valores únicos: 63
   - Columna: 'first_word_latency'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 174
     - Rango numérico: Min=6.00, Max=19.17, Promedio=11.45
   - Columna: 'cas_latency'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 32
     - Rango numérico: Min=2.50, Max=52.00, Promedio=16.86

--- Archivo: monitor.csv ---
1. Análisis Básico:
   - Dimensiones: 4216 filas, 8 columnas
   - Filas duplicadas: 69
   - Ejemplo de datos (primeras 3 filas):
                     name    price  screen_size resolution  refresh_rate  response_time panel_type aspect_ratio
0  Asus TUF Gaming VG27AQ   283.99         27.0  2560,1440         165.0            1.0        IPS         16:9
1             LG 65EP5G-B  8875.00         65.0  3840,2160         120.0            0.1       OLED         16:9
2           Gigabyte G27Q   219.99         27.0  2560,1440         144.0            NaN        IPS         16:9

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 4031
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 3000 (71.16%)
     - Valores únicos: 704
     - Rango numérico: Min=69.00, Max=8875.00, Promedio=437.98
   - Columna: 'screen_size'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 79
     - Rango numérico: Min=14.00, Max=65.00, Promedio=25.80
   - Columna: 'resolution'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 31
   - Columna: 'refresh_rate'
     - Tipo: float64
     - Nulos: 857 (20.33%)
     - Valores únicos: 37
     - Rango numérico: Min=30.00, Max=540.00, Promedio=96.86
   - Columna: 'response_time'
     - Tipo: float64
     - Nulos: 687 (16.30%)
     - Valores únicos: 32
     - Rango numérico: Min=0.01, Max=25.00, Promedio=4.74
   - Columna: 'panel_type'
     - Tipo: object
     - Nulos: 762 (18.07%)
     - Valores únicos: 12
   - Columna: 'aspect_ratio'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 15

--- Archivo: motherboard.csv ---
1. Análisis Básico:
   - Dimensiones: 4358 filas, 7 columnas
   - Filas duplicadas: 0
   - Ejemplo de datos (primeras 3 filas):
                           name   price   socket form_factor  max_memory  memory_slots           color
0          MSI B550 GAMING GEN3   99.99      AM4         ATX         128             4           Black
1  Gigabyte B650 AORUS ELITE AX  189.99      AM5         ATX         192             4  Black / Silver
2  Gigabyte Z790 AORUS ELITE AX  239.99  LGA1700         ATX         192             4           Black

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 4344
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 3627 (83.23%)
     - Valores únicos: 492
     - Rango numérico: Min=63.65, Max=2591.77, Promedio=276.61
   - Columna: 'socket'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 61
   - Columna: 'form_factor'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 11
   - Columna: 'max_memory'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 15
     - Rango numérico: Min=2.00, Max=2048.00, Promedio=71.70
   - Columna: 'memory_slots'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 7
     - Rango numérico: Min=1.00, Max=16.00, Promedio=3.62
   - Columna: 'color'
     - Tipo: object
     - Nulos: 300 (6.88%)
     - Valores únicos: 60

--- Archivo: mouse.csv ---
1. Análisis Básico:
   - Dimensiones: 2355 filas, 7 columnas
   - Filas duplicadas: 27
   - Ejemplo de datos (primeras 3 filas):
                          name   price tracking_method connection_type  max_dpi hand_orientation  color
0           Logitech G502 HERO   35.99         Optical           Wired  25600.0            Right  Black
1  Logitech G Pro X Superlight  109.99         Optical        Wireless  25400.0            Right  Black
2        Logitech G305 (Black)   37.53         Optical        Wireless  12000.0            Right  Black

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 1881
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 1582 (67.18%)
     - Valores únicos: 438
     - Rango numérico: Min=4.99, Max=589.97, Promedio=60.47
   - Columna: 'tracking_method'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 4
   - Columna: 'connection_type'
     - Tipo: object
     - Nulos: 5 (0.21%)
     - Valores únicos: 9
   - Columna: 'max_dpi'
     - Tipo: float64
     - Nulos: 601 (25.52%)
     - Valores únicos: 65
     - Rango numérico: Min=400.00, Max=36000.00, Promedio=6598.40
   - Columna: 'hand_orientation'
     - Tipo: object
     - Nulos: 129 (5.48%)
     - Valores únicos: 3
   - Columna: 'color'
     - Tipo: object
     - Nulos: 4 (0.17%)
     - Valores únicos: 86

--- Archivo: optical-drive.csv ---
1. Análisis Básico:
   - Dimensiones: 227 filas, 8 columnas
   - Filas duplicadas: 0
   - Ejemplo de datos (primeras 3 filas):
                       name  price    bd   dvd    cd   bd_write           dvd_write cd_write
0               LG WH14NS40  69.99  12.0  16.0  48.0  14/12/2/2     16/8/8/16/6/8/5    48/24
1  Asus DRW-24B1ST/BLK/B/AS  24.99   NaN  16.0  48.0        NaN  24/8/12/24/6/12/12    48/32
2               LG WH16NS40  59.99  12.0  16.0  48.0  16/12/2/2     16/8/8/16/6/8/5    48/24

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 227
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 191 (84.14%)
     - Valores únicos: 33
     - Rango numérico: Min=21.99, Max=213.04, Promedio=67.15
   - Columna: 'bd'
     - Tipo: float64
     - Nulos: 154 (67.84%)
     - Valores únicos: 6
     - Rango numérico: Min=4.00, Max=16.00, Promedio=9.10
   - Columna: 'dvd'
     - Tipo: float64
     - Nulos: 26 (11.45%)
     - Valores únicos: 7
     - Rango numérico: Min=5.00, Max=22.00, Promedio=14.64
   - Columna: 'cd'
     - Tipo: float64
     - Nulos: 25 (11.01%)
     - Valores únicos: 5
     - Rango numérico: Min=24.00, Max=50.00, Promedio=42.62
   - Columna: 'bd_write'
     - Tipo: object
     - Nulos: 172 (75.77%)
     - Valores únicos: 25
   - Columna: 'dvd_write'
     - Tipo: object
     - Nulos: 25 (11.01%)
     - Valores únicos: 61
   - Columna: 'cd_write'
     - Tipo: object
     - Nulos: 28 (12.33%)
     - Valores únicos: 16

--- Archivo: os.csv ---
1. Análisis Básico:
   - Dimensiones: 62 filas, 4 columnas
   - Filas duplicadas: 25
   - Ejemplo de datos (primeras 3 filas):
                                 name   price mode  max_memory
0  Microsoft Windows 11 Home (64-bit)  121.98   64         128
1  Microsoft Windows 10 Home (64-bit)     NaN   64         128
2   Microsoft Windows 11 Pro (64-bit)  149.99   64        2048

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 32
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 52 (83.87%)
     - Valores únicos: 10
     - Rango numérico: Min=121.98, Max=253.15, Promedio=179.01
   - Columna: 'mode'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 3
   - Columna: 'max_memory'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 6
     - Rango numérico: Min=4.00, Max=2048.00, Promedio=418.13

--- Archivo: power-supply.csv ---
1. Análisis Básico:
   - Dimensiones: 2805 filas, 7 columnas
   - Filas duplicadas: 64
   - Ejemplo de datos (primeras 3 filas):
                    name   price type efficiency  wattage modular  color
0  Corsair RM750e (2023)   96.99  ATX       gold      750    Full  Black
1  Corsair RM850x (2021)  131.72  ATX       gold      850    Full  Black
2  Corsair RM850e (2023)  114.99  ATX       gold      850    Full  Black

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 1768
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 2139 (76.26%)
     - Valores únicos: 423
     - Rango numérico: Min=16.98, Max=799.00, Promedio=176.72
   - Columna: 'type'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 5
   - Columna: 'efficiency'
     - Tipo: object
     - Nulos: 360 (12.83%)
     - Valores únicos: 6
   - Columna: 'wattage'
     - Tipo: int64
     - Nulos: 0 (0.00%)
     - Valores únicos: 81
     - Rango numérico: Min=200.00, Max=2050.00, Promedio=721.87
   - Columna: 'modular'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 4
   - Columna: 'color'
     - Tipo: object
     - Nulos: 1640 (58.47%)
     - Valores únicos: 23

--- Archivo: sound-card.csv ---
1. Análisis Básico:
   - Dimensiones: 77 filas, 8 columnas
   - Filas duplicadas: 1
   - Ejemplo de datos (primeras 3 filas):
                                     name   price  channels  digital_audio    snr  sample_rate        chipset interface
0        Creative Labs Sound Blaster AE-9  332.49       7.1           32.0  129.0        384.0   Sound Core3D   PCIe x1
1  Creative Labs Sound BlasterX AE-5 Plus  142.49       5.1           32.0  122.0        384.0   Sound Core3D   PCIe x1
2   Creative Labs Sound Blaster Audigy Rx   55.23       7.1           24.0  106.0        192.0  Creative E-MU   PCIe x1

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 75
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 63 (81.82%)
     - Valores únicos: 13
     - Rango numérico: Min=38.99, Max=332.49, Promedio=137.12
   - Columna: 'channels'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 4
     - Rango numérico: Min=2.00, Max=7.10, Promedio=5.90
   - Columna: 'digital_audio'
     - Tipo: float64
     - Nulos: 6 (7.79%)
     - Valores únicos: 3
     - Rango numérico: Min=16.00, Max=32.00, Promedio=24.00
   - Columna: 'snr'
     - Tipo: float64
     - Nulos: 23 (29.87%)
     - Valores únicos: 20
     - Rango numérico: Min=68.00, Max=129.00, Promedio=112.22
   - Columna: 'sample_rate'
     - Tipo: float64
     - Nulos: 6 (7.79%)
     - Valores únicos: 5
     - Rango numérico: Min=44.10, Max=384.00, Promedio=166.25
   - Columna: 'chipset'
     - Tipo: object
     - Nulos: 33 (42.86%)
     - Valores únicos: 15
   - Columna: 'interface'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 2

--- Archivo: speakers.csv ---
1. Análisis Básico:
   - Dimensiones: 268 filas, 6 columnas
   - Filas duplicadas: 0
   - Ejemplo de datos (primeras 3 filas):
                       name   price  configuration  wattage frequency_response  color
0                 KEF LSXBL  945.20            2.0    200.0              49,47  Black
1             Logitech Z200   39.99            2.0     10.0              20,20    NaN
2  Creative Labs Pebble 2.0   19.99            2.0      4.4             100,17  Black

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 259
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 159 (59.33%)
     - Valores únicos: 66
     - Rango numérico: Min=13.50, Max=945.20, Promedio=218.45
   - Columna: 'configuration'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 4
     - Rango numérico: Min=1.00, Max=5.10, Promedio=2.17
   - Columna: 'wattage'
     - Tipo: float64
     - Nulos: 38 (14.18%)
     - Valores únicos: 80
     - Rango numérico: Min=0.01, Max=550.00, Promedio=77.03
   - Columna: 'frequency_response'
     - Tipo: object
     - Nulos: 26 (9.70%)
     - Valores únicos: 74
   - Columna: 'color'
     - Tipo: object
     - Nulos: 153 (57.09%)
     - Valores únicos: 20

--- Archivo: thermal-paste.csv ---
1. Análisis Básico:
   - Dimensiones: 149 filas, 3 columnas
   - Filas duplicadas: 3
   - Ejemplo de datos (primeras 3 filas):
                                                name   price  amount
0  Arctic Silver 5 High-Density Polysynthetic Silver    6.97     3.5
1                           Thermal Grizzly Kryonaut    8.99     1.0
2                                Prolimatech PK-Zero  157.32   600.0

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 101
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 82 (55.03%)
     - Valores únicos: 61
     - Rango numérico: Min=4.29, Max=157.32, Promedio=20.31
   - Columna: 'amount'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 37
     - Rango numérico: Min=0.01, Max=600.00, Promedio=14.74

--- Archivo: ups.csv ---
1. Análisis Básico:
   - Dimensiones: 683 filas, 4 columnas
   - Filas duplicadas: 0
   - Ejemplo de datos (primeras 3 filas):
                      name     price  capacity_w  capacity_va
0         APC SURT20KRMXLT  19850.00     16000.0      20000.0
1  CyberPower CP1500PFCLCD    219.95      1000.0       1500.0
2          APC SRT10KRMXLT   7975.00     10000.0      10000.0

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 682
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 358 (52.42%)
     - Valores únicos: 307
     - Rango numérico: Min=53.95, Max=19850.00, Promedio=1395.62
   - Columna: 'capacity_w'
     - Tipo: float64
     - Nulos: 3 (0.44%)
     - Valores únicos: 109
     - Rango numérico: Min=16.00, Max=16000.00, Promedio=1448.62
   - Columna: 'capacity_va'
     - Tipo: float64
     - Nulos: 3 (0.44%)
     - Valores únicos: 55
     - Rango numérico: Min=125.00, Max=20000.00, Promedio=1877.59

--- Archivo: video-card.csv ---
1. Análisis Básico:
   - Dimensiones: 5811 filas, 8 columnas
   - Filas duplicadas: 68
   - Ejemplo de datos (primeras 3 filas):
                                 name   price                chipset  memory  core_clock  boost_clock  color  length
0  MSI GeForce RTX 3060 Ventus 2X 12G  289.24  GeForce RTX 3060 12GB    12.0      1320.0       1777.0  Black   235.0
1               Gigabyte WINDFORCE OC  549.99       GeForce RTX 4070    12.0      1920.0       2490.0  Black   261.0
2                  Gigabyte GAMING OC  499.99      Radeon RX 7800 XT    16.0      1295.0       2565.0  Black   302.0

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 3367
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 4783 (82.31%)
     - Valores únicos: 680
     - Rango numérico: Min=34.99, Max=8562.99, Promedio=682.42
   - Columna: 'chipset'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 343
   - Columna: 'memory'
     - Tipo: float64
     - Nulos: 0 (0.00%)
     - Valores únicos: 24
     - Rango numérico: Min=0.12, Max=48.00, Promedio=5.98
   - Columna: 'core_clock'
     - Tipo: float64
     - Nulos: 121 (2.08%)
     - Valores únicos: 403
     - Rango numérico: Min=115.00, Max=2670.00, Promedio=1258.53
   - Columna: 'boost_clock'
     - Tipo: float64
     - Nulos: 2405 (41.39%)
     - Valores únicos: 360
     - Rango numérico: Min=720.00, Max=2855.00, Promedio=1738.37
   - Columna: 'color'
     - Tipo: object
     - Nulos: 286 (4.92%)
     - Valores únicos: 66
   - Columna: 'length'
     - Tipo: float64
     - Nulos: 660 (11.36%)
     - Valores únicos: 216
     - Rango numérico: Min=69.00, Max=360.00, Promedio=249.47

--- Archivo: webcam.csv ---
1. Análisis Básico:
   - Dimensiones: 65 filas, 7 columnas
   - Filas duplicadas: 0
   - Ejemplo de datos (primeras 3 filas):
                         name   price            resolutions            connection focus_type                     os   fov
0  Logitech BRIO Ultra HD Pro  123.00          4k,1080p,720p  USB 3.2 Gen 1 Type-A       Auto  Windows,OS X,ChromeOS  82.0
1      Insta360 Insta360 Link  254.99          4k,1080p,720p        USB 2.0 Type-C       Auto           Windows,OS X  79.5
2               OBSBOT Tiny 2  329.00  4k,2k,1080p,720p,480p  USB 3.2 Gen 1 Type-A       Auto           Windows,OS X  85.5

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 64
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 14 (21.54%)
     - Valores únicos: 44
     - Rango numérico: Min=9.99, Max=329.00, Promedio=92.71
   - Columna: 'resolutions'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 12
   - Columna: 'connection'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 4
   - Columna: 'focus_type'
     - Tipo: object
     - Nulos: 5 (7.69%)
     - Valores únicos: 3
   - Columna: 'os'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 8
   - Columna: 'fov'
     - Tipo: float64
     - Nulos: 11 (16.92%)
     - Valores únicos: 24
     - Rango numérico: Min=55.00, Max=120.00, Promedio=81.14

--- Archivo: wired-network-card.csv ---
1. Análisis Básico:
   - Dimensiones: 133 filas, 4 columnas
   - Filas duplicadas: 0
   - Ejemplo de datos (primeras 3 filas):
                name   price interface color
0    TP-Link TG-3468   14.99   PCIe x1   NaN
1      Asus XG-C100C   86.18   PCIe x4   NaN
2  Intel E1G44ET2BLK  392.21   PCIe x4   NaN

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 133
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 59 (44.36%)
     - Valores únicos: 71
     - Rango numérico: Min=9.27, Max=392.21, Promedio=77.55
   - Columna: 'interface'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 9
   - Columna: 'color'
     - Tipo: object
     - Nulos: 98 (73.68%)
     - Valores únicos: 15

--- Archivo: wireless-network-card.csv ---
1. Análisis Básico:
   - Dimensiones: 340 filas, 5 columnas
   - Filas duplicadas: 8
   - Ejemplo de datos (primeras 3 filas):
                  name  price  protocol interface           color
0  Gigabyte GC-WBAX210  42.99  Wi-Fi 6E   PCIe x1  Black / Silver
1      Asus PCE-AX3000  49.99   Wi-Fi 6   PCIe x1           Black
2   TP-Link TL-WN881ND  14.99   Wi-Fi 4   PCIe x1             NaN

2. Análisis de Columnas y Calidad:
   - Columna: 'name'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 324
   - Columna: 'price'
     - Tipo: float64
     - Nulos: 219 (64.41%)
     - Valores únicos: 97
     - Rango numérico: Min=6.99, Max=129.94, Promedio=38.65
   - Columna: 'protocol'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 6
   - Columna: 'interface'
     - Tipo: object
     - Nulos: 0 (0.00%)
     - Valores únicos: 8
   - Columna: 'color'
     - Tipo: object
     - Nulos: 267 (78.53%)
     - Valores únicos: 12

================================================================================
RESUMEN GENERAL DEL ANÁLISIS
================================================================================

Total de archivos analizados: 25

3. Análisis de Patrones:
   - Categorías detectadas (por nombre de archivo): 25
   - Fabricantes únicos extraídos: 639
   - Colores únicos encontrados: 171
   - Columnas comunes en TODOS los archivos: name, price