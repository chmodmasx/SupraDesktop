# Materiales — registro de hipótesis visuales

Valores extraídos/reportados en la investigación previa del kit Sketch macOS 27; fuente exacta y revisión nativa pendientes. Radios de diseño NO son sigma gaussiano, píxeles físicos ni unidades de KWin/GLSL. Separar blur del fondo, blur de sombras y blur efectivo medido. Calibrar con patrones y perfiles de color.

| Liquid Glass | Radio claro/oscuro | Saturación C/O |
|---|---|---|
| Dock | 1/1 | 100/100% |
| Controles pequeños | 6/6 | 200/100% |
| Controles pequeños tintados | 6/6 | 100/100% |
| Notificaciones | 15/10 | 100/100% |
| Menús | 20/20 | 80/120% |
| Paneles medianos y grandes | 30/30 | 140/120% |
| Sidebar activa (tradicional) | 100/80 | 100/200% |
| Sidebar inactiva | 100/70 | 100/180% |
| Scroll edge (diseño) | 6/6 | 100/100% |

Materiales clásicos: radio de diseño común 60.
| Material | Tinte claro y alfa | Tinte oscuro y alfa | Saturación C/O |
|---|---|---|---|
| Ultra Thin | #ECECEC 38% | #292929 40% | 145/180% |
| Thin | #ECECEC 50% | #292929 49% | 145/190% |
| Regular | #ECECEC 63% | #2C2C2C 61% | 145/190% |
| Thick | #ECECEC 76% | #2C2C2C 71% | 200/190% |
| Ultra Thick | #ECECEC 88% | #2C2C2C 82% | 200/190% |

Dock: tinte luminosidad #4D4D4D 30% / #454545 50%, oscurecimiento #1A1A1A 10%, aclarado blanco 8%, distorsión 0.08, profundidad 0.9, radio esquinas 15. Menú: #E6E6E6 55% / #5A5A5A 50%, distorsión 0.3, profundidad 0.9, esquinas 12, sombra 30%. Barra superior: sin blur integral en kit, selección negro 8% / blanco 20%, radio selección 30, saturación 100/105%.

Sombras propuestas a calibrar: ventana activa clara y oscura con sidebar Y36 radio100 alfa40%; oscura sin sidebar Y16 radio33 alfa40%; inactiva Y16 radio32 alfa20%; menú Y4 radio24 alfa30%; popover claro Y18 radio46 alfa25%, oscuro Y18 radio48 alfa45%; utilidad clara Y5 radio20 alfa30%; notificación Y4 radio16 alfa10%.

Investigación independiente reportó platformContentGlass blurRadius 45, menú contextual efectivo ~6.8 pt, scroll edge 6 y saturación 125%, escala muestreo 0.25, lectura exterior ~12 pt. Son observaciones no reproducidas y posiblemente de diferentes etapas/implementaciones; no equivalencias.

## Implementación propuesta
Receta semántica tipada: id, schemaVersion, apariencia, tintes RGBA y blend, blurReference y unidad/origen, calibración backend, saturación/luminosidad, geometría, profundidad, distorsión, reflejo, sombras, fallback opaco y accesibilidad. Los parámetros del renderer deberán vivir en configuración propia validada. No introducir valores de referencia como constantes definitivas.
