# Compatibilidad

Qt 6/5: adaptadores de tema y plataforma cuando corresponda; GTK 3/4/libadwaita dentro de límites de toolkit; Electron y XWayland apariencia variable. No interceptar UI ni forzar modificaciones frágiles. Flatpak: portales XDG; AppImage: integración desktop entry; Wine/Proton/Steam: Wayland o XWayland según app, pruebas de entrada, fullscreen, capture y explicit sync. Menú global solamente donde app exporta menú. No prometer identidad visual total en apps externas. Accesibilidad AT-SPI y selección de IME. Matriz por versión, GPU, protocolo, caso de uso, resultado y limitación; todavía sin resultados.

Distribución oficial: Flatpak, AppImage, AppDir, SupraBundle opcional y AUR encapsulado; .deb no es formato de instalación oficial. Portabilidad del escritorio a otros Linux sigue objetivo, no promesa de empaquetado Debian. Compatibilidad de módulos, GPU, FUSE, contenedores y runtimes exige pruebas. [Distribución](../distribution/README.md).
