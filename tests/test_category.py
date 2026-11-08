"""Тесты класса Category."""

from src.category import Category
from src.product import Product


def test_category_initialization():
    product = Product("Телефон", "Смартфон", 49999.90, 5)
    category = Category("Электроника", "Техника", [product])

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert category.products == [product]
    assert category.products[0] is product


def test_category_count():
    first = Category("Электроника", "Техника", [])
    second = Category("Книги", "Литература", [])

    assert first.category_count == 2
    assert second.category_count == 2
    assert Category.category_count == 2


def test_product_count_is_number_of_products_not_stock_quantity():
    first_product = Product("Телефон", "Смартфон", 100.0, 20)
    second_product = Product("Ноутбук", "Компьютер", 200.0, 7)
    Category("Электроника", "Техника", [first_product, second_product])

    third_product = Product("Книга", "Роман", 30.0, 100)
    category = Category("Книги", "Литература", [third_product])

    assert category.product_count == 3
    assert Category.product_count == 3
