# Evaluación de toolkit — revisión documental 2026-11-24

No se eligió toolkit final ni se ejecutó ningún benchmark. Seleccionar por capacidades medidas, no popularidad.

| Candidato | Evidencia upstream | Incertidumbre crítica |
|---|---|---|
| Iced | [Repositorio](https://github.com/iced-rs/iced), renderer personalizable | Accesibilidad Linux, layer-shell y control de composición dentro de ventana |
| libcosmic | [README](https://github.com/pop-os/libcosmic) documenta applets, Wayland y a11y experimental | Dependencia de stack COSMIC, estabilidad y estilo totalmente independiente |
| GPUI | [README](https://github.com/zed-industries/zed/blob/main/crates/gpui/README.md) pre-1.0; [layer shell](https://github.com/zed-industries/zed/blob/main/crates/gpui/examples/layer_shell.rs), [headless](https://github.com/zed-industries/zed/blob/main/crates/gpui/examples/README.md) | Accesibilidad, API cambiante, renderizado personalizado y packaging |
| Slint | [backend Winit](https://docs.slint.dev/latest/docs/slint/guide/backends-and-renderers/backend_winit/), [prácticas de a11y](https://docs.slint.dev/latest/docs/slint/guide/development/best-practices/) | Superficies especiales, licencias aplicables a configuración elegida, control de materiales |
| Toolkit propio | Control completo hipotético | Alto coste de texto, IME, foco, accesibilidad, mantenimiento y widgets |

Importante: [COSMIC Files Cargo.toml](https://github.com/pop-os/cosmic-files/blob/master/Cargo.toml) y [Portal Cargo.toml](https://github.com/pop-os/xdg-desktop-portal-cosmic/blob/master/Cargo.toml) contienen comentarios sobre fallos con a11y. No generalizar a todos los componentes ni asumir que persisten tras cambios upstream.

## Prototipo idéntico por candidato
Ventana de Settings sintética, panel layer-shell, menú popup, sidebar con scroll, control segmentado, botón, switch, texto editable, navegación teclado, IME, DnD, escala 1/1.25/2, tema claro/oscuro y prueba de resize. Material propio dentro de ventana y solicitud estándar detrás de ventana. IDs semánticos estables, árbol accesible consumido por lector de pantalla y API de acciones independiente del modelo. Verificar comportamiento sin GPU si backend ofrece fallback.

## Puertas
P0: accesibilidad comprobable, acción semántica, foco/entrada, pixel control, ventanas Wayland y dependencia/licencia aceptables. Un fallo P0 no se compensa con FPS altos. P1: RAM PSS, latencia primera ventana y acción, p95/p99 frame time, compilación, escalado, integración de texto, testabilidad y esfuerzo de mantenimiento. Mismo hardware, toolchain, render size y corpus. Registrar revisión, flags, comandos y trazas; no declarar ganador sin prototipo.

Evaluar una biblioteca de diseño común con adaptadores pequeños, no un framework universal para ocultar diferencias artificialmente. Contratos de acciones y tokens permanecen independientes de elección gráfica.
