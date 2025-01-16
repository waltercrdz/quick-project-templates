package dev.waltercrdz.api.template.products.infrastructure.in.dto;

import java.math.BigDecimal;
import java.util.UUID;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public record ProductDto(
    @NotNull UUID id,
    @NotBlank String name,
    @NotBlank String description,
    @NotNull @Min(0) BigDecimal price,
    @NotNull @Min(0) Integer stock) {}
