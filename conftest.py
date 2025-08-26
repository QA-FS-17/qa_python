import pytest
from main import BooksCollector

# Фикстура для создания экземпляра BooksCollector
@pytest.fixture
def books_collector():
    return BooksCollector()
