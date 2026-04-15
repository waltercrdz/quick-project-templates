package dev.waltercrdz.api.template.shared.infrastructure.in.error;

import dev.waltercrdz.api.template.shared.domain.exception.DomainException;
import dev.waltercrdz.api.template.shared.domain.exception.ErrorCode;

import java.util.Map;
import java.util.Objects;

import static com.google.common.base.Preconditions.*;

public record ApiError(String error, String message, Map<String, Object> metadata) {
    public ApiError {
        checkArgument(Objects.nonNull(error), "Code cannot be null");
        checkArgument(Objects.nonNull(message), "Message cannot be null");
    }

    public static ApiError from(DomainException e) {
        return new ApiError(e.getErrorCode().getCode(), e.getMessage(), e.getMetadata());
    }

    public static ApiError from(ErrorCode errorCode, Exception e) {
        return new ApiError(errorCode.getCode(), e.getMessage(), Map.of());
    }

    public static ApiError from(Exception e) {
        return new ApiError(ErrorCode.INTERNAL_SERVER_ERROR.getCode(), e.getMessage(), Map.of());
    }
}
