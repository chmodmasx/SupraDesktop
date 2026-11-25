# Matriz de referencia visual y funcional

Fuentes conceptuales públicas: [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos), [Menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar), [Menus](https://developer.apple.com/design/human-interface-guidelines/menus), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Materials](https://developer.apple.com/design/human-interface-guidelines/materials). No utilizar kits de Apple.

| Área | Escenarios que deben especificarse y medirse |
|---|---|
| Ventanas | activa/inactiva, resize por borde, doble clic titlebar, controles hover, maximizar, fullscreen, cierre y minimizar, ventanas modales, CSD/SSD |
| Dock | icono fijo/en ejecución/activo, magnificación por distancia, separadores, recents, papelera, menú, auto-hide, transición minimizar, posición y múltiples pantallas |
| Menu Bar | nombre app, menú de sistema propio, menús y submenús, teclado, shortcuts, elementos deshabilitados, overflow de indicadores, pantalla completa |
| Control Center | apertura/cierre, sliders, estados Wi-Fi/Bluetooth, paneles expandidos, fondo oscuro/claro y movimiento |
| Notificaciones | banner, agrupación, interacción, estado sin conexión, historial, concentración |
| Spaces/Overview | gesto cancelado y completado, desplazamiento, mover ventana, miniaturas, fullscreen y monitor externo |
| Stage Manager | selección, grupos, orden, ventanas superpuestas, interacciones con Spaces |
| Spotlight | activación, búsqueda, categorías, resultados, teclado, acciones, historial opcional y errores |
| Files | iconos/lista/columnas/galería, selección múltiple, drag/drop, etiquetas, Quick Look, diálogos y estados de copia |
| Settings | navegación, búsqueda, paneles, switches, resize, teclado y accesibilidad |
| UI común | botones, foco, hover, pressed, disabled, text fields, menus, separators, tabs, switches, selection, scroll edge |
| Tipografía y layout | métricas de fuente libre, jerarquía, baseline, clipping, RTL, cambio escala, nombres largos |
| Iconografía | tamaños y posiciones, variantes, contraste, consistencia; recursos libres auditados o propios, no exigir copia de arte |

Cada caso se divide en estado inicial, acción, transición, estado final, reglas de cancelación, permisos, a11y, metadatos de referencia y tolerancias. Los parámetros exactos y animaciones siguen sin medir. No presentar HIG como especificación pixel-perfect. No sustituir resultados ausentes por estimaciones inventadas.
