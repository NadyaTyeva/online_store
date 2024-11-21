class Category:
    """Информация о котегориях"""

    category_count = 0
    product_count = 0

    name: str  # название
    description: str # описание
    products: list # список товаров категории

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)
