CREATE SCHEMA products;

CREATE TABLE IF NOT EXISTS products.products (
    id          UUID PRIMARY KEY,
    name        TEXT           NOT NULL,
    description TEXT           NOT NULL,
    price       NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    stock       INTEGER        NOT NULL CHECK (stock >= 0)
);