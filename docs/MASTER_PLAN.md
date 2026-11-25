# Plan maestro — M00

## Objetivo
Crear un entorno independiente para Linux con fidelidad visual y funcional a macOS 27, AI Ready, modular, GPU acelerado y local. Conservar identidad SupraDesktop. Integración futura como sesión alternativa de SupraLINUX (Ubuntu 26.04, amd64 inicialmente); no sustituir Plasma hasta validación.

## Alcance
- Compositor Wayland, XWayland, ventanas, salidas, entrada, gestión de sesión, bloqueo, permisos.
- SupraGlass: materiales tradicionales y ópticos, blur multinivel, tintes, vibrancy, refracción, reflejos, sombras y contraste.
- SupraUI: sistema de diseño, widgets, tipografía, accesibilidad y acciones semánticas.
- Shell: desktop, Dock, menú global, Control Center, notificaciones, búsqueda, widgets, Spaces, Mission Control, Stage Manager, OSD.
- Apps: Files, Settings, Preview, Terminal, Monitor, Archive; después Disks, Text, Calculator, Calendar, Notes, Photos, Backup, Store, Music.
- Servicios: registro de apps, lanzamiento, indexación, portapapeles, configuración, audio, energía, autenticación, portales.
- AI Ready: API nativa, MCP/CLI/SDK, AT-SPI, fallback visual autorizado, permisos y sesiones de agentes aisladas.
- Compatibilidad con Qt/GTK/Electron/Flatpak/AppImage/Steam/Wine/Proton; no prometer menú global o tema universal.
- Pruebas visuales, funcionales, rendimiento, accesibilidad, fallos, protocolos, packaging Debian.

## Stack
Smithay, calloop, Wayland, GLES/EGL inicial, GLSL, libinput, DRM/GBM, zbus, Tokio para servicios, Serde, SQLite/Tantivy cuando proceda, PipeWire/WirePlumber, NetworkManager, BlueZ, UPower, logind. Iced y AccessKit son candidatos; evaluar libcosmic y alternativas antes de fijar toolkit. Vulkan posterior si aporta valor. Inter candidata tipográfica. No fijar versiones ni licencias sin auditoría.

## Primer corte verificable
SupraLab + compositor anidado + material calibrable + un control accesible con acción registrada, validación de esquema y política. Ejecutar dentro de Plasma sin tocar sesión activa. Capturas deterministas, entrada y foco, pruebas de permisos, fallo de un componente y presupuesto de frame. No empezar por docenas de crates vacíos.

## Estado y decisiones
Los principios aprobados guían M00. El resto es especificación propuesta salvo ADR aceptado por el mantenedor. Ningún resultado gráfico ni benchmark está verificado. Los objetivos visuales y numéricos son hipótesis que requieren macOS nativo y hardware. Véase [roadmap](ROADMAP.md), [arquitectura](architecture/ARCHITECTURE.md), [fuentes](research/SOURCES.md).
