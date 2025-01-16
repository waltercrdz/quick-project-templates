package dev.waltercrdz.api.template.products.infrastructure.in.error;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import dev.waltercrdz.api.template.shared.domain.exception.DomainException;

import dev.waltercrdz.api.template.shared.infrastructure.in.error.ApiError;
import dev.waltercrdz.api.template.shared.infrastructure.in.HttpStatusResolver;

@ControllerAdvice
public class ErrorHandler {

    private static final Logger LOGGER = LoggerFactory.getLogger(ErrorHandler.class);

    private HttpStatusResolver statusResolver;

    public ErrorHandler(HttpStatusResolver errorMappings) {
        this.statusResolver = errorMappings;
    }

    @ExceptionHandler(DomainException.class)
    public ResponseEntity<ApiError> handleDomainException(DomainException e) {
        return buildApiError(e);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiError> handleUnexpectedException(Exception e) {
        return buildApiError(e);
    }

    public ResponseEntity<ApiError> buildApiError(Exception e) {
        LOGGER.error("Unexpected exception occurred: {}", e.getMessage(), e);
        ApiError apiError = ApiError.from(e);
        HttpStatus status = statusResolver.resolve(e);
        return ResponseEntity.status(status).body(apiError);
    }
}
