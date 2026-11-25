# SupraDesktop

Entorno de escritorio independiente para Linux. **1:1 macOS Visual · AI Ready · Modular First**.

Referencia inicial: macOS 27. Implementación independiente, Rust First, Wayland nativo, GPU acelerada, Local First. Integración futura con SupraLINUX sin dependencia obligatoria de esa distribución.

**Estado: M00 — especificación fundacional.** No existe todavía una sesión funcional, motor gráfico ni servidor MCP. Las carpetas describen límites de responsabilidad, no entregables terminados.

## Documentación
- [Principios](PRINCIPLES.md) — constitución del proyecto.
- [Plan maestro](docs/MASTER_PLAN.md) y [roadmap](docs/ROADMAP.md).
- [Arquitectura](docs/architecture/ARCHITECTURE.md).
- [Referencia visual y funcional](docs/reference-macos27/MACOS27_SPEC.md).
- [Sistema de diseño](docs/specifications/DESIGN_SYSTEM.md), [materiales](docs/specifications/MATERIALS.md) y [renderizado](docs/specifications/RENDERING_SPEC.md).
- [AI Ready](docs/ai-native/AI_ARCHITECTURE.md) y [modelo de amenazas](docs/ai-native/THREAT_MODEL.md).
- [Criterios de pruebas](docs/testing/TESTING.md).
- [Decisiones](docs/decisions/README.md) y [fuentes](docs/research/SOURCES.md).
- [Reglas para agentes](AGENTS.md), [contribución](CONTRIBUTING.md) y [seguridad](SECURITY.md).

## Límites
No se promete equivalencia binaria con macOS, compatibilidad con servicios propietarios, ni distribución de recursos de Apple. Licencia del código propio pendiente de ratificación y auditoría de dependencias; no incorporar código ajeno hasta resolverla. No es un proyecto afiliado a Apple.

No hay instrucciones de instalación todavía. No reemplazar una sesión existente con prototipos.
