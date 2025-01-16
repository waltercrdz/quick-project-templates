package dev.waltercrdz.api.template.products.infrastructure.in.utils;

import java.math.BigDecimal;
import java.util.UUID;

import dev.waltercrdz.api.template.products.infrastructure.in.dto.ProductDto;

public class ProductMother {

    public static final String INVALID_PRODUCT_ID = "invalid_product_id";
    public static final UUID NON_EXISTENT_PRODUCT_ID = UUID.fromString("f7b3b3b4-3b1b-4b3b-8b3b-3b1b3b1b3b1e");
    public static final UUID PRODUCT_ID_1 = UUID.fromString("f7b3b3b4-3b1b-4b3b-8b3b-3b1b3b1b3b1b");

    // ('f7b3b3b4-3b1b-4b3b-8b3b-3b1b3b1b3b1b', 'Product 1', 'Description 1', 10.00, 10),
    // ('f7b3b3b4-3b1b-4b3b-8b3b-3b1b3b1b3b1c', 'Product 2', 'Description 2', 20.00, 0),
    // ('f7b3b3b4-3b1b-4b3b-8b3b-3b1b3b1b3b1d', 'Product 3', 'Description 3', 30.00, 5)

    public static ProductDto createValidProduct() {
        return new ProductDto(
            PRODUCT_ID_1,
            "Product 1",
            "Description 1",
            BigDecimal.valueOf(10.00),
            10
        );
    }

    public static ProductDto createMalformedProduct() {
        return new ProductDto(
            PRODUCT_ID_1,
            "", // Empty name to simulate malformed product
            "Description with missing name",
            BigDecimal.valueOf(10.00),
            10
        );
    }

    public static ProductDto createProductWithNegativeStock() {
        return new ProductDto(
            PRODUCT_ID_1,
            "Product Negative Stock",
            "Description Negative Stock",
            BigDecimal.valueOf(10.00),
            -5
        );
    }

    public static ProductDto createProductWithNegativePrice() {
        return new ProductDto(
            PRODUCT_ID_1,
            "Product Negative Price",
            "Description Negative Price",
            BigDecimal.valueOf(-10.00),
            10
        );
    }
}
