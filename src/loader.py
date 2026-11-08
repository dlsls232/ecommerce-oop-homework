"""Загрузка категорий и товаров из JSON-файла."""

import json
from pathlib import Path
from typing import Any

from src.category import Category
from src.product import Product


def load_categories(file_path: str | Path) -> list[Category]:
    """Прочитать JSON и создать объекты Category и Product."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        data: list[dict[str, Any]] = json.load(file)

    categories = []
    for category_data in data:
        products = [
            Product(
                name=product_data["name"],
                description=product_data["description"],
                price=float(product_data["price"]),
                quantity=int(product_data["quantity"]),
            )
            for product_data in category_data["products"]
        ]

        categories.append(
            Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
        )

    return categories
