class Product:
    """Класс для представления продукта."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        if price < 0:
            raise ValueError("Цена товара не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным.")

        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price  # Используем сеттер для единой валидации цены

    @property
    def price(self) -> float:
        """Геттер для атрибута 'цена'."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для атрибута 'цена'."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """
        Класс-метод для создания нового продукта из словаря параметров.
        Корректно работает для классов-наследников при наличии нужных ключей.
        """
        return cls(**product_data)

    def __str__(self) -> str:
        """Строковое представление объекта Product."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Магический метод сложения стоимости запасов двух товаров одного типа."""
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного и того же класса.")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
