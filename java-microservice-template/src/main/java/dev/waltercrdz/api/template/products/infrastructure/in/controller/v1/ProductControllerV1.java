package dev.waltercrdz.api.template.products.infrastructure.in.controller.v1;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import dev.waltercrdz.api.template.products.application.ProductCreator;
import dev.waltercrdz.api.template.products.application.ProductFinder;
import dev.waltercrdz.api.template.products.infrastructure.in.dto.ProductDto;
import dev.waltercrdz.api.template.products.infrastructure.in.mapper.ProductMapper;
import jakarta.validation.Valid;

@RestController
@RequestMapping("/v1/products")
public class ProductControllerV1 {

    private final ProductFinder finder;
    private final ProductCreator creator;

    public ProductControllerV1(ProductFinder finder, ProductCreator creator) {
        this.finder = finder;
        this.creator = creator;
    }

    @GetMapping("/{id}")
    @ResponseStatus(HttpStatus.OK)
    public ProductDto getProduct(@PathVariable UUID id) {
        final var product = finder.find(id);
        return ProductMapper.toDto(product);
    }

    @GetMapping
    @ResponseStatus(HttpStatus.OK)
    public List<ProductDto> getProducts() {
        final var products = finder.findAll();
        return products.stream()
                       .map(ProductMapper::toDto)
                       .collect(Collectors.toList());
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ProductDto createProduct(@Valid @RequestBody ProductDto request) {
        final var product = ProductMapper.toDomain(request);
        creator.create(product);
        return request;
    }
}
