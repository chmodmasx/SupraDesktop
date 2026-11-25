# SupraMCP

Adaptador del registro de acciones, no backend paralelo. Namespaces candidatos supra.desktop.*, supra.windows.*, supra.apps.*, supra.files.*, supra.ui.*, supra.settings.*, supra.appearance.*, supra.hardware.*, supra.audio.*, supra.network.*, supra.notifications.*, supra.diagnostics.*, supra.automation.*, supra.permissions.*. Descubrimiento limitado al permiso efectivo y contexto. Preferir stdio local; remoto opt-in con transporte autenticado y autorización según especificación vigente; sin listener público por defecto. No aceptar identidad por parámetros del modelo. El acceso a herramientas no otorga privilegios; autorización en cada invocación, revocación, límites, auditoría. Nunca publicar secretos en resultados, recursos o descripciones. SDK candidato [Rust MCP SDK](https://github.com/modelcontextprotocol/rust-sdk). Versiones y conformidad pendientes.

## Interoperabilidad
[Especificación complementaria](INTEROPERABILITY.md). Autorización de transporte MCP no sustituye autorización de dominio; no reenviar tokens de otros servicios. Fijar revisión de protocolo y clientes después de pruebas. Sin exposición HTTP pública por defecto.
