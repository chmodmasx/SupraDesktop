# Registro de investigación

Compilación de referencias discutidas durante la planificación (24-11-2026). No constituye una nueva verificación de versiones, commits, licencias o cifras; los valores de terceros son hipótesis hasta reproducirlos. Registrar URL exacta, fecha, versión/commit, licencia, afirmación, método y evidencia al validar. No copiar kits/recursos propietarios al repo.

## Diseño macOS
- [Apple Design Resources](https://developer.apple.com/design/resources/) — kits oficiales; localizar artefacto exacto macOS 27 Sketch 27.0.3 reportado, 28-10-2026.
- [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) — materiales, controles y accesibilidad.
- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/) — explicación oficial del concepto.
- [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview) — composición behind/within-window.
- [macOS 27 Design Skill](https://skills.haythamasalama.me/skills/apple-macos-27-design) — extracción reportada de tokens; confirmar fuente y versión.
- [MaterialView](https://github.com/OskarGroth/MaterialView), [Liquid Glass React](https://github.com/medfa12/liquid-glass-react), [Liquid Glass Research](https://github.com/emribilemir/liquid-glass-research), [macOS Liquid Glass](https://github.com/i-am-logger/macos-liquid-glass) — pistas de terceros para calibración, no especificaciones oficiales. Comprobar disponibilidad y licencias.

## Plataforma
- [Smithay](https://github.com/Smithay/smithay), [client toolkit](https://github.com/Smithay/client-toolkit), [Wayland protocols](https://wayland.app/protocols/), [WLCS](https://github.com/canonical/wlcs).
- [COSMIC](https://github.com/pop-os/cosmic-epoch), [cosmic-comp](https://github.com/pop-os/cosmic-comp), [libcosmic](https://github.com/pop-os/libcosmic), [Niri](https://github.com/niri-wm/niri) — arquitectura y renderizado.
- [Iced](https://github.com/iced-rs/iced), [AccessKit](https://github.com/AccessKit/accesskit), [Inter](https://github.com/rsms/inter) — UI y accesibilidad.
- [XDG Desktop Portal](https://github.com/flatpak/xdg-desktop-portal), [COSMIC Portal](https://github.com/pop-os/xdg-desktop-portal-cosmic) — portales.
- [PipeWire](https://pipewire.org/), [libei](https://gitlab.freedesktop.org/libinput/libei), [Polkit](https://github.com/polkit-org/polkit), [AT-SPI2](https://gitlab.gnome.org/GNOME/at-spi2-core).

## AI Ready
- [MCP](https://modelcontextprotocol.io/), [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) — protocolo y adaptador.
- [Vercel Agent Desktop](https://github.com/vercel-labs/agent-desktop) — referencia reportada para interacción semántica; verificar.
- [Bubblewrap](https://github.com/containers/bubblewrap) — candidato de aislamiento, no garantía por sí mismo.
- [OWASP GenAI](https://genai.owasp.org/) — análisis de amenazas, prompt injection y acciones de agentes.

## Pendientes
Fijar build nativo de macOS, permisos de uso de referencia y corpus; extraer valores verificables; medir blur efectivo, paleta, sombras, refracción, curvas de animación, tipografía y geometría; comparar toolkit y backends; auditar licencias y amenazas; reproducir benchmarks. No presentar capturas o números no medidos como resultados.


## Segunda revisión
[Validación upstream](UPSTREAM_VALIDATION.md). Las referencias de kits y extracciones anteriores se conservan como historial no operativo, no como autorización ni fuente de tokens. No utilizar recursos de Apple. Priorizar documentación pública conceptual, observaciones permitidas y mediciones independientes.

## Iconografía
- [WhiteSur Icon Theme, revisión 73d8040](https://github.com/vinceliuice/WhiteSur-icon-theme/tree/73d8040da51a9ed74e47c7366e7e9ff437601a5c): candidato GPL v3. [COPYING](https://github.com/vinceliuice/WhiteSur-icon-theme/blob/73d8040da51a9ed74e47c7366e7e9ff437601a5c/COPYING), [AUTHORS](https://github.com/vinceliuice/WhiteSur-icon-theme/blob/73d8040da51a9ed74e47c7366e7e9ff437601a5c/AUTHORS), [install.sh](https://github.com/vinceliuice/WhiteSur-icon-theme/blob/73d8040da51a9ed74e47c7366e7e9ff437601a5c/install.sh). README describe estética Big Sur; instalador incluye opción de reemplazar logo Apple y no copia COPYING/AUTHORS por defecto (línea comentada). Auditoría por recurso pendiente; no importar todavía.

## Revisión técnica ampliada
- [Toolkit y prototipos](TOOLKIT_EVALUATION.md).
- [Composición, protocolos y gráficos](GRAPHICS_AND_PROTOCOLS.md).
- [Integración Linux y ciclo de sesión](LINUX_INTEGRATION.md).
- [Inventario visual y de interacción](../reference-macos27/INTERACTION_MATRIX.md).
- [Puertas experimentales M00/M01](../testing/EXPERIMENT_MATRIX.md).
- [Interoperabilidad de agentes](../ai-native/INTEROPERABILITY.md).

## Revisión avanzada
[Índice de fidelidad](../reference-macos27/fidelity/README.md): geometría, animaciones, Dock, ventanas y menús, gestos, scroll, óptica, texto, controles, monitores, gestión de sesión y aplicaciones. Referencias públicas por documento; no kits ni recursos Apple. Consulta documental 2026-11-24; mediciones nativas pendientes.

## Candidatos complementarios
[Kurbo](https://github.com/linebender/kurbo) curvas Rust; [Parley](https://github.com/linebender/parley) layout enriquecido; [cosmic-text](https://github.com/pop-os/cosmic-text) layout bidi; [Tantivy](https://github.com/quickwit-oss/tantivy) full text; [DRM/KMS](https://docs.kernel.org/gpu/drm-kms.html) modos y color; [Wayland color management](https://wayland.app/protocols/color-management-v1). Revisión documental, no importación ni selección definitiva.

## Investigación de subsistemas S01–S15
[Índice](../specifications/subsystems/README.md) contiene referencias primarias y candidatos, con fuentes por área (Icon Composer, freedesktop, Qt, GTK, Taffy, DTCG, Quick Look, Wayland, WASI, systemd, LocalSend, App Intents). Consulta documental, no mediciones ni importación. [Puertas](../testing/SUBSYSTEM_VALIDATION.md).

## Investigación de plataforma interna
[Índice A00/P16–P30](../specifications/platform/README.md): fuentes por subsistema (AppDir/AppImage/Flatpak/helloSystem/Apple Bundles, Smithay, etagere, xkbcommon, Unicode, AccessKit/Orca, systemd, calloop/Tokio/zbus, UPower, portals, IronRDP, Fluent/ICU4X, Rust ABI/WIT, Freedesktop Notifications, BlueZ/UDisks2, tracing). Consulta documental, 2026-11-24. Sin resultados de ejecución.

## Distribución Arch atómica
[Investigación y referencias](../distribution/README.md), [actualizaciones](../distribution/DEPLOYMENT.md), [AUR](../distribution/APPLICATIONS_AUR.md), [drivers](../distribution/KERNEL_EXTENSIONS.md), [build](../distribution/BUILD_RELEASE.md). Fuentes verificadas documentalmente 2026-11-24; no se ha ejecutado una VM ni creado imágenes.
