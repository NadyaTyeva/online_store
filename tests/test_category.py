def test_category_init(for_category):
    assert for_category.name == "Телевизоры"
    assert for_category.description == "Современный телевизор"
    assert for_category.products == ["телевизор 1", "телевизор 2"]
    assert for_category.category_count == 1
    assert for_category.product_count == 2


def test_category_init(for_category_tablets):
    assert for_category_tablets.name == "Планшеты"
    assert for_category_tablets.description == "Современные планшеты"
    assert for_category_tablets.products == ["планшет 1", "планшет 2", "планшет 3"]
    assert for_category_tablets.category_count == 1
    assert for_category_tablets.product_count == 3
