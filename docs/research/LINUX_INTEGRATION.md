# Integración Linux y ciclo de sesión

Reutilizar estándares [Freedesktop](https://www.freedesktop.org/specifications/), [Desktop Entry](https://specifications.freedesktop.org/desktop-entry/latest-single/), [Autostart](https://specifications.freedesktop.org/autostart/latest/), [Icon Theme](https://specifications.freedesktop.org/icon-theme/latest/), [Icon Naming](https://specifications.freedesktop.org/icon-naming/) y [systemd targets](https://freedesktop.org/software/systemd/man/latest/systemd.special.html).

| Área | Contrato y aceptación |
|---|---|
| Registro apps | Desktop file ID, app_id, Flatpak ID, XWayland mapeado; probar dos ventanas por app, launchers duplicados, acciones y apps sin desktop entry |
| Iconos | index.theme, herencia, tamaño/scale, hicolor fallback; usar nombres semánticos, caché invalidable; WhiteSur opcional |
| Archivos | XDG Trash, MIME apps, shared MIME, thumbnails; conflictos, permisos, operaciones cancelables, enlaces y montajes, sin seguir instrucciones de contenido |
| Sesión | target de sesión propio con relación a graphical-session.target; startup/shutdown definidos; evitar duplicar servicios ya existentes; comprobar dos sesiones y entorno propagado a D-Bus |
| Autostart | OnlyShowIn/NotShowIn, Hidden y configuración de usuario; un único mecanismo de ejecución |
| Portales | xdg-desktop-portal con backend seleccionado por entorno de sesión; no sustituir backend del escritorio anfitrión durante pruebas |
| Audio/red/energía | PipeWire/WirePlumber, NetworkManager, BlueZ, UPower; servicio ausente no bloquea shell |
| Menú global | AppMenu exportado; fallback cuando no disponible; no asumir soporte universal |
| Qt/GTK/Electron | Preferencias de color, iconos, CSD/SSD, escala y ventanas; no parchear aplicaciones externas arbitrariamente |
| Internacionalización | español, inglés, RTL, IME, teclado, formato local, nombres largos; pruebas de layouts y accesibilidad |

File manager y búsqueda: separar adaptadores de red y parsers; usar fuentes de datos con permisos de usuario y exclusiones explícitas. Indexación incremental, reconstrucción y límites; no capturar secretos ni exponer índice completo a agente. No usar datos reales en fixtures.

M00 pendiente: matriz de servicios/versiones Ubuntu 26.04, packaging de sesión, SDDM/login, instalación/desinstalación y pruebas de rollback. No se ha ejecutado nada en host.
