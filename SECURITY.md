# Seguridad

Estado preimplementación. No existe aún software de producción. Reportar problemas sensibles mediante un canal privado acordado con el mantenedor; no publicar credenciales, datos reales ni detalles sensibles en issues públicos. La disponibilidad de GitHub Private Vulnerability Reporting debe confirmarse antes de utilizarlo.

El modelo de amenazas está en [docs/ai-native/THREAT_MODEL.md](docs/ai-native/THREAT_MODEL.md). Agentes sin acceso root permanente, sin acceso implícito a secretos y sin capacidad de autoaprobar privilegios. Pantalla de bloqueo fail-closed, captura/entrada autorizadas y aislamiento efectivo. Nunca usar la sesión gráfica real para pruebas destructivas. No se declara seguridad verificada hasta contar con pruebas y revisión.
