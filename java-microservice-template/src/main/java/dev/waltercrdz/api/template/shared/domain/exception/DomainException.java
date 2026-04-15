package dev.waltercrdz.api.template.shared.domain.exception;

import java.util.Map;

public class DomainException extends RuntimeException {

    private final ErrorCode errorCode;
    private final Map<String, Object> metadata;

    public DomainException(String message, ErrorCode errorCode) {
        super(message);
        this.errorCode = errorCode;
        this.metadata = null;
    }
    
    public DomainException(String message, ErrorCode code, Map<String, Object> metadata) {
        super(message);
        this.errorCode = code;
        this.metadata = metadata;
    }
    
    public DomainException(String message, ErrorCode code, Throwable cause) {
        super(message, cause);
        this.errorCode = code;
        this.metadata = null;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }

    public Map<String, Object> getMetadata() {
        return metadata;
    }
}
