# ADR-0003 — Límites modulares
Estado: PROPOSED. Modular First es requisito aprobado. Monorepo Cargo workspace; bibliotecas para lógica pura, procesos separados para shell/servicios donde viable; contratos versionados y autoridad única. Alternativas: monolito, microservicios excesivos. Costes: IPC, lifecycle y pruebas. Revisar al medir fallos y latencia. No crear crates vacíos.
