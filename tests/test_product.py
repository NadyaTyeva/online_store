import pytest
from src.product import Product


def test_product(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_second_product(second_product):
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_product_category_property(first_product):
    assert first_product.price == 180000.0


def test_product_price_setter(first_product):
    new_price = 200000
    assert new_price == 200000


def test_product_price_setter_zero(first_product):
    new_price = 0
    assert "Цена не должна быть нулевая или отрицательная"


def test_product_price_setter_negative(first_product):
    new_price = -10
    assert "Цена не должна быть нулевая или отрицательная"


def test_classmethod_new_product():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy C23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_product_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
