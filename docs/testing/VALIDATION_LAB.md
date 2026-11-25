# Laboratorio experimental — 14 incertidumbres
Estado NOT_RUN. No ejecución, no benchmarks ni distribución arrancable. Fuentes: [QEMU blkdebug](https://www.qemu.org/docs/master/devel/testing/blkdebug.html), [QMP](https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html), [Arkdep build](https://docs.arkanelinux.org/arkdep/arkdep-build-usage/), [WLCS](https://github.com/canonical/wlcs).
## Distribución
VM QEMU/KVM + OVMF con discos descartables qcow2, ESP y Btrfs; snapshots de test, red controlada, serial logs, test signing keys exclusivamente. Baseline Arkdep fijado, snapshot Arch y artefactos verificables. Probar paquete normal antes de AUR, luego DKMS de prueba. Estado inicial y final: hash de archivos de despliegue activo (excluir estado permitido), manifest real y DB pacman, boot entries, datos de prueba, configuración, estado de transacción. Comparar con baseline.
Fault injection separado: error I/O mediante blkdebug, falta de espacio, interrupción de proceso, apagado abrupto de VM y fallo de health check. No equiparar apagar VM a fallo físico exacto ni usar disco real. Insertar checkpoints identificables en flujo; matriz antes/después de download, signature, staging, build, hooks, manifest, boot publish, first boot y health confirmation. Conservar known-good y prueba de datos; tras reiniciar reconciliar sin pasos manuales para casos previstos. Test de recuperación offline y de cambios de schema. Registrar PASS/FAIL/BLOCKED/NOT_RUN con logs y artefactos.
## Escritorio
Compositor anidado y headless, fixtures sintéticos sin datos personales. Smithay smallvil para mínimo, Anvil para features y wlcs_anvil para estudiar integración. Probar Wayland shell, popup, focus, seat, resize, buffers y salida; WLCS necesita adaptador de compositor, no suite plug-and-play. Mesa llvmpipe para CI software, no sustituye GPU real. Ver [compositor y glass](../research/GRAPHICS_PROTOTYPES.md).
## Criterios
| Área | Gate |
|---|---|
| Arkdep | Adaptación acotada, estado efectivo verificable, comparación si falla |
| Atomicidad | Todos los puntos de fallo conservan known-good y datos fixture |
| SupraLayers | Paquete normal/AUR/DKMS opcional y eliminación sin mutar activo |
| Secure Boot | OVMF claves test, luego hardware y cadena pública, no bypass |
| Smithay | Cliente anidado y conformance seleccionado |
| SupraGlass | Comparación de perfil blur, desplazamiento, sombra y color |
| SupraUI | Mismo fixture de layout, a11y, IME, layer-shell y acciones |
| Fidelidad | Corpus macOS nativo autorizado, no valores inventados |
| Licencias | Inventario transitivo y decisión de licencia previa a incorporación |
| Calamares | Branding/view sin regresiones de validación, job atómico separado |
| Recovery | Arranque offline, anterior, modo seguro y medio externo |
| Infraestructura | Medición build, artefactos, coste y retención |
| Hardware | Matriz por GPU/driver, disco, firmware y entrada |
| Firmware | Emulación de fwupd, actualización real solo en entorno autorizado |
No cerrar por documentación o compilación. No exigir todos los casos de release para comenzar un PoC sintético. CI documental es distinta de CI de ejecución.
