PRODUCT_INSERT: str = """
            INSERT INTO products
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