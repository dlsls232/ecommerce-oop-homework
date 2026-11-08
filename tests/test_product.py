"""Тесты класса Product."""

from src.product import Product


def test_product_initialization():
    product = Product("Телефон", "Смартфон", 49999.90, 5)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 49999.90
    assert product.quantity == 5
