# Puertas S01–S15 (NOT_RUN)
Ver [especificaciones](../specifications/subsystems/README.md). Ejecutar con fixtures propios, sesión anidada/VM, versiones fijadas y revisión de licencias. Registrar comandos, commit, hardware, resultados, métricas, artefactos, fallos y decisiones.
| ID | Dependencias principales | Puerta inicial | Hito |
|---|---|---|---|
| S01 | geometry, tokens, renderer | tema estándar + icono multicapa reproducible | M01/M03 |
| S02 | geometry, compositor, tokens | negociación CSD/SSD y ROI | M02/M04 |
| S03 | preferences, tokens, portal | matriz Qt/GTK/Flatpak con fallback | M04/M10 |
| S04 | text, geometry, tokens | constraints, hit test y a11y | M01/M04 |
| S05 | layout, data model | nodos acotados y selección estable | M04 |
| S06 | config, IPC, actions | revisión, persistencia y live update | M01/M04 |
| S07 | schema, measurement | generación determinista y errores | M01 |
| S08 | fileops, MIME, sandbox | cache XDG y preview aislado | M08/M09 |
| S09 | input, Wayland, fileops | DnD cross-toolkit y cancelación | M02/M09 |
| S10 | actions, permissions, UI | widget aislado y crash recovery | M08 |
| S11 | compositor, services | readiness, lock, recuperación | M02/M07 |
| S12 | focus, app registry, actions | menú asociado sin stale focus | M05/M10 |
| S13 | media, preferences | evento y fallback sin audio | M08 |
| S14 | fileops, permissions, discovery | transferencia local consentida | post M08 |
| S15 | actions, trust, events | flujo tipado reversible de prueba | M04/M08 |
Todos los subcasos descritos en cada documento. Seguridad, accesibilidad y licencia son puertas, no puntuaciones compensables. No cerrar S01/S02/S04 por compilación; falta calibración 1:1. S14/S15 no deben retrasar compositor básico.
