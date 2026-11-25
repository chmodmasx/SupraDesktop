# Modelo de amenazas inicial

Activos: archivos, credenciales, sesión gráfica, pantalla bloqueada, acciones privilegiadas, red, información de terceros, configuración y disponibilidad. Adversarios: agente comprometido o defectuoso, contenido externo con instrucciones maliciosas, cliente local no autorizado, servicio externo y widget no confiable.

Fronteras: procesos del usuario vs compositor/servicios; agente aislado vs usuario; portal vs app; datos externos vs instrucciones autorizadas; conexión remota vs local. Un agente ejecutado sin restricciones como el mismo usuario puede evitar el gateway: no prometer mediación completa en ese caso. Aislar procesos no confiables con identidades, espacios de nombres, filesystem y red restringidos; validar mecanismo elegido (Bubblewrap/servicios gestionados u otros) antes de afirmar aislamiento. No montar sockets de sesión o credenciales indiscriminadamente. No usar privilegios root permanentes.

Mitigaciones: menor privilegio, comprobación de identidad, autorización por operación y recurso, consentimiento fuera de la superficie controlada, límites de datos y recursos, red denegada salvo política, protección de logs, revocación y confirmación de operaciones sensibles. La captura/entrada visual requiere scope y consentimiento; suspender en lock; no capturar secretos. No exportar datos por defecto. Fallos deben cerrar permisos, no abrirlos.

Pruebas negativas: agente sin permiso, recurso fuera de scope, permiso expirado/revocado, intento de acceso por API alternativa, datos no confiables solicitando nuevas acciones, fuga de información vía logs o salida, caída de supervisor/lock, agotamiento de recursos. Usar fixtures inocuos y sesiones aisladas. Auditoría real pendiente.
