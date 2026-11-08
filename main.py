"""Точка входа в проект."""

from pathlib import Path

from src.category import Category
from src.loader import load_categories


def main() -> None:
    """Загрузить и вывести категории и товары."""
    data_path = Path(__file__).parent / "data" / "products.json"
    categories = load_categories(data_path)

    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(category.products, end="")

    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
