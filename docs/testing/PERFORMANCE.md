# Presupuestos propuestos (sin benchmark)

Base 1080p en reposo: RAM PSS agregada <500 MB, VRAM atribuible <256 MB, CPU <1% de un núcleo en condiciones controladas. Objetivo 60 FPS y alta frecuencia si hardware permite; presupuesto 16.67 ms a 60 Hz, 8.33 ms a 120 Hz. Búsqueda visible <100 ms, recuperación de shell <2 s; no crecimiento sostenido de memoria. Medir p50/p95/p99 frame time y latencia, dropped frames, GPU/CPU, PSS/VRAM, potencia, arranque y carga. Precisar idle, hardware, drivers, refresh y escenarios; no comparar cifras incompatibles.

Perfiles básico (material opaco o transparencia simple), equilibrado (blur/vibrancy y reflejos limitados), completo (refracción/iluminación/dispersion). Accesibilidad puede forzar opacidad. Damage tracking, caché, pooling, occlusion y direct scanout. Probar integradas Intel/AMD y NVIDIA en hardware real; KVM no sustituye drivers reales.
