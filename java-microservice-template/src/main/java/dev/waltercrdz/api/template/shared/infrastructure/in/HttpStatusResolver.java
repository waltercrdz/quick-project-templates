package dev.waltercrdz.api.template.shared.infrastructure.in;

import java.util.HashMap;
import java.util.Map;

import org.springframework.http.HttpStatus;

import dev.waltercrdz.api.template.shared.domain.exception.DomainException;

public class HttpStatusResolver extends HashMap<String, Integer> {

    private final Map<String, Integer> mappings;

    public HttpStatusResolver(Map<String, Integer> mappings) {
        this.mappings = mappings;
    }

    public HttpStatus resolve(DomainException exception) {
        final var statusCode = mappings.getOrDefault(exception.getErrorCode().getCode(), HttpStatus.INTERNAL_SERVER_ERROR.value());
        return HttpStatus.resolve(statusCode);
    }

    public HttpStatus resolve(Exception exception) {
        final var statusCode = mappings.getOrDefault(exception.getClass().getSimpleName(), HttpStatus.INTERNAL_SERVER_ERROR.value());
        return HttpStatus.resolve(statusCode);
    }
}
