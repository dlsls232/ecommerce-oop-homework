"""Тесты класса Category."""

from src.category import Category
from src.product import Product


def test_category_initialization():
    product = Product("Телефон", "Смартфон", 49999.90, 5)
    category = Category("Электроника", "Техника", [product])

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert category._Category__products == [product]
    assert "Телефон, 49999.9 руб. Остаток: 5 шт.\n" == category.products


def test_add_product():
    category = Category("Электроника", "Техника", [])
    product = Product("Телефон", "Смартфон", 49999.90, 5)

    initial_count = Category.product_count
    result = category.add_product(product)

    assert result is None
    assert category._Category__products == [product]
    assert Category.product_count == initial_count + 1


def test_category_count():
    initial_count = Category.category_count

    Category("Электроника", "Техника", [])
    Category("Книги", "Литература", [])

    assert Category.category_count == initial_count + 2


def test_product_count_is_number_of_products_not_stock_quantity():
    first_product = Product("Телефон", "Смартфон", 100.0, 20)
    second_product = Product("Ноутбук", "Компьютер", 200.0, 7)

    initial_count = Category.product_count

    Category("Электроника", "Техника", [first_product, second_product])

    assert Category.product_count == initial_count + 2


def test_category_str():
    first_product = Product("Телефон", "Смартфон", 100.0, 20)
    second_product = Product("Ноутбук", "Компьютер", 200.0, 7)
    category = Category(
        "Электроника",
        "Техника",
        [first_product, second_product],
    )

    assert str(category) == (
        "Электроника, количество продуктов: 27 шт."
    )
