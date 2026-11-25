# Composición gráfica y protocolos — revisión documental

Fuentes: [Smithay GlesRenderer](https://smithay.github.io/smithay/smithay/backend/renderer/gles/struct.GlesRenderer.html), [RenderElement](https://docs.rs/smithay/latest/smithay/backend/renderer/element/index.html), [renderer](https://smithay.github.io/smithay/smithay/backend/renderer/index.html), [Linux DRM/KMS](https://docs.kernel.org/gpu/drm-kms.html).

Smithay expone primitivas de shaders y damage tracking; no equivale a un motor Liquid Glass listo. Crear prototipo offscreen: textura sintética -> blur de referencia -> composición -> lectura de fixture; luego material detrás de superficie en compositor anidado. Mantener materiales dentro de ventana en toolkit. No compartir texturas privadas entre clientes. El compositor tiene autoridad sobre escena y composición.

## Hallazgo: protocolo de blur
[ext-background-effect-v1](https://wayland.app/protocols/ext-background-effect-v1) permite pedir efectos de fondo por región. [Niri Window Effects](https://github.com/niri-wm/niri/blob/main/docs/wiki/Window-Effects.md) documenta uso en ventanas y layer surfaces. Priorizar estándar y negociar capacidades; fallback a superficie opaca o translúcida simple cuando falte. [KDE blur](https://wayland.app/protocols/kde-blur) candidato de compatibilidad. No confundir solicitud de blur con radio, refracción, tintes o iluminación arbitrarios.

## Render y calidad
- Espacio de trabajo explícito: comparar composición lineal y perceptual contra referencia; definir conversión entrada/salida, alfa premultiplicada y orden de filtros. No asumir sRGB para todos los monitores.
- Separar blur de sombras, blur efectivo y distorsión óptica. Referencia gaussiana y candidato Dual Kawase: comparar respuesta de borde/impulso, frecuencia y pérdida cromática.
- Clipping SDF y antialiasing a escala fraccional; probar radios continuos y esquinas sin fugas.
- Damage tracking incluye huella de blur/refraction, posición, z-order, perfiles y cambios de estado; comparar contra redraw completo en secuencia sintética.
- Texturas reutilizadas, memoria acotada, degradación de efectos, evitar readback en frame interactivo.
- Backdrop fijo vs dinámico: caché solo cuando entradas realmente invariantes; probar ventana inferior moviéndose y múltiples superficies translúcidas.
- DRM/KMS atomic, fences, DMA-BUF y direct scanout requieren validación real; un compositor anidado no prueba hardware. Mantener explicit sync, multi-output, hotplug y escalas distintas como escenarios.

## Protocolos complementarios
[security-context](https://wayland.app/protocols/security-context-v1), [session-lock](https://wayland.app/protocols/ext-session-lock-v1), [toplevel-icon](https://wayland.app/protocols/xdg-toplevel-icon-v1), [session management](https://wayland.app/protocols/xdg-session-management-v1), [color management](https://wayland.app/protocols/color-management-v1). Session lock debe presentar frame seguro en todas salidas antes de confirmar bloqueo; si lock surface desaparece, fallback sólido. Session management requiere cooperación de clientes; no garantiza restauración de procesos. Security context no es identidad autoafirmada por cliente arbitrario; comprobar procedencia del launcher y políticas.

Estado: evidencia de documentación, versiones y disponibilidad exactas a fijar al probar.
