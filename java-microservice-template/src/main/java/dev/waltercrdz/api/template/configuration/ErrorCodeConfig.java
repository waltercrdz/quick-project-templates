package dev.waltercrdz.api.template.configuration;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.Map;

import dev.waltercrdz.api.template.shared.infrastructure.in.HttpStatusResolver;

@Configuration
@ConfigurationProperties(prefix = "error.codes")
public class ErrorCodeConfig {
    
    private Map<String, Integer> mappings;

    @Bean
    public HttpStatusResolver errorMappings() {
        return new HttpStatusResolver(this.mappings);
    }
}
