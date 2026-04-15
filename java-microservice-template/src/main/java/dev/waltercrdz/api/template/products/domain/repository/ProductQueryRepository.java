package dev.waltercrdz.api.template.products.domain.repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

import dev.waltercrdz.api.template.products.domain.model.Product;

public interface ProductQueryRepository {

    Optional<Product> findById(UUID id);
    List<Product> findAll();
}
