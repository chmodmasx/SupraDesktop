# Protocolos y compatibilidad Wayland

Prioridad inicial (no implica soporte actual de Smithay).
- P0: xdg-shell, wl_shm, linux-dmabuf, xdg-decoration, wlr-layer-shell, xdg-activation, viewporter, fractional-scale, ext-session-lock, linux-drm-syncobj.
- P1: presentation-time, ext-foreign-toplevel-list, ext-workspace, pointer-constraints, relative-pointer, text-input-v3, input-method-v2, idle-inhibit, ext-image-copy-capture.
- P2: color-management, integración KDE AppMenu, protocolos adicionales según apps.

Separar permisos de protocolos privilegiados del cliente estándar. No permitir lectura de otras ventanas ni entrada emulada arbitraria. XWayland como compatibilidad; documentar límites de aislamiento X11. Validar clientes GTK, Qt, Electron y juegos; WLCS donde esté soportado. Lock: si cliente de bloqueo muere, compositor permanece bloqueado. Gestos y activación respetan foco, seat y seriales.

Fuente: [Wayland protocols](https://wayland.app/protocols/), [Smithay](https://github.com/Smithay/smithay), [WLCS](https://github.com/canonical/wlcs).

## Revisión upstream 2026-11-24
Smithay 0.7.0 documenta backend winit, DRM, GBM y módulos drm_syncobj, fractional_scale, session_lock y foreign_toplevel_list; presencia de API no es integración probada. ext-foreign-toplevel-list es intencionalmente mínimo y no cubre toda la gestión de ventanas: diseñar contrato autenticado del compositor para el shell. xdg-decoration negocia decoraciones; no asumir SSD universal. Diferenciar composición within-window (UI) y behind-window (compositor). No exponer textura del fondo a clientes arbitrarios. Fuentes: [Smithay backend](https://docs.rs/smithay/0.7.0/smithay/backend/), [Wayland](https://docs.rs/smithay/0.7.0/smithay/wayland/), [toplevel list](https://wayland.app/protocols/ext-foreign-toplevel-list-v1).

## Ampliación de protocolos candidatos
P0/P1: ext-background-effect-v1 (blur por región; soporte upstream a verificar para revisión Smithay elegida), cursor-shape, xdg-toplevel-icon, idle-notify, primary-selection, data-device (clipboard/DnD), tablet, keyboard-shortcuts-inhibit según casos. P1/P2: security-context (identidad de cliente sandbox proporcionada por launcher confiable, no reemplaza sandbox), xdg-session-management (restauración cooperativa, no recuperación transparente), DRM lease, color-management, explicit sync, tearing-control, fifo/commit-timing según soporte. [Análisis](../research/GRAPHICS_AND_PROTOCOLS.md). No exponer protocolos privilegiados a clientes arbitrarios. Adaptador KDE blur opcional; priorizar estándar. El protocolo de background-effect no transmite textura del fondo al cliente ni expresa toda la óptica SupraGlass.
