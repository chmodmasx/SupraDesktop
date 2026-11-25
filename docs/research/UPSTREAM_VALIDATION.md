# Validación upstream — 2026-11-24

| Fuente | Hallazgo | Consecuencia |
|---|---|---|
| [Apple HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials) | Liquid Glass regular/clear; macOS distingue blending detrás/dentro de ventana | Dos responsables de composición, receta semántica común |
| [Apple WWDC25 Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/) | Material dinámico y adaptación de legibilidad | Validar estados, fondo, tamaño, movimiento y contraste; no reducir a blur |
| [Apple macOS 27 kits](https://developer.apple.com/news/?id=e2lxw9l1) | Existencia de kits para Figma/Sketch | No emplearlos en SupraDesktop |
| [Apple licencias](https://developer.apple.com/licensing-trademarks/) | Recursos sujetos a términos específicos | Arte, fuentes y código independientes; revisión jurídica |
| [Smithay 0.7.0 backend](https://docs.rs/smithay/0.7.0/smithay/backend/) | Winit anidado y DRM/GBM | Prototipo anidado primero |
| [Smithay Wayland](https://docs.rs/smithay/0.7.0/smithay/wayland/) | Módulos syncobj, lock, fractional scale, toplevel list | Verificar feature flags y pruebas reales antes de fijar dependencias |
| [ext-foreign-toplevel-list](https://wayland.app/protocols/ext-foreign-toplevel-list-v1) | Enumeración mínima, requiere extensiones para más funciones | API propia autorizada para gestión del shell |

Estado: consulta documental; ninguna prueba de ejecución ni medición nativa. No se verificaron los números históricos de colores y blur. No se descargaron recursos gráficos de Apple. Las fuentes no sustituyen pruebas de conformidad ni revisión legal.
