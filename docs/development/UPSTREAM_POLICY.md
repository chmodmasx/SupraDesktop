# Política upstream
## Decisión
Definir requisito y prueba; evaluar dependencia sin cambios, extensión, parche upstream, fork/vendoring y solución propia. Elegir según fidelidad, rendimiento, accesibilidad, seguridad, compatibilidad y coste total. Si ninguna dependencia cumple, desarrollar nuestra implementación. No forzar abstracciones ni adoptar forks por comodidad.
## Registro
third_party/manifest.toml: componente, URL, commit, licencia efectiva, archivos de avisos, fuentes, parches, frontera de integración, procedimiento de actualización/rollback, responsable, justificación y pruebas. Mantener código upstream separado, historial o referencia exacta; no eliminar créditos al renombrar. Revisar licencias transitivas y obligaciones de distribución. Registrar cambios locales y evaluar actualización periódica. No incorporar código propietario ni recursos Apple. No descartar recursos libres por mero parecido.
## Aceptación
Pruebas del requisito que motivó la adaptación, regresiones de API/ABI, rendimiento y accesibilidad; documentar discrepancias. No declarar un fork mantenido hasta que tenga política de actualización, pruebas y fuente verificable. Licencia del núcleo sin ratificar.
