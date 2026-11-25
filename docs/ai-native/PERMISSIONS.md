# SupraTrust — permisos

Denegar por defecto. Identidad por agente/sesión, recursos limitados, expiración, revocación, cancelación y política aplicada en backend. Niveles: 0 observación no sensible con permiso básico; 1 cambios reversibles; 2 modificaciones scoped; 3 datos personales/captura/portapapeles con consentimiento específico; 4 privilegios e irreversibles con confirmación y autenticación separadas; 5 credenciales y controles de seguridad no accesibles directamente. Las clasificaciones dependen del recurso, no solo del nombre de la acción.

Permisos una vez, sesión o persistentes de mínimo alcance; usuario puede revisar y retirar en Agent Manager. Confirmaciones en UI confiable fuera del control del agente. Polkit y portales cuando corresponda. No permitir al agente concederse permisos. Auditoría con redacción, retención limitada y sin contenido sensible por defecto. Detener y revocar sesiones mediante control humano independiente.
