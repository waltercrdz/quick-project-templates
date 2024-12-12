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

PRODUCT_SELECT_BY_ID: str = """
    SELECT * 
    FROM products 
    WHERE id = %(id)s
"""