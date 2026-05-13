# Cloud9

Система управления компьютерным клубом.

## Описание проекта

Cloud9 — это веб-приложение для управления компьютерным клубом.
Система позволяет сотрудникам клуба управлять клиентами, контролировать время сессий и работать с базой данных через удобный интерфейс.

## Основной функционал

- Авторизация сотрудников
- Dashboard
- Управление клиентами
- Контроль времени клиентов
- CRUD операции
- Session Authentication
- Работа с PostgreSQL

## Используемые технологии

    ### Backend
    - Django
    - PostgreSQL

    ### Frontend
    - Django Templates
    - HTML/CSS
    - TailwindCSS

    ### Tools
    - GitHub
    - Figma

## Архитектура проекта

Проект построен по MTV (Model-Template-View) архитектуре.

### Основные модули:
- Authentication
- Clients
- Database
- Dashboard

## Диаграммы

    ### ER Diagram
    Описание структуры базы данных проекта.

    ### UML Sequence Diagram
    Диаграмма процесса авторизации пользователя.

## UI / UX

Были разработаны:
- Login Wireframe
- Dashboard UI
- Clients Page Mockup


## Структура проекта

```bash
Cloud9/
│
├── backend/
├── docs/
│   │
│   ├──design/
│   ├──ERD/
│   ├──testing/
│   └──UML/
├── gitingore
└── Cloud9_Project_Tasks_Final.xlsx


backend/
│
├── core/
├── clients/
│   │ 
│   ├──python
│   └──templates/
├── registration_and_authorization/
│   │ 
│   ├──python
│   └──templates/
│   
├── static/
│   │ 
│   └──pic/
├── theme/
│   │ 
│   ├──static/
│   └──templates/
│
└── manage.py