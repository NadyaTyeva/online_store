import pytest
from tests.conftest import new_product


def test_category_init(for_category):
    assert for_category.name == "Телевизоры"
    assert for_category.description == "Современный телевизор"
    #assert for_category.products == ["телевизор 1", "телевизор 2"]
    assert for_category.category_count == 1
    assert for_category.product_count == 2


def test_add_product(for_category, new_product, data_for_err):
    assert for_category.product_count == 4
    for_category.add_product(new_product)
    assert for_category.product_count == 5
    with pytest.raises(TypeError):
        for_category.add_product(data_for_err)
