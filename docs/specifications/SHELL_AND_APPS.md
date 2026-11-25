# Shell, servicios y aplicaciones

Dock y menú consultan registro de apps (app_id, desktop entry, Flatpak, XWayland) y compositor, no títulos como identidad. Spaces, Overview y Stage comparten autoridad de ventanas del compositor. Menu global: menú exportado vía AppMenu/D-Bus cuando disponible; fallback sin inventar menús. Integración desigual en GTK, Qt, Electron, X11.

SupraFiles: motor fileops separado, vistas iconos/lista/columnas/galería, tabs, favoritos, etiquetas, miniaturas, Quick Look, búsquedas, papelera XDG, conflictos, operaciones asíncronas y undo cuando posible. SupraSettings usa mismos handlers que CLI y UI. Preview con parsers aislados; Terminal, Monitor y Archive independientes.

Servicios reutilizan NetworkManager, BlueZ, PipeWire/WirePlumber, UPower, power-profiles-daemon, UDisks2, CUPS, PAM/Polkit, logind, Secret Service, freedesktop Notifications, XDG MIME, Fcitx5/IBus. Indexación local con exclusiones, cancelación y límites. Ausencia de servicio degrada solo su función. Widgets de terceros fuera del compositor.

Portales XDG: Settings, FileChooser, ScreenCast, Screenshot, RemoteDesktop, GlobalShortcuts, Background, Inhibit; captura y entrada requieren consentimiento y sesión scoped. PipeWire para stream, libei/EIS candidato. No reemplazar portales de sesión activa durante pruebas.
