package dev.waltercrdz.api.template.products.application;

import static java.util.Objects.nonNull;
import static com.google.common.base.Preconditions.checkArgument;

import java.util.List;
import java.util.UUID;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;


import dev.waltercrdz.api.template.products.domain.model.Product;
import dev.waltercrdz.api.template.products.domain.repository.ProductQueryRepository;
import dev.waltercrdz.api.template.shared.domain.exception.ProductNotFoundException;

@Service
public class ProductFinder {

    private static final Logger LOGGER = LoggerFactory.getLogger(ProductFinder.class);

    private final ProductQueryRepository reader;

    public ProductFinder(ProductQueryRepository reader) {
        this.reader = reader;
    }

    public Product find(UUID id) {
        LOGGER.info("Finding product by id: {}", id);
        checkArgument(nonNull(id));
        return reader.findById(id).orElseThrow(() -> new ProductNotFoundException("Product not found", id));
    }

    public List<Product> findAll() {
        LOGGER.info("Finding all products");
        return reader.findAll();
    }
}
