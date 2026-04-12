# Architecture — aws-python-lambda-template

## Overview

An AWS Lambda function that consumes messages from an SQS queue and persists product records to a MySQL database. It follows **Hexagonal Architecture** (Ports & Adapters) to keep business logic decoupled from AWS and database concerns.

## Deployment

| Component | Technology |
|---|---|
| Function runtime | Python 3.14 on AWS Lambda |
| Trigger | AWS SQS |
| Database | MySQL (Amazon RDS or compatible) |
| Deployment tool | Serverless Framework v4 |
| Dependency packaging | `serverless-python-requirements` with uv |
| Infrastructure | VPC with security group + subnets |

## Hexagonal Architecture

```
┌─────────────────────────────────────────────────┐
│                   AWS Lambda                    │
│                                                 │
│  ┌─────────────┐     ┌──────────────────────┐  │
│  │   Inbound   │     │    Outbound Adapter  │  │
│  │   Adapter   │     │                      │  │
│  │             │     │  persistence/        │  │
│  │  handler/   │     │  ProductRepository   │  │
│  └──────┬──────┘     └──────────┬───────────┘  │
│         │                       │               │
│         ▼                       ▼               │
│  ┌──────────────────────────────────────────┐   │
│  │            Application Core             │   │
│  │                                          │   │
│  │  application/   domain/   shared/        │   │
│  │  AddProduct     Product   mappers        │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
         │                        │
    SQS Event               MySQL Database
```

## Layer Breakdown

### `src/handler/` — Inbound Adapter
Entry point for the Lambda function. Receives the raw SQS event from AWS, extracts and validates the message body, and delegates to the application layer.

- `sqs_consumer_handler.py` — `lambda_handler(event, context)` function; iterates SQS records and calls the use case.

### `src/application/` — Use Cases
Orchestrates domain objects to fulfil a business operation. Has no knowledge of SQS, HTTP, or databases.

- `add_product.py` — `AddProduct` use case; receives a product DTO, creates the domain entity, and calls the repository port.

### `src/domain/` — Domain Model
Pure business logic. No I/O, no framework dependencies.

- `product.py` — `Product` dataclass (id, name, price, …).
- `error.py` — Domain-specific error types.

### `src/persistence/` — Outbound Adapter
Implements the repository port defined by the application layer. Translates domain objects to SQL and executes queries against MySQL.

- `product_repository.py` — `ProductRepository`; opens a connection and calls the query module.
- `queries.py` — Raw SQL statements as constants.

### `src/configuration/` — Configuration
Reads environment variables and exposes a typed `Config` object consumed by the handler and persistence layers.

- `config.py` — `Config` dataclass populated from `os.environ`.

### `src/shared/` — Shared Utilities
Cross-cutting helpers that do not belong to any single layer.

- `mappers.py` — Converts between SQS message payloads and domain objects.
- `decorator.py` — Reusable decorators (e.g. error handling, logging).

### `tests/`
Unit tests. Each test targets a single layer in isolation using mocks for outbound ports.

```
tests/
├── application/   # use-case tests (mocked repository)
├── shared/        # mapper tests
└── utils/         # ObjectMother factories for test data
```

## Data Flow

```
SQS Event
    │
    ▼
lambda_handler (handler/sqs_consumer_handler.py)
    │  extracts & maps message body
    ▼
AddProduct (application/add_product.py)
    │  creates Product domain entity
    ▼
ProductRepository (persistence/product_repository.py)
    │  executes INSERT query
    ▼
MySQL
```

## Key Design Decisions

| Decision | Rationale |
|---|---|
| Hexagonal Architecture | Isolates business logic from AWS and database; enables unit testing without real infrastructure |
| No ORM | Raw SQL via `mysql-connector-python` keeps the Lambda package size small and startup latency low |
| Strict mypy | Catches type errors at development time; prevents runtime failures in Lambda where debugging is harder |
| `serverless-python-requirements` with uv | Packages only production dependencies, strips debug symbols (`slim: true`) to reduce Lambda cold-start time |

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `DB_HOST` | Yes | MySQL hostname |
| `DB_NAME` | Yes | Database name |
| `DB_USER` | Yes | Database username |
| `DB_PASSWORD` | Yes | Database password |
| `SQS_REGION` | Yes | AWS region where SQS queue lives |
| `SEC_GROUP_ID` | Yes | VPC security group ID for Lambda |
| `SUBNET_ID1` | Yes | VPC subnet ID (AZ 1) |
| `SUBNET_ID2` | Yes | VPC subnet ID (AZ 2) |
| `ENV` | No | Execution environment (`development` / `staging` / `production`) |
| `REGION` | No | AWS region (injected automatically by Serverless) |
| `ACCOUNT_ID` | No | AWS account ID (injected automatically by Serverless) |
