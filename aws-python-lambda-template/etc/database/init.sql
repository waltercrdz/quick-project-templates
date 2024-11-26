CREATE TABLE IF NOT EXISTS MailValidation.extrapolations (
    id bigint AUTO_INCREMENT PRIMARY KEY,
    external_id bigint null,
    pattern_priority int null,
    pattern_id varchar(50) null,
    pattern varchar(50) null,
    email varchar(60) null,
    validation_status ENUM('VALID', 'INVALID', 'UNKNOWN', 'PENDING', 'CATCH_ALL') null,
    validation_method ENUM('GOOGLE', 'MICROSOFT', 'CORE') null,
    extrapolation_type ENUM('DEAD_END', 'ORGANIC', 'MANUAL') null,
    status ENUM('SENT', 'ON_HOLD', 'FAILED', 'REJECTED', 'EXCLUDED', 'VALIDATED', 'ALREADY_ACTIVE') null,
    linkedin_company_id bigint null,
    created_at datetime null,
    updated_at datetime null,
    UNIQUE KEY UNIQUE_CANDIDATE_EMAIL_EXTRAPOLATIONS_EMAIL_STRATEGY (external_id, email)
);

CREATE INDEX IX_EXTRAPOLATIONS_EXTERNAL_ID
    ON MailValidation.extrapolations (external_id);

ALTER TABLE MailValidation.backlog_validation
ADD COLUMN validation_method VARCHAR(50) NULL;

CREATE TABLE IF NOT EXISTS MailValidation.dead_ends (
    id bigint AUTO_INCREMENT PRIMARY KEY,
    external_id bigint NULL,
    linkedin_company_id bigint NULL,
    company_id bigint NULL,
    business_value decimal(3, 2) NULL,
    extrapolation_status ENUM('TO_PROCESS', 'PROCESSED') DEFAULT 'TO_PROCESS',
    rd_status ENUM('TO_PROCESS', 'PROCESSED', 'DOMAIN_NOT_FOUND') DEFAULT 'TO_PROCESS',
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY UNIQUE_DEAD_ENDS_EXTERNAL_ID (external_id)
);