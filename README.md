# sga-software-engineering-squad
Sistema de Gestión Académica desarrollado con Scrum, Django 5.x y GitHub Projects por Software Engineering Squad.
## Descripción
Se agregó la vista inicial de login para el módulo accounts.

## Cambios realizados
- Creación de login_view
- Configuración inicial para Sprint 1

## Tipo de cambio
- [x] Nueva funcionalidad
=======
# Sistema de Gestión Académica (SGA)

## Sprint 0 Goal

El equipo Software Engineering Squad tiene el entorno Django configurado, el repositorio Git Flow activo, el Product Backlog organizado en GitHub Projects y la estructura base del SGA lista para iniciar el Sprint 1.

## Equipo — Software Engineering Squad

| Rol | Integrante | GitHub |
|---------------|------------|-------------|
| Product Owner | Nombre | @usuario |
| Scrum Master | Nombre | @usuario |
| Backend Dev | Nombre  | @usuario |
| Frontend Dev | HinostrozaDaniel | @usuario |
| QA / DevOps | Nombre | @usuario |

## Stack Tecnológico

- Python 3.12+
- Django 5.1
- Django REST Framework
- SQLite para desarrollo
- GitHub Projects
- Scrum + Git Flow

## Apps del Sistema

- accounts
- academico
- matricula
- calificaciones
- reportes
- api

## Cómo ejecutar el proyecto localmente

```bash
git clone https://github.com/AldairSY/sga-software-engineering-squad.git
cd sga-software-engineering-squad
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver