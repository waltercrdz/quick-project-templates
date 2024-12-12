# Python Microservice Template

This is a template for building Python microservices using FastAPI. It includes features such as product creation, and product information retrieval. The project is structured to follow Hexagonal Architecture, best practices and is ready for deployment.

## Features

- Product creation
- Product info

## Project Structure

* `pyproject.toml`: Standard configuration file for Python projects, used by various tools including Poetry, Ruff, isort, and more.
* `app/main.py`: Entry point of the project that starts the application.
* `app/infrastructure`: Contains the implementation details and adapters for external systems, such as database repositories and API routers.
* `app/domain`: Contains the core business logic and domain models. This layer is independent of external systems and frameworks.
* `app/application`: Contains the application services and use cases that orchestrate the business logic. This layer interacts with the domain layer and the infrastructure layer.
* `app/shared/mappers.py`: Contains utility functions for mapping data.
* `tests/`: Directory containing test cases for the project.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/waltercrdz/quick-project-templates.git
    cd python-microservice-template
    ```

2. Install the dependencies using Poetry:
    ```bash
    poetry install --no-root
    ```

3. Create a `.env` file in the `etc` directory with the following content:
    ```env
    DB_HOST=YOUR_DB_HOST
    DB_USER=YOUR_DB_USER
    DB_PASSWORD=YOUR_DB_PASSWORD
    DB_NAME=products
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

## API Endpoints

### Product Creation

- **Endpoint:** `/products`
- **Method:** `POST`
- **Description:** Creates a new Product.
- **Request Body:**
    - `name` (string): The name of the product.
    - `description` (string): The description of the product.
    - `price` (float): The price of the product.
    - `quantity` (int): The quantity of the product in stock.
- **Responses:**
    - `201 Created`: Successfully created the Product.
        - Body: A JSON object representing the Product.
    - `400 Bad Request`: Invalid input data.
    - `500 Internal Server Error`: An error occurred on the server.
- **Curl Command:**
    ```bash
    curl -X POST "http://127.0.0.1:8000/products" -H "Content-Type: application/json" -d '{"name": "Sample Product", "description": "This is a sample product", "price": 19.99, "quantity": 100}'
    ```

### Get a Product by Id

- **Endpoint:** `/products/{uuid}`
- **Method:** `GET`
- **Description:** Retrieves a Product by their unique identifier.
- **Path Parameters:**
    - `id` (UUID): The unique identifier of the Product.
- **Responses:**
    - `200 OK`: Successfully retrieved the Product.
        - Body: A JSON object representing the Product.
    - `404 Not Found`: No Product found with the specified id.
    - `500 Internal Server Error`: An error occurred on the server.
- **Curl Command:**
    ```bash
    curl -X GET "http://127.0.0.1:8000/products/{uuid}" -H "accept: application/json"
    ```

For more details, please refer to the OpenAPI documentation, hosted at `http://127.0.0.1:8000/docs`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.