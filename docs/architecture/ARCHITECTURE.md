# Arquitectura

Capas: plataforma Linux → compositor/renderer → UI y servicios → shell → aplicaciones. Los contratos de dominio (tipos, acciones, eventos, configuración) son dependencias inferiores comunes. Ninguna dependencia circular ni dependencia shell→shell; no crear un crate por función trivial.

| Área | Propiedad y límites |
|---|---|
| supra-compositor | Autoridad sobre ventanas, foco, escena, entrada, salidas, escritorios, protocolos, sesiones |
| supra-scene / renderer | Composición, damage tracking, caché, presentación, GPU; no lógica de aplicaciones |
| supra-glass / materials | Motor óptico y recetas semánticas independientes, sin acceso a datos de aplicaciones |
| supra-ui / text / accessibility | Controles, layout, semántica y renderizado within-window |
| supra-actions / ipc / config | Contratos tipados, registro, versiones, configuración atómica |
| shell | Procesos independientes por responsabilidad; Dock, Menu, Overview, Control, etc. |
| services | Adaptadores D-Bus y propietarios de estado de dominio |
| apps | Clientes de contratos; sin acceso directo a internos del compositor |
| agents | Adaptadores autorizados, no autoridad del sistema |

Compositor: backend anidado primero, luego DRM/KMS; separar input, output, focus, workspace, layout, gesture, capture, scheduler, xwayland, security, diagnostics. Calloop no bloqueado por red/disco/servicios; Tokio solo donde corresponda. IPC asíncrono con límites de colas, timeouts, cancelación, snapshots y eventos con secuencia. Identidad y autorización verificadas por recurso. La caída del compositor puede cerrar clientes; no garantizar recuperación transparente. Fallo de shell no debe provocar caída del compositor.

## Convenciones
Un Cargo workspace virtual se introduce al existir el primer crate real. Aplicaciones binarias y bibliotecas con APIs pequeñas y tests. Interfaces de backend reemplazables donde haya necesidad real; no abstracción prematura. El árbol de carpetas inicial es un mapa, no código implementado.

## Proceso de decisión
Cambios de dependencias, APIs, licencias, modelo de seguridad y pipeline requieren ADR. Los límites se comprueban con cargo metadata y reglas de dependencias cuando exista código.

## Infraestructura transversal S01–S15
SupraIcon, SupraDecoration, SupraLayout, virtualización, SupraPreferences y SupraTokens son responsabilidades candidatas, no necesariamente un crate por nombre. Separar diseño/medición de generación y runtime. FileOps, preview, drag/drop, widgets, sesión, global menu, sound, share/continuity y shortcuts consumen contratos existentes; no crear segunda autoridad de estado, permisos o acciones. [Especificaciones](../specifications/subsystems/README.md).

## Plataforma interna y Applications
[Especificaciones](../specifications/platform/README.md). Scene snapshot autoritativo y render graph acotado, pools/atlas separados de buffers cliente; calloop compositor y servicios async con colas acotadas, IPC control-plane y data-plane separados; AppRegistry reúne identidad/instalación/instancia/ventanas sin confundir PID con app. Providers APT/Flatpak/portable, vista unificada y bundle opcional. No segunda autoridad de acciones o permisos. Plugins de terceros fuera de proceso crítico. Diagnóstico local con datos mínimos.
