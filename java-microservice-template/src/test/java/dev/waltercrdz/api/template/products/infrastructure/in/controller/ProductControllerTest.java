package dev.waltercrdz.api.template.products.infrastructure.in.controller;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.annotation.Import;
import org.springframework.test.web.servlet.MockMvc;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

import dev.waltercrdz.api.template.products.infrastructure.in.configuration.TestConfig;
import dev.waltercrdz.api.template.products.infrastructure.in.utils.ProductMother;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.springframework.http.MediaType;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
@AutoConfigureMockMvc
@Import(TestConfig.class)
public class ProductControllerTest {
    
    private static final String URI_PRODUCT = "/products";

    @Autowired
    private MockMvc mockMvc;

    private ObjectMapper objectMapper;

    @BeforeAll
    void setup() {
        objectMapper = new ObjectMapper()
                        .setPropertyNamingStrategy(PropertyNamingStrategies.SNAKE_CASE)
                        .registerModule(new JavaTimeModule());
    }

    @Test
    void shouldReturnAllProducts() throws Exception {
        mockMvc.perform(get(URI_PRODUCT)
            .contentType(MediaType.APPLICATION_JSON))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$").isArray())
            .andExpect(jsonPath("$.length()").value(3));
    }

    @Test
    void shouldReturnProduct_whenValidProductIdIsProvided() throws Exception {
        final var expectedProductResult = ProductMother.createValidProduct();
        mockMvc.perform(get(URI_PRODUCT + "/" + expectedProductResult.id().toString())
            .contentType(MediaType.APPLICATION_JSON))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.id").value(expectedProductResult.id().toString()))
            .andExpect(jsonPath("$.name").value(expectedProductResult.name()))
            .andExpect(jsonPath("$.description").value(expectedProductResult.description()))
            .andExpect(jsonPath("$.price").value(expectedProductResult.price().toString()))
            .andExpect(jsonPath("$.stock").value(expectedProductResult.stock()));
    }
    
    @Test
    void shouldReturnNotFoundError_whenNonExistentProductIdIsProvided() throws Exception {
        mockMvc.perform(get(URI_PRODUCT + "/" + ProductMother.NON_EXISTENT_PRODUCT_ID.toString())
            .contentType(MediaType.APPLICATION_JSON))
            .andExpect(status().isNotFound());
    }
    
    @Test
    void shouldReturnBadRequestError_whenInvalidProductIdIsProvided() throws Exception {
        mockMvc.perform(get(URI_PRODUCT + "/" + ProductMother.INVALID_PRODUCT_ID)
            .contentType(MediaType.APPLICATION_JSON))
            .andExpect(status().isBadRequest());
    }
    
    @Test
    void shouldCreateProductSuccessfully_whenValidRequestProvided() throws Exception {
        final var request = ProductMother.createValidProduct();

        mockMvc.perform(post(URI_PRODUCT)
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.id").value(request.id().toString()))
            .andExpect(jsonPath("$.name").value(request.name()))
            .andExpect(jsonPath("$.description").value(request.description()))
            .andExpect(jsonPath("$.price").value(request.price().toString()))
            .andExpect(jsonPath("$.stock").value(request.stock()));
    }
    
    @Test
    void shouldReturnBadRequest_whenProductIsMalformed() throws Exception {
        final var request = ProductMother.createMalformedProduct();

        mockMvc.perform(post(URI_PRODUCT)
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest());
    }

    @Test
    void shouldReturnBadRequest_whenProductStockIsNegative() throws Exception {
        final var request = ProductMother.createProductWithNegativeStock();

        mockMvc.perform(post(URI_PRODUCT)
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest());   
    }
    
    @Test
    void shouldReturnBadRequest_whenProductPriceIsNegative() throws Exception {
        final var request = ProductMother.createProductWithNegativePrice();

        mockMvc.perform(post(URI_PRODUCT)
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest());
    }
}
