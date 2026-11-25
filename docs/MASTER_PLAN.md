# Plan maestro — M00

## Objetivo
Crear un entorno independiente para Linux con fidelidad visual y funcional a macOS 27, AI Ready, modular, GPU acelerado y local. Conservar identidad SupraDesktop. Distribución oficial candidata basada en Arch Linux x86-64, imágenes atómicas y escritorio independiente; no migrar ni sustituir SupraLINUX existente sin decisión explícita.

## Alcance
- Compositor Wayland, XWayland, ventanas, salidas, entrada, gestión de sesión, bloqueo, permisos.
- SupraGlass: materiales tradicionales y ópticos, blur multinivel, tintes, vibrancy, refracción, reflejos, sombras y contraste.
- SupraUI: sistema de diseño, widgets, tipografía, accesibilidad y acciones semánticas.
- Shell: desktop, Dock, menú global, Control Center, notificaciones, búsqueda, widgets, Spaces, Mission Control, Stage Manager, OSD.
- Apps: Files, Settings, Preview, Terminal, Monitor, Archive; después Disks, Text, Calculator, Calendar, Notes, Photos, Backup, Store, Music.
- Servicios: registro de apps, lanzamiento, indexación, portapapeles, configuración, audio, energía, autenticación, portales.
- AI Ready: API nativa, MCP/CLI/SDK, AT-SPI, fallback visual autorizado, permisos y sesiones de agentes aisladas.
- Compatibilidad con Qt/GTK/Electron/Flatpak/AppImage/Steam/Wine/Proton; no prometer menú global o tema universal.
- Pruebas visuales, funcionales, rendimiento, accesibilidad, fallos, protocolos, packaging Arch y pruebas de despliegue atómico.

## Stack
Smithay, calloop, Wayland, GLES/EGL inicial, GLSL, libinput, DRM/GBM, zbus, Tokio para servicios, Serde, SQLite/Tantivy cuando proceda, PipeWire/WirePlumber, NetworkManager, BlueZ, UPower, logind. Iced y AccessKit son candidatos; evaluar libcosmic y alternativas antes de fijar toolkit. Vulkan posterior si aporta valor. Inter candidata tipográfica. No fijar versiones ni licencias sin auditoría.

## Primer corte verificable
SupraLab + compositor anidado + material calibrable + un control accesible con acción registrada, validación de esquema y política. Ejecutar dentro de Plasma sin tocar sesión activa. Capturas deterministas, entrada y foco, pruebas de permisos, fallo de un componente y presupuesto de frame. No empezar por docenas de crates vacíos.

## Estado y decisiones
Los principios aprobados guían M00. El resto es especificación propuesta salvo ADR aceptado por el mantenedor. Ningún resultado gráfico ni benchmark está verificado. Los objetivos visuales y numéricos son hipótesis que requieren macOS nativo y hardware. Véase [roadmap](ROADMAP.md), [arquitectura](architecture/ARCHITECTURE.md), [fuentes](research/SOURCES.md).

## Aclaración de alcance aprobada
La fidelidad 1:1 abarca apariencia, disposición, materiales y estados de toda la interfaz propia, con excepciones explícitas para arte, marca y tipografía propietaria. No utilizar recursos de Apple; medir independientemente y documentar desviaciones. La compatibilidad externa y las restricciones transversales siguen vigentes. Véase [metodología](reference-macos27/MEASUREMENT_PROTOCOL.md).

## Investigación ampliada y orden de prototipos
Consultar [índice de investigación](research/SOURCES.md) y [puertas experimentales](testing/EXPERIMENT_MATRIX.md). Resolver toolkit, composición, compatibilidad, lifecycle y permisos mediante pruebas pequeñas antes de comprometer arquitectura definitiva. WhiteSur es candidato a tema de iconos libre reemplazable; parecido estético no implica exclusión automática. No importar recursos sin acreditar derechos.

## Especificaciones avanzadas
[Índice de fidelidad](reference-macos27/fidelity/README.md). El mantenedor permite forks, adaptaciones e incorporación de código libre con obligaciones satisfechas. [Política upstream](development/UPSTREAM_POLICY.md). Ninguna dependencia dicta nuestro diseño. Los modelos matemáticos son candidatos a ajustar mediante observación independiente, no parámetros nativos verificados.

## Subsistemas S01–S15
[Especificaciones detalladas](specifications/subsystems/README.md), [puertas y dependencias](testing/SUBSYSTEM_VALIDATION.md). Reutilizar formatos y protocolos estándar, adaptar implementaciones libres o construir propias si insuficientes. No adoptar toolkit ni API sin experimentos. Integrar acciones semánticas, configuración y accesibilidad desde cada módulo.

## Experiencia Applications y plataforma interna
[Especificaciones A00/P16–P30](specifications/platform/README.md), [puertas](testing/PLATFORM_VALIDATION.md). Vista Aplicaciones unificada y ~/Applications para portables; soportar AppImage/AppDir primero, Flatpak mediante su gestor; AUR integrado/restringido o por capas host opcional; sin proveedor .deb oficial, SupraBundle opcional solo si brecha comprobada. No confundir formato con 1:1 visual ni crear gestor nuevo. Núcleo: render graph pequeño, presupuesto GPU, entrada Unicode/IME y accesibilidad, registro/lifecycle, eventos/IPC, diagnóstico, energía, headless, i18n, ABI, notificaciones y dispositivos. Todos candidatos y experimentos pendientes.

## Distribución oficial
[Arquitectura y puertas de decisión](distribution/README.md). Preferencia del mantenedor: base Arch, paquetes congelados coherentemente, sistema atómico, Flatpak/AppImage/AppDir y SupraBundle opcional. Pacman construye la base; no es el instalador habitual del usuario. Las decisiones de backend, kernel, layout de disco y modelo de seguridad siguen PROPOSED. No migrar el proyecto SupraLINUX actual ni publicar imágenes.

## Experiencia de distribución ratificada
Diseñar primero para usuarios sin experiencia Linux, con procesos gráficos coherentes con macOS, accesibles y honestos. Modos avanzados opcionales. SupraDesktop y distribución separados. Paquetes Arch/AUR por capas elegibles, módulos bajo demanda; v4l2loopback no requisito de base. Ver [UX](distribution/USER_EXPERIENCE.md), [SupraLayers](distribution/PACKAGE_LAYERING.md) y [validación ampliada](distribution/DEEP_VALIDATION.md).

## Ratificación y transición a prototipos
Priorizar Arkdep adaptado como PoC, no dependencia definitiva. [Auditoría](distribution/ARKDEP_SOURCE_REVIEW.md), [frontend del instalador](distribution/INSTALLER_FRONTEND.md) y [gates](distribution/PROTOTYPE_GATES.md). Mantener distro como proyecto independiente; no migrar SupraLINUX ni crear repo sin autorización. La investigación documental no prueba fidelidad o atomicidad. Siguiente trabajo recomendado: cerrar contradicciones y ejecutar cortes verticales M01/M02 y D00–D04 en entornos descartables.
