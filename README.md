# Notes API

REST API for notes control with FastAPI + SQLAlchemy + PostgreSQL + Alembic + Docker + Docker Compose

## About 

- CRUD operations with notes
- Data validation using Pydantic
- Tests with 100% coverage

## Tech-Stack

- **FastAPI** — web-framework
- **SQLAlchemy** — ORM
- **PostgreSQL** — database
- **Pytest** — testing
- **Alembic** - migrations
- **Docker** - containers
- **Docker Compose** - containers orchestration

## Install and Run

1. **Clone repo**
   ```bash
   git clone https://github.com/danilpashin/NotesAPI
   cd NotesAPI
   ```

2. **Create virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate # Linux/Mac
    venv\Scripts\activate # Windows
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```bash
    alembic upgrade head
    ```

5. **Set .env (example in .env.example)**
    ```bash
    cp .env.example .env
    ```

6. **Run server**
    ```bash
    uvicorn app.main:app --reload
    ```

7. **Open in browser**
- Notes: http://127.0.0.1:8000/notes/
- Health: http://127.0.0.1:8000/health/


## Using with Docker Desktop

1. **Clone repo**
   ```bash
   git clone https://github.com/danilpashin/NotesAPI
   cd NotesAPI
   ```
2. **Run containers**
    ```bash
    docker compose up
    ```