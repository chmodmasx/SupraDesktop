# SupraRenderer / SupraGlass

Pipeline candidato: escena y visibilidad → backdrop situado detrás del material → espacio cromático definido → pirámide blur → SDF/curvatura/normales → refracción y muestreo → vibrancy/tinte → Fresnel/reflejos/dispersión → máscaras/bordes/sombras → composición premultiplied alpha → presentación. Orden sujeto a calibración; referencia gaussiana separada de Dual Kawase optimizado. Separar blur behind-window (compositor) y within-window (toolkit); no inferir regiones internas de apps externas.

Cache por salida y región de daño; invalidar al cambiar contenido inferior, escala, color, geometría, material o foco. Evitar muestreo de superficies superiores/protegidas. Texture pooling, clipping correcto, occlusion y direct scanout cuando no se requiera composición. Escalado fraccional, múltiples pantallas, perfiles SDR/HDR, explicit sync. Fallback sin shader y opaco para accesibilidad/fallo. GLES/EGL inicial; Vulkan solo tras benchmark y ADR.

SupraLab debe renderizar recetas y controles aislados, exportar capturas/metadata y comparar con patrones deterministas. Validar bordes, costuras, alfa, gamut, sombras, refracción y movimiento. No llamar Liquid Glass a una mera transparencia.
