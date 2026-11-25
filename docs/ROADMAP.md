# Hitos y puertas de aceptación

Todos pendientes salvo creación de documentación fundacional (M00 parcial). No son promesas de fechas. Una puerta exige evidencia; si falla, mantener estado experimental.

| Hito | Entregable / puerta | Dependencias |
|---|---|---|
| M00 | Inventario, principios, ADR, fuentes, licencias, amenazas y criterios revisados | — |
| M01 | SupraLab con patrones deterministas, capturas, métricas y material de referencia | M00 |
| M02 | Compositor anidado, cliente Wayland, foco, entrada, resize y cierre | M00 |
| M03 | SupraGlass con blur, composición, sombras y refracción calibrables; fallback | M01, M02 |
| M04 | SupraUI con controles accesibles, tokens y acciones semánticas | M01, M02 |
| M05 | Desktop, Dock, barra superior, lanzamiento y registro de apps | M02–M04 |
| M06 | Spaces, Mission Control, Exposé, tiling, fullscreen, Stage Manager | M05 |
| M07 | Sesión nativa DRM/KMS, XWayland, escalado y bloqueo fail-closed | M02, M05 |
| M08 | Servicios, portales, búsqueda, notificaciones, control | M04, M05 |
| M09 | Files, Settings, Preview, Terminal, Monitor, Archive | M04, M08 |
| M10 | Matriz Qt/GTK/Electron/Flatpak/Steam/Wine | M07–M09 |
| M11 | Hardening, accesibilidad, rendimiento, recuperación, pruebas de permisos | M07–M10 |
| M12 | PKGBUILD, repositorio Arch congelado, imagen atómica y sesión/ISO experimental | M11 |
| M13 | Auditoría y 1.0 únicamente con aprobación y puertas satisfechas | M12 |

AI Ready transversal desde M00: catálogo y permisos en M01–M04; acciones nativas y supervisión en M05–M08; MCP, portales y sesión aislada validados antes de declarar AI Ready operativo. Cada módulo entrega API, pruebas negativas y accesibilidad junto a UI, no como tarea final.

Versiones tentativas 0.0.1 laboratorio, 0.1 compositor, 0.2 glass, 0.3 UI, 0.4 shell, 0.5 ventanas, 0.6 sesión, 0.7 servicios, 0.8 apps, 0.9 beta. No crear tags/releases automáticamente.

## Puertas de riesgo previas a expansión
[Matriz experimental](testing/EXPERIMENT_MATRIX.md): toolkit y a11y, render offscreen y composición, región blur, cliente externo, contrato de acción, ciclo de sesión y modelo de permisos. No esperar a M11 para identificar bloqueos estructurales; incorporar pruebas tempranas. La puerta M00 requiere resolver o registrar formalmente cada incertidumbre crítica; no exigir medición física completa para comenzar fixtures sintéticos.

## Dependencias S01–S15
Consultar [puertas](testing/SUBSYSTEM_VALIDATION.md) para ordenar experimentos por riesgo. S07/S06 antes de tokens dispersos; S04/S02 antes de shell masivo; S05/S08/S09 antes de Files; S11 desde compositor inicial; S12 con app registry; S14 y S15 no bloquean sesión básica. Licencias y AI Ready transversales.

## Plataforma A00/P16–P30
[Puertas](testing/PLATFORM_VALIDATION.md). Diagnóstico y event loop desde M01/M02; composición y memoria antes de efectos avanzados; IME/a11y/i18n en primer toolkit; registro antes de Dock y Applications; gestión de sesión y energía antes de despliegue; remoting externo y formato propio no bloquean núcleo.

## Track D — distribución oficial candidata
[D00–D12](distribution/VALIDATION.md) paralelo al escritorio, sin bloquear M01/M02. D00 arquitectura; D01–D04 construir base y probar actualización/rollback en VM; D05–D08 módulos y aplicaciones; D09–D12 seguridad, hardware, instalador, distribución. Ninguna imagen estable sin aprobación. No sustituir el proyecto SupraLINUX existente.

## Siguiente corte verificable
[Prototipos D00 y M01/M02](distribution/PROTOTYPE_GATES.md). No ampliar scope antes de obtener evidencia. Mantener contratos portables del escritorio y de SupraDeploy; prototipo de distribución no bloquea compositor anidado. Backend candidato Arkdep, Calamares frontend adaptado, ninguna selección definitiva ni release.
