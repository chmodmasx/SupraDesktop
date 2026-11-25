# ADR-0002 — Rust y Wayland
Estado: PROPOSED. Rust First y Wayland Native son principios aprobados; Smithay preferido frente a wlroots/KWin/Mutter o compositor desde cero. Verificar APIs, licencias, soporte de protocolos, backend NVIDIA e integración XWayland. Toolkit Iced provisional; comparar libcosmic y GPUI con pruebas de accesibilidad, layer shell, renderizado y texto. No fijar dependencia hasta superar prototipo.

## Puerta de elección de toolkit
Comparar Iced, libcosmic, GPUI y Slint con la misma prueba de concepto; no fijar hasta medir. GPUI incluye ejemplo layer-shell pero es pre-1.0; libcosmic documenta a11y experimental y COSMIC Files/Portal muestran limitaciones en manifests. [Matriz](../research/TOOLKIT_EVALUATION.md). Si ningún candidato supera las puertas, investigar backend limitado propio antes de construir toolkit generalista.
