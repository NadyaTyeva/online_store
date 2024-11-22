def test_category_init(for_category):
    assert for_category.name == "Телевизоры"
    assert for_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert for_category.products == ["телевизор 1", "телевизор 2"]
    assert for_category.category_count == 1
    assert for_category.product_count == 2
