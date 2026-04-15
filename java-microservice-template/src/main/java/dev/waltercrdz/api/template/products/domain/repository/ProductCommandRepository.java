package dev.waltercrdz.api.template.products.domain.repository;

import dev.waltercrdz.api.template.products.domain.model.Product;

public interface ProductCommandRepository {

    void save(Product product);
}