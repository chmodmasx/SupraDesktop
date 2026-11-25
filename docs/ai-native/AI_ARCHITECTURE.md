# AI Ready — SupraAI

Principio #2 transversal. No depende de proveedor, LLM, suscripción ni cloud. Desinstalar o desactivar IA no afecta el escritorio. Cobertura de acciones autorizables, no acceso ilimitado.

## Capas
Agentes locales/remotos autorizados → MCP/CLI/SDK → SupraAgent Gateway → SupraTrust → acciones y servicios de dominio. UI humana y agentes comparten handlers tipados, no políticas duplicadas. Preferir API nativa, después AT-SPI semántico para apps externas, último recurso captura/entrada autorizada por portales. En apps propias SupraUI registra IDs estables, roles, estados, acciones, eventos y permisos. Ninguna captura permanente ni transmisión automática de todo el escritorio.

## Capacidades
Ventanas, escritorios, apps, archivos autorizados, apariencia, settings, audio, pantallas, red, Bluetooth, hardware y diagnósticos, notificaciones, portapapeles, procesos permitidos, paquetes con aprobación, automatización. MCP descubre herramientas según permisos y tarea; recursos mínimos, resultados estructurados, paginación y eventos. Integraciones previstas Hermes Agent, OpenCode, Codex, Claude Code, OpenClaw y clientes MCP genéricos.

## Componentes
supra-actions, supra-agent-sdk, supra-capabilities, supra-context, supra-permissions, supra-transactions, supra-audit; gateway, MCP, supervisor/runtime; SupraTrust, eventos, automatización; Agent Manager, CLI. Crear módulos cuando tengan código útil. Sesiones gráficas anidadas o headless aisladas para agentes, sin interrumpir sesión humana; Spaces no es aislamiento. Proteger credenciales, interfaces de sesión y red.

## Aceptación
100% de acciones propias compatibles con automatización expuestas de forma segura, 100% controles propios semánticos, auditabilidad de acciones mediadas, cero bypass conocidos en corpus negativo, funcionamiento sin IA y sin red; no afirmar seguridad absoluta. Reversión cuando viable, confirmación independiente para efectos sensibles.
