# Validación

Separar pruebas unitarias, integración, conformidad Wayland (WLCS), visual, rendimiento, accesibilidad, fallo, permisos y packaging. Registrar commit, hardware, drivers, perfil gráfico, escala, resolución, comandos, fixtures y resultados. Estados: PASS, FAIL, BLOCKED, INFRA_INVALID, NOT_RUN; no ocultar omisiones. No afirmar PASS sin evidencia.

Visual: ΔE00 <1 para sólidos, geometría ≤1 px lógico, blur y sombras error <5%, alfa <1 punto porcentual, animación <5%, tipografía ≤1 px en casos seleccionados, refracción error mediano <1 px, SSIM >0.98 en regiones comparables. Son metas propuestas, no mediciones. Definir métrica exacta, ROI y corpus por requisito. Separar screenshots sintéticos públicos de referencias Apple restringidas. Probar light/dark, foco, estados, alto contraste, reducción de transparencias/movimiento.

Fallos: Dock/Control/Indexer caen sin arrastrar compositor; fallback shader; configuración inválida recuperable; servicios ausentes degradan individualmente; lock fail-closed; compositor caído retorno controlado a login (no garantía de mantener apps). IA: pruebas negativas de autorización, aislamiento y revocación, protección de datos, consentimiento y auditoría. Integración: Intel/AMD/NVIDIA, KVM/VirtIO, software renderer, sesiones anidadas antes de hardware real. No pruebas destructivas en host principal.
