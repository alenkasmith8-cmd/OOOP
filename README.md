Этот проект содержит два основных класса: Product и Category.
Классы предназначены для управления товарами и категориями товаров в приложении.

## Структура классов


## Класс Product

### 1. Базовый класс `Product`
Представляет базовую сущность товара.

* **Атрибуты объекта**:
  * `name` (str): название товара.
  * `description` (str): описание товара.
  * `quantity` (int): остаток товара на складе (не может быть отрицательным).
  * `__price` (float): приватный атрибут стоимости товара.
* **Свойства и методы**:
  * `@property price`: возвращает текущую цену товара.
  * `@price.setter`: проверяет корректность новой цены (запрещает значения $\le 0$).
  * `@classmethod new_product(product_data)`: фабричный метод для создания экземпляра из словаря.
  * `__str__()`: возвращает строку формата `"Название, X руб. Остаток: X шт."`.
  * `__add__()`: возвращает суммарную стоимость складских остатков двух товаров (`price * quantity`). Складывать можно только объекты одного и того же класса.


### 2. Дочерние классы товаров

#### `Smartphone` (наследуется от `Product`)
* Дополнительные атрибуты:
  * `efficiency` (float): производительность процессора.
  * `model` (str): модель смартфона.
  * `memory` (int): объём встроенной памяти (ГБ).
  * `color` (str): цвет корпуса.

#### `LawnGrass` (наследуется от `Product`)
* Дополнительные атрибуты:
  * `country` (str): страна-производитель.
  * `germination_period` (str): срок всхожести семян.

## Класс Category

Представляет категорию, объединяющую товары.

* **Атрибуты класса (статические)**:
  * `category_count` (int): общее количество созданных категорий.
  * `product_count` (int): общее количество наименований товаров во всех категориях.
* **Атрибуты объекта**:
  * `name` (str): название категории.
  * `description` (str): описание категории.
  * `__products` (list): приватный список товаров категории.
* **Методы и свойства**:
  * `add_product(product)`: принимает объект класса `Product` (или его наследников) и добавляет в категорию. Защищает список от добавления посторонних объектов.
  * `@property products`: возвращает строковый список всех товаров категории построчно.
  * `__str__()`: выводит название категории и суммарный остаток всех физических единиц товара в ней.


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
```python
from src.category import Category
from src.product import LawnGrass, Product, Smartphone

# Создание категории
smartphones_cat = Category("Смартфоны", "Мобильные устройства")

# Создание товара через фабричный метод
phone_data = {
    "name": "iPhone 15",
    "description": "128GB, Black",
    "price": 85000.0,
    "quantity": 5,
    "efficiency": 3.46,
    "model": "A16 Bionic",
    "memory": 128,
    "color": "Черный"
}
iphone = Smartphone.new_product(phone_data)

# Добавление товара
smartphones_cat.add_product(iphone)

# Вывод информации
print(smartphones_cat)
# Смартфоны, количество продуктов: 5 шт.

print(smartphones_cat.products)
# iPhone 15, 85000.0 руб. Остаток: 5 шт.

```

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