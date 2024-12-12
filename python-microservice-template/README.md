# Python Microservice Template

This is a template for building Python microservices using FastAPI. It includes features such as product creation, and product information retrieval. The project is structured to follow Hexagonal Architecture, best practices and is ready for deployment.

## Features

- Product creation
- Product info

## Project Structure

* `pyproject.toml`: Standard configuration file for Python projects, used by various tools including Poetry, Ruff, isort, and more.
* `app/main.py`: Entry point of the project that starts the application.
* `app/infrastructure/routers/products.py`: Contains the API endpoints for product-related operations.
* `app/domain/product.py`: Defines the Product domain model.
* `app/application/add_product.py`: Contains the business logic for adding products.
* `app/application/find_product_by_id.py`: Contains the business logic for finding products by ID.
* `app/shared/mappers.py`: Contains utility functions for mapping data.
* `tests/`: Directory containing test cases for the project.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/waltercrdz/python-microservice-template.git
    cd python-microservice-template
    ```

2. Install the dependencies using Poetry:
    ```bash
    poetry install --no-root
    ```

3. Create a `.env` file in the `etc` directory with the following content:
    ```env
    DB_HOST=db
    DB_USER=products
    DB_PASSWORD=password123
    DB_NAME=products
    ```

4. Run the FastAPI server:
    ```bash
    poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

## Running with Docker

1. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

2. The FastAPI server will be available at `http://localhost:8000`.

## Testing

1. Run the tests using pytest:
    ```bash
    poetry run pytest
    ```

## Usage

### Product Endpoints

- **Create Product**: `POST /products/`
    - Request Body:
        ```json
        {
            "name": "Product Name",
            "description": "Product Description",
            "price": 12.20,
            "stock": 100
        }
        ```
    - Response:
        ```json
        {
            "id": "UUID",
            "name": "Product Name",
            "description": "Product Description",
            "price": 12.20,
            "stock": 100
        }
        ```

- **Get Product by ID**: `GET /products/{product_id}`
    - Response:
        ```json
        {
            "id": "UUID",
            "name": "Product Name",
            "description": "Product Description",
            "price": 12.20,
            "stock": 100
        }
        ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

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