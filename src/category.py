from src.product import Product


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
        self.__products = products

        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(products)  # Увеличиваем счетчик товаров на количество добавленных товаров

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, цена {product.price} руб, Остаток: {product.quantity} шт \n"
        return product_str

    def add_product(self, products: Product):
        if isinstance(products, Product):
            self.__products.append(products.name)
            Category.product_count += 1
        else:
            raise TypeError
