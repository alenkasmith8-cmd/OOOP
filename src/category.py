from typing import List, Optional

from .product import Product


class Category:
    """Класс для представления категории продуктов."""

    category_count: int = 0  # Общее количество категорий
    product_count: int = 0  # Общее количество наименований товаров во всех категориях
    total_products: int = 0  # Для совместимости со скриптами проверки

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        """
        Инициализация объекта Category.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список продуктов в категории.
        """
        self.name = name
        self.description = description
        # Приватный атрибут по критериям задания
        self.__products: List[Product] = list(products) if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)
        Category.total_products = Category.product_count

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления продукта в категорию.

        :param product: Объект класса Product или его наследников.
        :raises TypeError: Если передан объект другого типа.
        """
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников."
            )

        self.__products.append(product)
        Category.product_count += 1
        Category.total_products = Category.product_count

    @property
    def _products(self) -> List[Product]:
        """Внутренний доступ к списку продуктов для итератора и совместимости тестов."""
        return self.__products

    @property
    def products(self) -> str:
        """Геттер для получения строкового описания продуктов."""
        return "\n".join(str(p) for p in self.__products)

    def __str__(self) -> str:
        """
        Строковое представление категории.
        Отображает суммарный остаток всех штук товаров в категории.
        """
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
