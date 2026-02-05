from src.models import Category, Product


def test_product_initialization():
    product = Product("Apple", "A fresh apple", 0.99, 100)
    assert product.name == "Apple"
    assert product.description == "A fresh apple"
    assert product.price == 0.99
    assert product.quantity == 100


def test_category_initialization():
    product1 = Product("Apple", "A fresh apple", 0.99, 100)
    product2 = Product("Banana", "A ripe banana", 1.25, 80)
    category = Category("Fruits", "All kinds of fruits", [product1, product2])

    assert category.name == "Fruits"
    assert category.description == "All kinds of fruits"
    assert len(category.products) == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2


def test_multiple_categories():
    Category("Fruits", "All kinds of fruits")
    Category("Vegetables", "All kinds of vegetables")

    assert Category.total_categories == 3  # 2 предыдущих + 1 добавленный
