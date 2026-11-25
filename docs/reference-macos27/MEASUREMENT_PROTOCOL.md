# Protocolo de medición independiente para fidelidad 1:1

Estado PROPOSED. No utilizar kits, fuentes, iconos, sonidos, fondos ni recursos Apple. Usar observación permitida de un sistema al que se tenga acceso legítimo y patrones propios. Capturas y datos de referencia solo con permisos correspondientes; no publicar material no autorizado. El alcance es reproducción de interfaz, no reinterpretación artística.

## Metadatos
Build exacto macOS y app, hardware, resolución, escala lógica/física, perfil de color, SDR/HDR, frecuencia, apariencia, acento, foco, accesibilidad, estado, fondo sintético y hash, método de captura, formato sin pérdida, ROI, procedencia, fecha y revisión de derechos. Repetir casos variables y registrar dispersión. No tratar capturas de internet comprimidas como referencia exacta.

| ID | Experimento | Resultado |
|---|---|---|
| V01 | Fondos uniformes y estados equivalentes | RGB en espacio definido, ΔE00 |
| V02 | Fondos negro, blanco, gris y colores | Alfa y tinte estimados, residuales de composición |
| V03 | Patrones de borde, impulso y barras propios | Perfil de blur, sigma efectiva si modelo gaussiano válido |
| V04 | Rejilla propia bajo material | Desplazamiento óptico en píxeles lógicos, centro y bordes |
| V05 | Ventana sobre fondo uniforme, activa e inactiva | Perfil de sombra, offset, intensidad |
| V06 | Contornos, padding y posiciones a escalas distintas | Geometría, curvatura y alineación |
| V07 | Texto propio en varios pesos/tamaños/idiomas | Baseline, anchura, altura, espaciado, contraste |
| V08 | Secuencia temporal a frecuencia conocida | Duración, curva y trayectoria de animaciones |
| V09 | Matriz de apariencia, foco, hover, disabled y accesibilidad | Comportamiento de estados |
| V10 | Recorridos Dock, menú, Spaces, Settings, Files | Transiciones, entradas y estado final |

## Evaluación
Separar fidelidad respecto de referencia autorizada de regresión frente a baseline propio. Excluir del cálculo las áreas artísticas originales declaradas antes de medir, no los errores de interfaz. No usar SSIM global como único criterio. Comparar perfiles, geometría y ΔE00 por ROI, adjuntar residuales y limitaciones. Guardar referencia observada separada del parámetro de implementación. Si un efecto no puede igualarse, abrir una discrepancia verificable, no rebajar silenciosamente el objetivo.

No hay corpus nativo, capturas ni resultados verificados todavía. SupraLab puede iniciar con fixtures sintéticos propios.
