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
