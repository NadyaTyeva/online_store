import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def data_for_categories():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )


@pytest.fixture
def second_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def for_category():
    return Category("Телевизоры", "Современный телевизор", ["телевизор 1", "телевизор 2"])


@pytest.fixture
def for_category_tablets():
    return Category(name="Планшеты", description="Современные планшеты",
                    products=["планшет 1", "планшет 2", "планшет 3"])


@pytest.fixture
def new_product():
    return Product.new_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    })


@pytest.fixture
def data_for_err():
    """Для проверки возбуждения ошибки при добавлении нового токара в список """
    return "Новый продукт"


@pytest.fixture
def data_for_counters_categories():
    """Данные для теста класса Category"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для " "удобства жизни",
        [
            Product.new_product(
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
            ),
            Product.new_product(
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
            ),
        ],
    )
