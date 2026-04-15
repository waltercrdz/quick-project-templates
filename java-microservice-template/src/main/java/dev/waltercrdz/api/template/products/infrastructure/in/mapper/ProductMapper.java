package dev.waltercrdz.api.template.products.infrastructure.in.mapper;

import dev.waltercrdz.api.template.products.domain.model.Product;
import dev.waltercrdz.api.template.products.infrastructure.in.dto.ProductDto;

public class ProductMapper {

    public static ProductDto toDto(Product product) {
        return new ProductDto(
            product.getId(),
            product.getName(),
            product.getDescription(),
            product.getPrice(),
            product.getStock());
    }

    public static Product toDomain(ProductDto productDto) {
        return Product.of(
            productDto.id(),
            productDto.name(),
            productDto.description(),
            productDto.price(),
            productDto.stock());
    }
}
