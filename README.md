
# E-commerce: категории и товары

Учебный проект по ООП. В нём описаны две сущности интернет-магазина:

- `Product` — товар с названием, описанием, ценой и количеством в наличии.
- `Category` — категория с названием, описанием и списком объектов `Product`.

Класс `Category` автоматически считает количество созданных категорий
(`category_count`) и общее количество товаров в списках категорий
(`product_count`). Считаются именно позиции товаров, а не количество
единиц на складе.

Дополнительно реализована загрузка категорий и товаров из JSON-файла
`data/products.json` с помощью функции `load_categories()`.

## Установка

```bash
poetry install
```

## Запуск

```bash
poetry run python main.py
```

## Тесты и покрытие

```bash
poetry run pytest
poetry run pytest --cov=src --cov-report=term-missing --cov-report=html
```

HTML-отчёт появится в папке `htmlcov/`.

## Проверка стиля

```bash
poetry run flake8 src tests main.py
```
