import pytest
from src.product import Product, LawnGrass, Smartphone


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


def test_smartphone(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_2(smartphone2):
    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_add_grass():
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    grass_sum = grass1 + grass2
    assert grass_sum == 16750.0


def test_add_grass_error(grass1):
    with pytest.raises(TypeError):
        grass1 + 1


def test_lawngrass(grass2):
    assert grass2.name == "Газонная трава"
    assert grass2.description == "Элитная трава для газона"
    assert grass2.price == 500.0
    assert grass2.quantity == 20
    assert grass2.country == "Россия"
    assert grass2.germination_period == "7 дней"
    assert grass2.color == "Зеленый"








