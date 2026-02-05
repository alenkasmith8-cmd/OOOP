from typing import List, Optional


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация класса Product.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        """
        Инициализация класса Category.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []  # Явная проверка на None

        # Увеличиваем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(self.products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        self.products.append(product)
        Category.total_products += 1

    def remove_product(self, product: Product):
        """Удаляет продукт из категории."""
        if product in self.products:
            self.products.remove(product)
            Category.total_products -= 1
        else:
            print(f"Product {product.name} not found in the category {self.name}.")

    def __str__(self):
        return f"Category(name={self.name}, description={self.description}, products_count={len(self.products)})"
