
"""Тесты загрузки данных из JSON."""

import json

from src.category import Category
from src.loader import load_categories


def test_load_categories(tmp_path):
    data = [
        {
            "name": "Электроника",
            "description": "Техника",
            "products": [
                {
                    "name": "Телефон",
                    "description": "Смартфон",
                    "price": 49999.9,
                    "quantity": 5,
                }
            ],
        }
    ]
    file_path = tmp_path / "products.json"
    file_path.write_text(
        json.dumps(data, ensure_ascii=False),
        encoding="utf-8",
    )

    categories = load_categories(file_path)

    assert len(categories) == 1
    assert categories[0].name == "Электроника"
    assert categories[0].products[0].name == "Телефон"
    assert isinstance(categories[0].products[0].price, float)
    assert Category.category_count == 1
    assert Category.product_count == 1
