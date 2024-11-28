# Serverless Framework AWS Python Template

This template demonstrates how to deploy a Python function running on AWS Lambda using the traditional Serverless Framework. It includes an SQS consumer that processes messages and persists data into a PostgreSQL database. For more advanced configurations check out the [examples repo](https://github.com/serverless/examples/) which includes integrations with SQS, DynamoDB or examples of functions that are triggered in `cron`-like manner. For details about configuration of specific `events`, please refer to our [documentation](https://www.serverless.com/framework/docs/providers/aws/events/).

## Features

- SQS Consumer: Processes messages from an AWS SQS queue.
- PostgreSQL Persistence: Stores data in a PostgreSQL database.

## Project Structure
* pyproject.toml: Standard configuration file for Python projects, used by various tools including Poetry.
* ruff.toml: Configuration file for Ruff, which is used to enforce coding standards and style guidelines.
* src/handler/sqs_consumer_handler.py: Entry point of the project that starts the application.
* tests/: Directory containing test cases for the project.

## Installation

### Deployment

In order to deploy the example, you need to run the following command:

```bash
serverless deploy
```

Configure your AWS credentials with the following command:
```bash
aws configure
```

### Invocation

After successful deployment, you can invoke the deployed function by using the following command:

```bash
serverless invoke --function sqs-consumer -p etc/test/test-body.json
```

Which should result in response similar to the following:

```json
{
    "statusCode": 200,
    "body": "Products processed successfully"
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local -f sqs-consumer -p etc/test/test-body.json
```

Which should result in response similar to the following:

```json
{
    "statusCode": 200,
    "body": "Products processed successfully"
}
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.