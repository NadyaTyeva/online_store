class Product:
    """Информация о продуктах"""

    name: str  # название
    description: str # описание
    price: float # цена
    quantity: int # количество в наличии

    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        self.__price = price
        try:
            self.quantity = quantity
            raise TypeError
        except TypeError as e:
            print(e)
            print("Товар с нулевым количеством не может быть добавлен")

        super().__init__()