# Contribución

Leer primero [PRINCIPLES](PRINCIPLES.md) y [AGENTS](AGENTS.md). Cada PR debe indicar objetivo, módulo, requisitos, diseño, alternativas, licencias, impacto de seguridad/accesibilidad/rendimiento, pruebas ejecutadas y limitaciones. Usar commits convencionales (docs, feat, fix, test, refactor, build, ci). Separar cambios funcionales de refactors. No incorporar binarios ni código de terceros sin auditoría. Los cambios de contrato requieren ADR y estrategia de migración.

M00: contribuir documentación y experimentos explícitamente etiquetados; no hay build de producción. Cuando existan crates, exigir cargo fmt --check, clippy, test y pruebas específicas; fijar toolchain/dependencias tras validar compatibilidad. Los PR no se fusionan automáticamente.
