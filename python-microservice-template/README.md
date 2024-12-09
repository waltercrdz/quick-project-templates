# Users API

API to handle user registration, authentication, and retrieval of user information.

## Features

- User registration
- User Authentication
- User info

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