package dev.waltercrdz.api.template.products.infrastructure.out.persistence.mapper;

import dev.waltercrdz.api.template.products.domain.model.Product;
import dev.waltercrdz.api.template.products.infrastructure.out.persistence.entity.ProductEntity;

public class ProductMapper {

    public static ProductEntity toEntity(Product product) {
        return new ProductEntity(
            product.getId(),
            product.getName(),
            product.getDescription(),
            product.getPrice(),
            product.getStock()
        );
    }

    public static Product toDomain(ProductEntity productEntity) {
        return Product.of(
            productEntity.getId(),
            productEntity.getName(),
            productEntity.getDescription(),
            productEntity.getPrice(),
            productEntity.getStock()
        );
    }
}
