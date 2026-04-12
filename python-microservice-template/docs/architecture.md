# Architecture — python-microservice-template

## Overview

A containerized FastAPI microservice for product management with CRUD operations backed by MySQL. It follows **Hexagonal Architecture** (Ports & Adapters) to keep business logic fully decoupled from HTTP and database concerns.

## Deployment

| Component | Technology |
|---|---|
| Runtime | Python 3.14 |
| HTTP framework | FastAPI + Uvicorn (ASGI) |
| Database | MySQL 9 |
| Containerization | Docker Compose |
| Migrations | Alembic |
| API schema | Auto-generated OpenAPI (Swagger UI at `/docs`) |

## Hexagonal Architecture

```
┌────────────────────────────────────────────────────────┐
│                    Microservice                        │
│                                                        │
│  ┌──────────────────┐     ┌────────────────────────┐  │
│  │  Inbound Adapter │     │   Outbound Adapter     │  │
│  │                  │     │                        │  │
│  │  infrastructure/ │     │  infrastructure/       │  │
│  │  routers/        │     │  persistence/          │  │
│  └────────┬─────────┘     └───────────┬────────────┘  │
│           │                           │               │
│           ▼                           ▼               │
│  ┌────────────────────────────────────────────────┐   │
│  │               Application Core                │   │
│  │                                                │   │
│  │  application/        domain/      shared/      │   │
│  │  AddProduct          Product      mappers      │   │
│  │  FindProductById     exceptions               │   │
│  └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
         │                              │
    HTTP Client                   MySQL Database
```

## Layer Breakdown

### `app/infrastructure/routers/` — Inbound Adapter
Translates HTTP requests into calls to the application layer and maps results back to HTTP responses. FastAPI route definitions live here.

- `products.py` — Route handlers for `POST /products` and `GET /products/{uuid}`.
- `dto.py` — Pydantic request/response models (Data Transfer Objects).
- `exception_handlers.py` — Maps domain exceptions to HTTP error responses (e.g. `ProductNotFound` → 404).

### `app/application/` — Use Cases
Orchestrates domain objects to fulfil a business operation. Has no knowledge of HTTP or SQL.

- `add_product.py` — `AddProduct` use case; validates input, creates domain entity, persists via repository.
- `find_product_by_id.py` — `FindProductById` use case; fetches a product or raises a domain exception.

### `app/domain/` — Domain Model
Pure business logic. No I/O, no framework dependencies.

- `product.py` — `Product` dataclass (uuid, name, price, …).
- `exceptions.py` — Domain-specific exceptions (e.g. `ProductNotFoundError`).

### `app/infrastructure/persistence/` — Outbound Adapter
Implements the repository port. Translates domain objects to SQL and executes queries against MySQL.

- `product_repository.py` — `ProductRepository`; manages connections and delegates to the query module.
- `queries.py` — Raw SQL statements as constants.

### `app/configuration/` — Configuration
Reads environment variables and exposes a typed `Config` object to the rest of the app.

- `config.py` — `Config` dataclass populated from `os.environ`.

### `app/shared/` — Shared Utilities
Cross-cutting helpers that do not belong to any single layer.

- `mappers.py` — Converts between persistence rows and domain objects.

### `app/main.py` — Application Entry Point
Creates the FastAPI application, registers routers, and attaches exception handlers.

### `tests/`
Unit tests. Each test targets a single layer in isolation using mocks for outbound ports.

```
tests/
├── application/   # use-case tests (mocked repository)
├── shared/        # mapper tests
└── utils/         # ObjectMother factories for test data
```

## Data Flow

### Create Product (`POST /products`)

```
HTTP POST /products  {name, price}
    │
    ▼
products router  (infrastructure/routers/products.py)
    │  validates DTO, calls use case
    ▼
AddProduct  (application/add_product.py)
    │  creates Product domain entity
    ▼
ProductRepository  (infrastructure/persistence/product_repository.py)
    │  executes INSERT query
    ▼
MySQL
    │
    ▼
HTTP 201 Created  {uuid}
```

### Get Product (`GET /products/{uuid}`)

```
HTTP GET /products/{uuid}
    │
    ▼
products router  (infrastructure/routers/products.py)
    │  calls use case with uuid
    ▼
FindProductById  (application/find_product_by_id.py)
    │  queries repository; raises ProductNotFoundError if absent
    ▼
ProductRepository  (infrastructure/persistence/product_repository.py)
    │  executes SELECT query
    ▼
MySQL
    │
    ▼
HTTP 200 OK  {uuid, name, price, …}   or   HTTP 404 Not Found
```

## Key Design Decisions

| Decision | Rationale |
|---|---|
| Hexagonal Architecture | Business logic is testable without a running database or HTTP server |
| FastAPI + Pydantic | Automatic OpenAPI docs and runtime request validation with zero boilerplate |
| No ORM | Raw SQL via `mysql-connector-python` gives full control over queries and avoids N+1 issues |
| Domain exceptions mapped at the router boundary | Keeps application layer free of HTTP concerns; single place to change error codes |
| Alembic for migrations (dev) | Schema versioning without coupling the app to ORM models |
| Docker Compose with healthcheck | Ensures MySQL is fully ready before the API starts, preventing connection errors on startup |

## Environment Variables

Configure in `etc/.env` (referenced by `docker-compose.yaml`):

| Variable | Required | Description |
|---|---|---|
| `DB_HOST` | Yes | MySQL hostname |
| `DB_NAME` | Yes | Database name |
| `DB_USER` | Yes | Database username |
| `DB_PASSWORD` | Yes | Database password |
