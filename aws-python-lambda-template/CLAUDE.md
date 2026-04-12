# aws-python-lambda-template

AWS Lambda function triggered by SQS that processes product events and persists them to MySQL. Deployed with Serverless Framework v4.

## Stack

- **Runtime**: Python 3.14
- **Trigger**: AWS SQS
- **Database**: MySQL (via `mysql-connector-python`)
- **Deployment**: Serverless Framework v4 + `serverless-python-requirements`
- **Dependencies**: uv

## Common Commands

```bash
uv sync --dev              # install all dependencies
uv run pytest              # run tests
uv run coverage run -m pytest && uv run coverage report  # run tests with coverage
uv run ruff check src/     # lint
uv run mypy                # type check
```

## Deploy

```bash
npm install                          # install Serverless plugins
serverless deploy --stage dev        # deploy to AWS
serverless invoke local -f sqs-consumer --path etc/test/test-body.json  # local test
```

## Environment Variables

| Variable | Description |
|---|---|
| `DB_HOST` | MySQL host |
| `DB_NAME` | Database name |
| `DB_USER` | Database user |
| `DB_PASSWORD` | Database password |
| `SQS_REGION` | AWS region for SQS |
| `SEC_GROUP_ID` | VPC security group ID |
| `SUBNET_ID1` | VPC subnet ID 1 |
| `SUBNET_ID2` | VPC subnet ID 2 |

See `docs/architecture.md` for full architecture details.
