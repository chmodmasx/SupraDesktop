# Registro de acciones (propuesta)

Cada acción declara id versionado, descripción, JSON Schema de entrada/salida, recurso, permisos, nivel de sensibilidad, efectos, posibilidad de vista previa/undo, timeout y errores. Ejemplos no implementados: windows.list, windows.focus, windows.resize, workspaces.create, appearance.set_theme, audio.set_volume, applications.launch, files.search, notifications.list. No ofrecer ejecución arbitraria privilegiada.

Ciclo: solicitud → validación y autorización → preview cuando posible → consentimiento independiente si corresponde → ejecución con precondiciones → verificación → auditoría y datos de reversión. Revalidar al ejecutar, evitar carreras, cancelar y revocar; si undo imposible informar antes. Eventos sugeridos: window.created, window.focus_changed, appearance.changed, display.connected, task.completed, permission.revoked. Datos no confiables nunca son instrucciones.
