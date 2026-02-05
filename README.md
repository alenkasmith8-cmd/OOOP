Этот проект содержит два основных класса: Product и Category.
Классы предназначены для управления товарами и категориями товаров в приложении.

## Структура классов


## Класс Product

Атрибуты:
name (str): Название продукта.
description (str): Описание продукта.
price (float): Цена продукта (может содержать десятичную часть).
quantity (int): Количество продукта в наличи.

## Класс Category

Атрибуты:
name (str): Название категории.
description (str): Описание категории.
products (list): Список объектов класса Product, относящихся к данной категории.
total_categories (int): Общее количество категорий (атрибут класса).
total_products (int): Общее количество товаров в категории (атрибут класса).


+ Как использовать

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product: Product):
        self.products.append(product)
        Category.total_products += 1


# Пример использования
if __name__ == "__main__":
    electronics = Category("Electronics", "Gadgets and devices")
    phone = Product("Smartphone", "Latest model smartphone", 699.99, 10)
    
    electronics.add_product(phone)
    print(f"Category: {electronics.name}, Total products: {len(electronics.products)}")

## Тестирование

Для тестирования классов используется библиотека pytest. Тесты проверяют корректность инициализации объектов и подсчет категорий и товаров.


import pytest

def test_product_initialization():
    product = Product("Laptop", "High-performance laptop", 1500.00, 5)
    assert product.name == "Laptop"
    assert product.description == "High-performance laptop"
    assert product.price == 1500.00
    assert product.quantity == 5

def test_category_initialization():
    category = Category("Home Appliances", "Kitchen and other appliances")
    assert category.name == "Home Appliances"
    assert category.description == "Kitchen and other appliances"
    assert len(category.products) == 0
    assert Category.total_categories == 1

def test_add_product():
    category = Category("Toys", "Fun and games")
    product = Product("Doll", "A beautiful doll", 20.00, 15)
    category.add_product(product)
    
    assert len(category.products) == 1
    assert category.products[0].name == "Doll"
    assert Category.total_products == 1

def test_multiple_categories():
    cat1 = Category("Books", "Literature")
    cat2 = Category("Music", "Various music genres")
    
    assert Category.total_categories == 2

# Запуск тестов
if __name__ == "__main__":
    pytest.main()

## Установка

Убедитесь, что у вас установлен Python (версия 3.6 или выше).
Установите pytest, если он ещё не установлен:
pip install pytest

Запустите тесты:
pytest имя_файла_с_тестами.py


Заключение

Этот проект демонстрирует использование ООП в Python для создания и управления объектами
продуктов и категорий. Тесты обеспечивают надежность и уверенность в правильности работы классов.