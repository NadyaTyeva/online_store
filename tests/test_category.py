import pytest


def test_category_init(for_category):
    assert for_category.name == "Телевизоры"
    assert for_category.description == "Современный телевизор"
    assert for_category.category_count == 1
    assert for_category.product_count == 2


def test_category_products_property(data_for_counters_categories):
    assert data_for_counters_categories.products == (
        "Iphone 15, цена 210000.0 руб, Остаток: 8 шт \n" "Xiaomi Redmi Note 11, цена 31000.0 руб, Остаток: 14 шт \n"
    )


def test_add_product(data_for_categories, new_product, data_for_err):
    assert len(data_for_categories.products_in_list) == 1
    data_for_categories.add_product(new_product)
    assert len(data_for_categories.products_in_list) == 2
    with pytest.raises(TypeError):
        data_for_categories.add_product(data_for_err)


def test_category_str(data_for_counters_categories):
    assert str(data_for_counters_categories) == "Смартфоны, количество продуктов: 22 шт."
