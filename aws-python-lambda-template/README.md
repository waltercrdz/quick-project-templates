# Serverless Framework AWS Python Template

This template demonstrates how to deploy a Python function running on AWS Lambda using the traditional Serverless Framework. It includes an SQS consumer that processes messages and persists data into a PostgreSQL database. For more advanced configurations check out the [examples repo](https://github.com/serverless/examples/) which includes integrations with SQS, DynamoDB or examples of functions that are triggered in `cron`-like manner. For details about configuration of specific `events`, please refer to our [documentation](https://www.serverless.com/framework/docs/providers/aws/events/).

## Features

- SQS Consumer: Processes messages from an AWS SQS queue.
- PostgreSQL Persistence: Stores user data in a PostgreSQL database.

## Project Structure
* pyproject.toml: Standard configuration file for Python projects, used by various tools including Poetry, Ruff, isort, and more.
* app/main.py: Entry point of the project that starts the application.
* tests/: Directory containing test cases for the project.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/waltercrdz/users-api.git
    cd users-api
    ```

2. Install the dependencies using Poetry:
    ```bash
    poetry install --no-root
    ```

3. Run the FastAPI server:
    ```bash
    poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

## Running with Docker Compose

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/users-api.git
    cd users-api
    ```

2. Run the application using Docker Compose:
    ```bash
    docker-compose up --build
    ```

## API Endpoints

### User Registration

- **Endpoint:** `/users`
- **Method:** `POST`
- **Description:** Register a new user.
- **Request Body:**
    - `email` (string): The email of the user.
    - `password` (string): The password of the user.
- **Responses:**
    - `201 Created`: Successfully registered the user.
        - Body: A JSON object representing the user.
    - `400 Bad Request`: Invalid input data.
    - `500 Internal Server Error`: An error occurred on the server.
- **Curl Command:**
    ```bash
    curl -X POST "http://127.0.0.1:8000/register" -H "Content-Type: application/json" -d '{"email": "walterio@gmail.com", "password": "newpassword123"}'
    ```

### Get a User by Id

- **Endpoint:** `/users/{id}`
- **Method:** `GET`
- **Description:** Retrieves a user by their unique identifier.
- **Path Parameters:**
    - `id` (string): The unique identifier of the user.
- **Responses:**
    - `200 OK`: Successfully retrieved the user.
        - Body: A JSON object representing the user.
    - `404 Not Found`: No user found with the specified id.
    - `500 Internal Server Error`: An error occurred on the server.
- **Curl Command:**
    ```bash
    curl -X GET "http://127.0.0.1:8000/users/{id}" -H "accept: application/json"
    ```

### User Authentication

- **Endpoint:** `/auth`
- **Method:** `POST`
- **Description:** Authenticate a user and returns a JWT token.
- **Request Body:**
    - `email` (string): The email of the user.
    - `password` (string): The password of the user.
- **Responses:**
    - `200 OK`: Successfully authenticated the user.
        - Body: A JSON object containing the JWT token.
    - `401 Unauthorized`: Invalid credentials.
    - `500 Internal Server Error`: An error occurred on the server.
- **Curl Command:**
    ```bash
    curl -X POST "http://127.0.0.1:8000/auth" -H "Content-Type: application/json" -d '{"email": "walterio@gmail.com", "password": "newpassword123"}'
    ```

For more details, please refer to the OpenAPI documentation, hosted at `http://127.0.0.1:8000/docs`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.


###############################################

# Serverless Framework AWS Python Template

This template demonstrates how to deploy a Python function running on AWS Lambda using the traditional Serverless Framework. The deployed function does not include any event definitions as well as any kind of persistence (database). For more advanced configurations check out the [examples repo](https://github.com/serverless/examples/) which includes integrations with SQS, DynamoDB or examples of functions that are triggered in `cron`-like manner. For details about configuration of specific `events`, please refer to our [documentation](https://www.serverless.com/framework/docs/providers/aws/events/).

## Usage

### Deployment

In order to deploy the example, you need to run the following command:

```
$ serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying aws-python-project to stage dev (us-east-1)

✔ Service deployed to stack aws-python-project-dev (112s)

functions:
  hello: aws-python-project-dev-hello (1.5 kB)
```

### Invocation

After successful deployment, you can invoke the deployed function by using the following command:

```bash
serverless invoke --function hello
```

Which should result in response similar to the following:

```json
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v3.0! Your function executed successfully!\", \"input\": {}}"
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function hello
```

Which should result in response similar to the following:

```
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v3.0! Your function executed successfully!\", \"input\": {}}"
}
```

### Bundling dependencies

In case you would like to include third-party dependencies, you will need to use a plugin called `serverless-python-requirements`. You can set it up by running the following command:

```bash
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to `plugins` section in your `serverless.yml` file and add it as a `devDependency` to `package.json` file. The `package.json` file will be automatically created if it doesn't exist beforehand. Now you will be able to add your dependencies to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but requires additional configuration) and they will be automatically injected to Lambda package during build process. For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).
