"""Точка входа в проект."""

from pathlib import Path

from src.loader import load_categories


def main() -> None:
    """Загрузить и вывести категории и товары."""
    data_path = Path(__file__).parent / "data" / "products.json"
    categories = load_categories(data_path)

    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        for product in category.products:
            print(
                f"- {product.name}: {product.price:.2f} руб. "
                f"(в наличии: {product.quantity})"
            )

    print(f"Всего категорий: {categories[0].category_count}")
    print(f"Всего товаров: {categories[0].product_count}")


if __name__ == "__main__":
    main()
