package dev.waltercrdz.api.template.products.domain.event;

import dev.waltercrdz.api.template.products.domain.model.Product;
import dev.waltercrdz.api.template.shared.domain.event.DomainEvent;
import dev.waltercrdz.api.template.shared.domain.event.EventType;

public class ProductCreatedDomainEvent extends DomainEvent {

    public final String orderId;

    private ProductCreatedDomainEvent(String orderId) {
        super(EventType.PRODUCT_CREATED);
        this.orderId = orderId;
    }

    public static ProductCreatedDomainEvent from(Product product) {
        return new ProductCreatedDomainEvent(product.getId().toString());
    }
}
