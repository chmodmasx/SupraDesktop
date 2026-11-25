# Sistema de diseño SupraUI

**AVISO DE PROCEDENCIA — NO OPERATIVO:** las cifras históricas de este borrador no están verificadas independientemente y no constituyen parámetros de producción aprobados. No utilizar recursos de diseño de Apple ni extraer sus archivos. Sustituir las hipótesis por mediciones propias permitidas y datos de procedencia lícita; preservar la meta 1:1 sin inventar valores. Véase [protocolo de medición](../reference-macos27/MEASUREMENT_PROTOCOL.md).

Tokens semánticos canónicos versionados: color.text.primary/secondary/tertiary/quaternary, color.window.background, color.selection.active, color.accent, material.dock/menu/sidebar/toolbar/notification, geometry.window.radius, spacing, typography, shadow, animation. Generar adaptadores sin duplicar constantes. Apariencia clara, oscura, alto contraste, reducción de movimiento/transparencia, acentos y estados activo/inactivo.

## Paleta de trabajo
Datos de la investigación previa atribuidos al kit macOS 27 Sketch (28-10-2026); pendientes de contrastar contra artefacto exacto y colorimetría nativa. No tratarlos como API pública ni medir sobre capturas sin perfil.

| Color | Claro | Oscuro | Claro vibrante | Oscuro vibrante |
|---|---|---|---|---|
| Rojo | #FF383C | #FF4245 | #F52F32 | #FF4747 |
| Naranja | #FF8D28 | #FF9230 | #F58625 | #FF9E33 |
| Amarillo | #FFCC00 | #FFD600 | #F5C200 | #FFE014 |
| Verde | #34C759 | #30D158 | #26BF4D | #3BDB63 |
| Menta | #00C8B3 | #00DAC3 | #00BDA9 | #2DE0CD |
| Teal | #00C3D0 | #00D2E0 | #00B3BF | #2DD7E0 |
| Cian | #00C0E8 | #3CD3FE | #00ABCF | #47D8FC |
| Azul | #0088FF | #0091FF | #0078F0 | #0A99FF |
| Índigo | #6155F5 | #6D7CFF | #5C50E6 | #7163FF |
| Violeta | #CB30E0 | #DB34F2 | #B72BC9 | #E647FC |
| Rosa | #FF2D55 | #FF375F | #F5234B | #FF4169 |
| Marrón | #AC7F5E | #B78A66 | #9E7354 | #C29672 |
| Gris | #8E8E93 | #98989D | #848489 | #A2A2A7 |

Texto claro negro alfa 85/50/25/10/5/3%; oscuro blanco 100/55/25/10/5/3% (discrepancia Figma reportada: primario 85%; verificar). Rellenos normales negro/blanco 10/8/5/3/2%; vibrantes claro 15/7/5/3/2%, oscuro 14/8/5/4/3%. Modos plus-darker / plus-lighter a validar. Contenido principal #FFFFFF / #1E1E1E. Sidebar activa #FAFAFA 80% / #0C0C0C 85%; inactiva #F4F4F4 100% / #2E2E2E 85%.

Sonoma 14.4 (referencia histórica separada): ventana #ECECEC/#323232, contenido #FFFFFF/#1E1E1E, selección #0064E1/#0059D1, texto seleccionado #B3D7FF/#3F638B, inactiva #DCDCDC/#464646, enlaces #0068DA/#419CFF, acento #007AFF. No mezclar automáticamente con macOS 27.

## Controles
Botones, switches, radios, checkbox, segmentos, campos, combo, búsqueda, listas, tablas, árboles, tabs, sidebar, toolbar, menús, popovers, diálogos, indicadores, focus ring. Cada control define geometría, estados, tokens, navegación por teclado, árbol semántico, acción, permisos y prueba visual. Inter (OFL) candidata; calibrar métricas, sin redistribuir SF. Recursos originales con procedencia y licencia.

## Referencias
[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) y [Design Resources](https://developer.apple.com/design/resources/). Véase [fuentes](../research/SOURCES.md).
