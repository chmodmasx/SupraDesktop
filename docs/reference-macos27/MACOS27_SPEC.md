# Inventario macOS 27 (referencia inicial)

La referencia visual debe quedar fijada por build, idioma, escala lógica/física, perfil de color, apariencia, wallpaper, foco, configuración de accesibilidad y estado del control. No mezclar Sonoma, Sequoia, Tahoe y macOS 27 sin etiquetar procedencia. Las cifras de kits no son mediciones nativas. Véase [materiales](../specifications/MATERIALS.md).

| Área | Requisitos visuales y funcionales |
|---|---|
| Ventanas | Esquinas continuas, controles de ventana, titlebar, sidebar, toolbar, estados activos/inactivos, sombras, resize, maximizar/minimizar |
| Dock | Anclaje, ampliación progresiva, rebote, indicadores, autoocultar, drag/drop, recents, separadores, stacks, papelera, minimización |
| Menu Bar | Menú del sistema original, app activa, menú exportado, indicadores, reloj, adaptación al fondo |
| Spaces/Mission Control | Miniaturas, gestos, navegación, fullscreen en espacio dedicado, Exposé, split view, mosaicos, hot corners, show desktop |
| Stage Manager | Grupos de ventanas y navegación; validar comportamiento exacto |
| Spotlight | Búsqueda apps/archivos/contenido, cálculo, acciones, historial opcional de portapapeles |
| Control Center | Wi-Fi, Bluetooth, audio, pantalla, concentración, paneles expandibles |
| Notification Center | Agrupación, acciones, historial, widgets y estados |
| Finder | Iconos/lista/columnas/galería, pestañas, etiquetas, favoritos, ubicaciones, búsqueda, papelera, Quick Look |
| Settings | Categorías, búsqueda, paneles, coherencia de controles |
| Lock/Login | Estados seguros; no replicar marca o credenciales propietarias |
| Apps | Preview, Terminal, Activity Monitor, Archive, utilidades y suite complementaria |

## Corpus
Capturas propias lícitas de referencia: fondo uniforme, gradiente, rejilla, patrón de borde/impulso, alto contraste, fotografía; estado activo/inactivo/hover/pressed/disabled/focused/selected. Vídeos de animaciones a frecuencia conocida y trazas de gestos; región de interés y metadatos. No subir recursos propietarios o datos personales. Mantener fixtures sintéticos públicos.

## Límites
No se garantiza identidad literal de fuentes, iconos o recursos Apple. No implementar iCloud, iMessage o AirDrop como si fueran servicios compatibles. Priorizar equivalentes propios interoperables. Verificar cada comportamiento y medidas específicas en sistema real antes de cerrar requisito.

## Alcance exacto
Comparar todos los elementos de interfaz, incluidos materiales, iconos de controles funcionales, geometría, distribución, estado y movimiento. La ilustración artística, los iconos de aplicación, sonidos, fondos, marca y fuentes propietarias no se copian: usar equivalentes propios/libres con dimensiones y alineaciones comparables. Para métricas, excluir únicamente las regiones artísticas declaradas previamente; no excluir fallos de layout, tipografía, sombras o materiales. [Protocolo](MEASUREMENT_PROTOCOL.md).
