# Contratos IPC y acciones

D-Bus/zbus candidato para servicios; protocolos Wayland para superficies y funciones gráficas. Contrato versionado con identificador estable, esquema de argumentos y resultado, permisos, efectos, reversibilidad, errores, timeout/cancelación y correlación. Un solo handler de dominio para UI, CLI, SDK y MCP; cada entrada verifica autorización de su identidad. No exponer estado interno mutable.

Estado mediante snapshots versionados y eventos ordenados; reconectar y resincronizar ante pérdida. Idempotencia donde sea posible, precondiciones de revisión para evitar carreras, límites de tamaño y frecuencia. Identificadores opacos scoped por sesión y recurso. Nunca confiar en identidad declarada por el propio cliente. Las especificaciones concretas y transportes quedan pendientes de ADR/prototipo.
