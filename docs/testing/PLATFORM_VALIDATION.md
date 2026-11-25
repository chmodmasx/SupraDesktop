# Puertas A00 y P16–P30
Todos NOT_RUN. Ver [especificaciones](../specifications/platform/README.md). Usar fixtures, sesión anidada/VM y hardware dedicado; registrar versiones, pruebas, resultados, limitaciones. No confundir prueba documental con ejecución.
| ID | Puerta inicial | Hito |
|---|---|---|
| A00 | Applications + AppImage/AppDir, registro y no autoejecución | M05/M09 |
| P16 | daño incremental equivalente a redraw, efectos correctos | M02/M03 |
| P17 | recursos acotados, lifetime/fences y fallback | M03 |
| P18 | IME, graphemes, teclado y texto protegido | M02/M04 |
| P19 | Orca/AT-SPI y semántica real, accesibilidad no opcional | M04 |
| P20 | identidad y lifecycle multi-window/formatos | M05 |
| P21 | colas acotadas, input/render no bloqueado | M02 |
| P22 | IPC tipado medido, autorización y resync | M01/M04 |
| P23 | detección no respondiente sin falso cierre | M05 |
| P24 | energía/perfiles sin interferir protecciones | M07/M08 |
| P25 | headless CI separado, portal autorizado | M02/M08 |
| P26 | locales, RTL, pseudolocale y acciones estables | M04 |
| P27 | compatibilidad de plugins, aislamiento y rechazo seguro | M08 |
| P28 | notificaciones/Focus y privacidad | M08 |
| P29 | hotplug, adaptadores y permisos | M07/M08 |
| P30 | trazas, métricas, export redactado | M01 transversal |
P16/P17/P21/P22/P30 tempranos, P18/P19/P26 en primer UI, P20 antes de Dock. A00 primero portables/registro, formato nativo solo si brecha comprobada. P25 headless útil para CI, servidor remoto externo no bloquea primera sesión. P27 no obliga a framework de plugins en M00. Cada especificación define subcasos; pruebas nativas macOS aún pendientes.

A00 se actualiza para no ofrecer .deb en distribución oficial. Añadir pruebas de aplicaciones AUR exportadas y extensiones host separadas. [Puertas D00–D12](../distribution/VALIDATION.md).
