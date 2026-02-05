import json

from src.models import Category, Product


def load_data_from_json(file_path: str):
    """
    Загрузка данных из JSON файла.

    :param file_path: Путь к файлу с данными
    :return: Список объектов Category
    """
    with open(file_path, "r") as file:
        data = json.load(file)

    categories = []
    for category_info in data["categories"]:
        products = [Product(**product) for product in category_info["products"]]
        category = Category(
            category_info["name"], category_info["description"], products
        )
        categories.append(category)

    return categories
