PRODUCT_INSERT: str = """
            INSERT INTO products.products
            (
                id,
                name,
                description,
                price,
                stock
            ) VALUES (
                %(id)s,
                %(name)s,
                %(description)s,
                %(price)s,
                %(stock)s
            )
        """