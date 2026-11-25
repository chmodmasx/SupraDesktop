# Puertas experimentales tempranas

Estado: NOT_RUN en todas. Registrar revisión, comandos, entorno, resultados, limitaciones, artefactos y decisión. No confundir revisión documental con ejecución. Fixtures propios y sesiones de prueba.

| ID | Pregunta | Evidencia necesaria |
|---|---|---|
| E01 | ¿Toolkit viable? | Misma UI en candidatos, resultados P0/P1 de TOOLKIT_EVALUATION |
| E02 | ¿Smithay anidado funciona? | Cliente xdg-shell, foco/resize, popup y frame sin alterar host |
| E03 | ¿Material reproducible? | Offscreen fixture, blur referencia, alpha, clipping y tolerancias |
| E04 | ¿Blur por región estándar? | Cliente de prueba, fallback, escala y límites de superficie |
| E05 | ¿Caché correcta? | Secuencia de ventanas sintéticas, equivalencia con redraw completo |
| E06 | ¿Accesibilidad y acciones? | Lectura por AT-SPI, teclado, estado estructurado y acción reversible |
| E07 | ¿Permisos verificables? | Denegar recurso no autorizado, consentimiento, revocación, auditoría en fixture aislado |
| E08 | ¿Lifecycle modular? | Terminar shell de prueba, recuperar servicio sin alterar resto |
| E09 | ¿Integración apps? | Qt/GTK/Electron de prueba, CSD/SSD, escala, clipboard y popup |
| E10 | ¿Portales compatibles? | Selección autorizada de superficie y sesión de prueba; cancelación |
| E11 | ¿Sesión nativa viable? | Intel/AMD/NVIDIA y KVM, DRM/KMS, explicit sync, hotplug |
| E12 | ¿Provenance y licencias? | Inventario, revisión upstream, derechos, source artifacts y avisos |
| E13 | ¿Fidelidad 1:1? | Corpus legítimo de referencia, ROI y mediciones reproducibles |
| E14 | ¿Rendimiento? | p95/p99, PSS, VRAM, consumo, dropped frames, escenarios definidos |
| E15 | ¿Packaging reversible? | sbuild/autopkgtest y sesión alternativa, rollback sin cambiar defaults |

Secuencia inicial E01–E07 en paralelo si contratos acordados, después E08–E10, E11/E15 en entorno dedicado. E12 transversal y antes de distribuir; E13 se inicia con fixtures sintéticos y se completa con referencia nativa; E14 en cada etapa. No bloquear todo M00 por disponibilidad de macOS físico, pero no declarar 1:1 hasta obtener evidencia.
