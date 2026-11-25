# Desarrollo y packaging

M00 documentación y ADR. Primer crate real con workspace virtual, Cargo.lock versionado para aplicaciones, toolchain fijado tras prueba, fmt/clippy/test y dependencias auditadas. CI incremental: docs, build, pruebas, conformidad, visual, fallos, accesibilidad, permisos, rendimiento, build Arch en chroot limpio y pruebas de despliegue. No activar checks ficticios; workflow actual solo valida enlaces Markdown locales. No hay build/instalación disponible.

Entorno inicial: compositor anidado en sesión Linux existente; datos/config temporales. Más tarde VM KVM y sesión separada en hardware. Packaging Arch modular mediante PKGBUILD y devtools, unidad systemd de usuario y sesión Wayland alternativa. No sustituir KDE ni cambiar defaults de SupraLINUX durante experimentos. Separar artefactos experimentales y estables; sin publicación estable automática. Pruebas de instalación, actualización, desinstalación y rollback. Versionado semántico y changelog al implementar.

El empaquetado Debian queda fuera del nuevo plan oficial. Mantener portátil el código upstream. [Build/release](../distribution/BUILD_RELEASE.md). No confundir chroot limpio con sandbox de código no confiable.
