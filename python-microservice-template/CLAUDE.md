# python-microservice-template

FastAPI REST microservice for product management with MySQL persistence. Runs fully containerized with Docker Compose.

## Stack

- **Runtime**: Python 3.14
- **Framework**: FastAPI + Uvicorn
- **Database**: MySQL 9
- **Containerization**: Docker Compose
- **Dependencies**: uv

## Common Commands

```bash
uv sync --dev              # install all dependencies
uv run pytest              # run tests
uv run coverage run -m pytest && uv run coverage report  # run tests with coverage
uv run ruff check app/     # lint
uv run mypy                # type check
```

## Run Locally

```bash
docker compose up          # start API + MySQL
```

API available at `http://localhost:8000`. Swagger UI at `http://localhost:8000/docs`.

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/products` | Create a product |
| `GET` | `/products/{uuid}` | Get a product by ID |

## Environment Variables

Configure in `etc/.env`:

| Variable | Description |
|---|---|
| `DB_HOST` | MySQL host |
| `DB_NAME` | Database name |
| `DB_USER` | Database user |
| `DB_PASSWORD` | Database password |

See `docs/architecture.md` for full architecture details.
