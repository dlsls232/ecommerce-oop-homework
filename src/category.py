"""Модуль с классом Category."""

from src.product import Product


class Category:
    """Категория товаров интернет-магазина."""

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(
            product.quantity for product in self.__products
        )
        return (
            f"{self.name}, количество продуктов: "
            f"{total_quantity} шт."
        )

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список товаров в виде строки."""
        return "".join(
            f"{product}\n" for product in self.__products
        )
