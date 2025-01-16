package dev.waltercrdz.api.template.shared.domain.event;

public interface EventPublisher {

    void publish(DomainEvent event);
}
