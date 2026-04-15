package dev.waltercrdz.api.template.products.application;

import static com.google.common.base.Preconditions.checkArgument;
import static java.util.Objects.nonNull;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import dev.waltercrdz.api.template.products.domain.model.Product;
import dev.waltercrdz.api.template.products.domain.repository.ProductCommandRepository;

@Service
public class ProductCreator {

    private static final Logger LOGGER = LoggerFactory.getLogger(ProductCreator.class);

    private final ProductCommandRepository writer;

    public ProductCreator(ProductCommandRepository writer) {
        this.writer = writer;
    }
    
    public void create(Product product) {
        checkArgument(nonNull(product));
        LOGGER.info("Creating product: {}", product);
        writer.save(product);
    }
}
