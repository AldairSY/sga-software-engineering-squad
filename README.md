# sga-software-engineering-squad
Sistema de Gestión Académica desarrollado con Scrum, Django 5.x y GitHub Projects por Software Engineering Squad.
## Estado Actual

# Reporte de Actividades Técnicas - Sprint 1
**Estudiante:** Daniel
**Rol en el Equipo:** Frontend Developer / Core Integrator
**Proyecto:** Sistema de Gestión de Facturación e Inventario - Meycif
**Rama de Trabajo:** `develop`

---

## 1. Introducción y Contexto del Sprint
Durante el inicio del Sprint 1, el objetivo principal del equipo fue establecer la arquitectura base del software y garantizar la sincronización absoluta de los entornos de desarrollo locales con el repositorio centralizado en GitHub administrado por el compañero Aldair. 

Como desarrollador del equipo, mi enfoque inicial se centró en la preparación del entorno, la resolución de divergencias en el código base y la mitigación de conflictos de fusión (*Merge Conflicts*), asegurando la integridad de las ramas antes de iniciar con el despliegue de las interfaces gráficas en React.

---

## 2. Actividades Técnicas Realizadas

### A. Configuración y Autenticación del Entorno Git
* **Problema Inicial:** Restricciones de seguridad en el protocolo de comunicación de la línea de comandos (CMD) que impedían la transferencia de paquetes hacia el repositorio remoto.
* **Solución Implementada:** Se procedió con la actualización e integración de *Git Credential Manager* mediante la consola del sistema utilizando el comando:
  ```bash
  git config --global credential.helper manager
Sprint 0 completado exitosamente.

