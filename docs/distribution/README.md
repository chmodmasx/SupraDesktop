# Distribución oficial candidata — Arch atómico
Objetivo: experiencia integrada tipo macOS, control de stack y actualización coherente, sin convertir SupraDesktop en dependencia de Arch. Nombre de distro y relación con SupraLINUX actual pendientes de decisión. No migrar proyecto existente. Estado PROPOSED; no imagen ni prototipo.
## Diseño inicial
Arch x86-64, snapshot coherente de repositorios, PKGBUILD propios, imagen versionada y firmada, raíz protegida de solo lectura, datos persistentes, kernel LTS candidato, firmware y drivers por imagen, Wayland/XWayland. Flatpak, AppImage/AppDir, SupraBundle opcional; AUR encapsulado o extensión excepcional; sin APT/dpkg ni proveedor .deb oficial. Pacman en build y staging, no actualización in-place habitual. Distro no obliga a usar IA.
## Documentos
- [Despliegues y rollback](DEPLOYMENT.md)
- [Construcción, seguridad y releases](BUILD_RELEASE.md)
- [Applications y AUR](APPLICATIONS_AUR.md)
- [Kernel y extensiones](KERNEL_EXTENSIONS.md)
- [Instalador, datos y hardware](INSTALLER_HARDWARE.md)
- [Puertas D00–D12](VALIDATION.md)
## Referencias primarias
[Arch Archive](https://wiki.archlinux.org/title/Arch_Linux_Archive), [partial upgrades](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported), [Arkdep](https://github.com/arkanelinux/arkdep), [RAUC](https://rauc.readthedocs.io/en/latest/using.html), [sysupdate](https://www.freedesktop.org/software/systemd/man/latest/systemd-sysupdate.html). Revisión documental 2026-11-24, no pruebas realizadas.
