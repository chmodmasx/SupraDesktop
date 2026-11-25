# ADR-0007 — Iconografía libre y modular

Estado: PROPOSED. El mantenedor propuso WhiteSur Icon Theme como base; no es aprobación de todos sus recursos ni elección de licencia del núcleo.

## Evidencia
Repositorio [vinceliuice/WhiteSur-icon-theme](https://github.com/vinceliuice/WhiteSur-icon-theme), revisión consultada 73d8040da51a9ed74e47c7366e7e9ff437601a5c. COPYING contiene GPL versión 3 y AUTHORS atribuye a Vince Liuice. README indica inspiración Big Sur, variantes, iconos alternativos y opción de sustituir el logotipo Apple. El script de instalación tiene comentada la copia de COPYING/AUTHORS. No asumir que cada recurso tiene procedencia lícita por la licencia general.

## Propuesta
Proveedor de iconos separado, basado en nombres semánticos y estándar freedesktop (index.theme, herencia y fallback). Paquete Debian independiente candidato supradesktop-icons-whitesur, fuentes y parches versionados, sin dependencia del compositor sobre WhiteSur. Permitir sustitución por cualquier tema y recursos propios. Adaptar geometría, variantes y estilo a la referencia macOS 27 con mediciones independientes. Crear marca SupraDesktop propia.

## Puerta previa a importar o distribuir
- Inventariar procedencia y licencia por recurso o grupo verificable; excluir marcas Apple, archivos de procedencia dudosa y recursos propietarios.
- Conservar COPYING, AUTHORS, avisos existentes, indicar modificaciones y fechas y cumplir obligaciones GPL de fuentes correspondientes y distribución de derivados. No depender de que el instalador copie avisos.
- Auditar SVG, referencias externas, enlaces simbólicos, herencia y scripts; staging reproducible sin ejecutar instalador en host principal.
- Verificar cobertura, escalas, light/dark y fallback, y compatibilidad de licencias. Separar paquete no implica automáticamente ausencia de obligaciones GPL; evaluar forma de integración.
- Mantener identidad de proyecto y no afirmar que iconos Big Sur son 1:1 con macOS 27.

Alternativas: arte propio completo, otros temas libres auditados, combinación mediante herencia. No se han copiado iconos ni ejecutado el instalador. Licencia del núcleo permanece pendiente.
