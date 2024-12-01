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




if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(category.products)