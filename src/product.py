from abc import ABC, abstractmethod


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def __init__(self):
        pass


class Product(BaseProduct, PrintMixin):
    """Информация о продуктах"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):


        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()


    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_params: dict):
        """Метод добавляющий новый продукт в список"""
        return cls(**product_params)

    @property
    def price(self):
        """Метод волзвращающий цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Метод меняющий цену продукта в зависимости от условия"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color





