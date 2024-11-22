import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def second_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def for_category():
    return Category(name="Телевизоры", description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником", products=["телевизор 1", "телевизор 2"])