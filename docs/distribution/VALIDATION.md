# Puertas de distribución (D00–D12)
Estado de todas: NOT_RUN. No distro ni release existente.
| ID | Evidencia exigida |
|---|---|
| D00 | Comparativa Arkdep/RAUC/sysupdate, licencia, mantenimiento, modelo de datos y coste |
| D01 | Snapshot Arch coherente, PKGBUILD, locks, firmas y SBOM |
| D02 | Imagen de prueba arranca en KVM/UEFI y sesión mínima |
| D03 | Actualización interrumpida en descarga, stage y boot; anterior sigue arrancable |
| D04 | Boot assessment/rollback, datos y migraciones compatibles, espacio insuficiente |
| D05 | Flatpak, AppImage/AppDir, Applications, sin autoejecución, sin .deb |
| D06 | v4l2loopback por kernel, cámara virtual y aplicación autorizada; rollback |
| D07 | NVIDIA/Intel/AMD, legacy, CUDA/VRAM bajo carga, multilib y juegos |
| D08 | AUR build separado, exportación, perfil restringido y host excepcional |
| D09 | Verificación firmas, boot trust, módulos, recovery y permisos; pruebas negativas inocuas |
| D10 | Instalador, cifrado, dual boot, recuperación y hardware |
| D11 | CVE, canales, promoción, revocación y disponibilidad de artefactos |
| D12 | Auditoría, documentación, soporte y aprobación explícita antes de publicación |
No declarar PASS sin evidencia; no confundir checks Markdown con pruebas. Mantener track distro separado de desarrollo de compositor; no bloquear M01/M02. D00 requiere decisión de nombre/repositorio/alcance y recursos de mantenimiento; no migrar SupraLINUX existente.
