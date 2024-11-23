class Category:
    """Информация о котегориях"""

    category_count = 0  # Счетчик категорий
    product_count = 0  # Счетчик товаров

    name: str  # название
    description: str  # описание
    products: list  # список товаров категории

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(products)  # Увеличиваем счетчик товаров на количество добавленных товаров
