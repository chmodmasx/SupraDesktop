# Constitución de SupraDesktop

Requisitos ordenados por identidad del proyecto. Seguridad, accesibilidad, legalidad y estabilidad son restricciones transversales no negociables.

| # | Principio | Regla |
|---|---|---|
| 1 | 1:1 macOS Visual | Máxima fidelidad medible a la versión de referencia: paleta, materiales, blur, iluminación, geometría, tipografía, iconografía, sombras y animaciones. No conformarse con algo parecido. |
| 2 | AI Ready | Acciones y estado semánticos, contratos versionados, MCP, CLI, SDK y APIs bajo autorización granular. |
| 3 | Modular First | Dependencias unidireccionales; módulos comprobables, reemplazables y aislados cuando sea viable. |
| 4 | 1:1 macOS Experience | Gestos, navegación, organización de ventanas, flujos y comportamiento fieles. |
| 5 | Rust First | Rust para código propio salvo excepción técnica documentada. |
| 6 | Security by Design | Mínimo privilegio, consentimiento, aislamiento real, auditoría y revocación. |
| 7 | Performance First | Baja latencia y consumo; medir antes de optimizar. |
| 8 | Wayland Native | Wayland como plataforma; XWayland para compatibilidad. |
| 9 | Independent Desktop | Sin dependencia de una sesión KDE, GNOME o COSMIC. |
| 10 | Single Source of Truth | Un propietario por estado y una definición canónica por contrato o token. |
| 11 | Local First | Función local completa sin cuentas, cloud, modelos o proveedores obligatorios. |
| 12 | Linux Compatibility | Compatibilidad con Qt, GTK, Electron, Flatpak, AppImage, Steam, Wine y Proton, dentro de sus límites. |
| 13 | Accessibility First | Semántica, teclado, asistencia y preferencias de accesibilidad desde el diseño. |
| 14 | Open Source & Legal Clean | Licencias auditadas, recursos originales, atribución y ausencia de material propietario no autorizado. |
| 15 | Evidence over Assumptions | Investigar, medir, probar, documentar; nunca confundir compilación con finalización. |

## Resolución de conflictos
No sacrificar seguridad, legalidad o accesibilidad para alcanzar el aspecto visual. Documentar discrepancias y alternativas en ADR; no cambiar los principios sin aprobación explícita del mantenedor. No añadir alcance ajeno al propósito. Evitar duplicaciones, atajos permanentes, abstracciones sin necesidad y dependencias no justificadas. Toda regresión debe quedar visible.

## Alcance exacto de 1:1 macOS Visual (aclaración del mantenedor, 2026-11-24)
La interfaz debe reproducir visualmente macOS 1:1, no reinterpretarlo: colores, materiales, blur, transparencia, refracción, iluminación, sombras, geometría, tamaños, espaciado, layout, estados y animaciones. La excepción son los recursos artísticos y la identidad de marca: iconos, fondos, sonidos, logotipos y otros recursos serán originales o libres y auditados; tipografía libre con métricas ajustadas. Código propio e independiente. No cambiar parámetros de interfaz arbitrariamente para diferenciarse. Las excepciones técnicas, legales y de accesibilidad deben registrarse; no ocultarlas en la métrica de fidelidad. No usar recursos de diseño de Apple. Medir y reproducir de forma independiente; no afirmar que una implementación idéntica está verificada sin evidencia.
