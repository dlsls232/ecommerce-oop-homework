"""Тесты класса Product."""

from src.product import Product


def test_product_initialization():
    product = Product("Телефон", "Смартфон", 49999.90, 5)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 49999.90
    assert product.quantity == 5


def test_new_product():
    product_data = {
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 100000.0,
        "quantity": 3,
    }

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 100000.0
    assert product.quantity == 3


def test_price_setter():
    product = Product("Телефон", "Смартфон", 50000.0, 5)

    product.price = 60000.0

    assert product.price == 60000.0


def test_price_setter_rejects_zero(capsys):
    product = Product("Телефон", "Смартфон", 50000.0, 5)

    product.price = 0

    assert product.price == 50000.0
    message = "Цена не должна быть нулевая или отрицательная"
    assert message in capsys.readouterr().out


def test_price_setter_rejects_negative(capsys):
    product = Product("Телефон", "Смартфон", 50000.0, 5)

    product.price = -100

    assert product.price == 50000.0
    message = "Цена не должна быть нулевая или отрицательная"
    assert message in capsys.readouterr().out


def test_product_str():
    product = Product("Телефон", "Смартфон", 80, 15)

    assert str(product) == "Телефон, 80 руб. Остаток: 15 шт."


def test_product_add():
    product_a = Product("Телефон", "Смартфон", 100, 10)
    product_b = Product("Ноутбук", "Компьютер", 200, 2)

    assert product_a + product_b == 1400
