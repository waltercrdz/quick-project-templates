# quick-project-templates

A collection of production-ready Python project templates following Hexagonal Architecture (Ports & Adapters).

## Templates

| Template | Description |
|---|---|
| `aws-python-lambda-template` | AWS Lambda SQS consumer with MySQL persistence, deployed via Serverless Framework |
| `python-microservice-template` | FastAPI REST microservice with MySQL, containerized with Docker Compose |

## Architecture

Both templates apply Hexagonal Architecture with three layers:
- **Domain** — business entities and rules, no external dependencies
- **Application** — use cases orchestrating domain logic
- **Infrastructure** — inbound adapters (HTTP routers / Lambda handlers) and outbound adapters (persistence)

## Package Manager

Both templates use [uv](https://docs.astral.sh/uv/). Common commands:

```bash
uv sync --dev         # install all dependencies (including dev)
uv run pytest         # run tests
uv run ruff check .   # lint
uv run mypy           # type check
```
