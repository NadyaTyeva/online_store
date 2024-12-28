from src.product import Product


class Category:
    """Информация о категориях"""

    category_count = 0  # Счетчик категорий
    product_count = 0  # Счетчик товаров

    name: str  # название
    description: str  # описание
    products: list  # список товаров категории

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Метод отображающий строку в заданном формате"""
        total_quatity = 0
        for product in self.__products:
            total_quatity += product.quantity
        return f"{self.name}, количество продуктов: {total_quatity} шт."

    @property
    def products(self):
        """Отображение продукта в заданном формате"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, цена {product.price} руб, Остаток: {product.quantity} шт \n"
        return product_str

    def add_product(self, product: dict):
        """Метод добавления нового продукта в список"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([products.price for products in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
