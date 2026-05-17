# FastAPI-SaaS-Backend
FastAPI Backend framework for CRM, task manager, SaaS platform, project management system


## Production-ready backend template built with:

- FastAPI
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- JWT Authentication
- Redis
- Docker

## Features

- User registration/login
- JWT authentication
- PostgreSQL database
- SQLAlchemy async ORM
- Alembic migrations
- Redis integration
- Project management
- Task management
- Repository pattern
- Service layer architecture
- Docker support


## Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL 16
- Redis 7
- SQLAlchemy 2.0
- Alembic
- Pydantic v2
- Docker Compose

---

# Project Structure

```text
backend/
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── fsbsrc/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── projects.py
│   │       └── tasks.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── logging.py
│   │   ├── redis.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── project_repository.py
│   │   └── task_repository.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── project_service.py
│   │   └── task_service.py
│   │
│   ├── tasks/
│   │   └── email_tasks.py
│   │
│   ├── utils/
│   │   └── pagination.py
│   │
│   └── main.py
│
├── .env
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
````

---

# Installation

## Clone repository

```bash
git clone https://github.com/IlyaBisec/FastAPI-SaaS-Backend.git

cd FastAPI-SaaS-Backend/backend
```

---

# Environment Variables

Create `.env`

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/fsb_db

SECRET_KEY=supersecretkey

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

REDIS_URL=redis://redis:6379
```

---

# Run with Docker

```bash
docker compose up --build
```

Application:

```text
http://localhost:8000
```

Swagger docs:

```text
http://localhost:8000/docs
```

---

# Run locally

## Create virtual environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

# Run database

```bash
docker compose up db redis -d
```

---

# Run migrations

Create migration:

```bash
alembic revision --autogenerate -m "initial"
```

Apply migration:

```bash
alembic upgrade head
```

---

# Start server

```bash
uvicorn fsbsrc.main:app --reload
```

---

# Authentication

## Register

POST `/auth/register`

```json
{
  "email": "test@test.com",
  "username": "test",
  "password": "12345678"
}
```

## Login

POST `/auth/login`

```json
{
  "email": "test@test.com",
  "password": "12345678"
}
```

Response:

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

# API Endpoints

## Auth

* POST `/auth/register`
* POST `/auth/login`

## Users

* GET `/users/me`

## Projects

* GET `/projects`
* POST `/projects`

## Tasks

* GET `/tasks`
* POST `/tasks`

---

# Database Migrations

Generate migration:

```bash
alembic revision --autogenerate -m "message"
```

Apply:

```bash
alembic upgrade head
```

Rollback:

```bash
alembic downgrade -1
```

---

# Docker Commands

Stop containers:

```bash
docker compose down
```

Remove volumes:

```bash
docker compose down -v
```

Rebuild containers:

```bash
docker compose up --build
```

---

# Development

Recommended IDE:

* PyCharm 2025.2.6.1
* VSCode

Recommended tools:

* Ruff
* Black
* MyPy

---

# Future Improvements

* Celery background jobs
* Email sending
* WebSockets
* File uploads
* Role permissions
* OAuth2
* Unit tests
* CI/CD pipeline
* Kubernetes deployment

---

# IlyaBisec
ilya.borisov.bisec@gmail.com

(c) 2026

