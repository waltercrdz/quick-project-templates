package dev.waltercrdz.api.template.shared.domain.event;

public enum EventType {
    PRODUCT_CREATED("product_created"),
    PRODUCT_UPDATED("product_updated");

    private final String value;

    EventType(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }
}
