import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, books_collector):
        # создаем экземпляр (объект) класса BooksCollector
        # collector = BooksCollector()

        # добавляем две книги
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(books_collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1. Параметризованный тест для метода add_new_book
    # Проверка, что книга добавляется в словарь books_genre и что нельзя добавить книгу с именем длиннее 40 символов.
    @pytest.mark.parametrize('name, expected', [
        ('Книга 1', True),
        ('Книга с очень длинным названием, которое превышает 40 символов', False),
        ('', False),
    ])
    def test_add_new_book(self, books_collector, name, expected):
        books_collector.add_new_book(name)
        assert (name in books_collector.books_genre) == expected

    # 2. Тест для метода set_book_genre
    # Проверка, что жанр книги устанавливается корректно, если книга существуют.
    def test_set_book_genre(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.set_book_genre('Книга 1', 'Фантастика')
        assert books_collector.get_book_genre('Книга 1') == 'Фантастика'

    # Проверка, что жанр не устанавливается для несуществующей книги.
    def test_set_book_genre_for_non_existing_book(self, books_collector):
        books_collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in books_collector.books_genre

    # Проверка, что жанр не устанавливается, если он недопустим.
    def test_set_book_genre_for_invalid_genre(self, books_collector):
        books_collector.add_new_book('Книга 2')
        books_collector.set_book_genre('Книга 2', 'Недопустимый жанр')
        assert books_collector.get_book_genre('Книга 2') == ''

    # 3. Тест для метода get_book_genre
    # Проверка, что возвращает правильный жанр для существующей книги с установленным жанром.
    def test_get_book_genre_for_existing_book_with_genre(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.set_book_genre('Книга 1', 'Фантастика')
        assert books_collector.get_book_genre('Книга 1') == 'Фантастика'

    # Проверка, что метод возвращает None для несуществующей книги.
    def test_get_book_genre_for_non_existing_book(self, books_collector):
        assert books_collector.get_book_genre('Несуществующая книга') is None

    # Проверка, что метод возвращает пустую строку для существующей книги с недопустимым жанром.
    def test_get_book_genre_for_existing_book_without_genre(self, books_collector):
        books_collector.add_new_book('Книга 2')
        assert books_collector.get_book_genre('Книга 2') == ''

    # Проверка, что метод возвращает пустую строку для существующей книги с недопустимым жанром.
    def test_get_book_genre_for_existing_book_with_invalid_genre(self, books_collector):
        books_collector.add_new_book('Книга 3')
        books_collector.set_book_genre('Книга 3', 'Недопустимый жанр')
        assert books_collector.get_book_genre('Книга 3') == ''

    # Проверка, что метод возвращает пустую строку для существующей книги с пустым жанром.
    def test_get_book_genre_for_existing_book_with_empty_genre(self, books_collector):
        books_collector.add_new_book('Книга 4')
        books_collector.set_book_genre('Книга 4', '')
        assert books_collector.get_book_genre('Книга 4') == ''

    # 4. Тест для метода get_books_with_specific_genre
    # Проверка, что метод возвращает список книг с определенным жанром.
    @pytest.mark.parametrize('genre, expected_books',[
        ('Фантастика', ['Книга 1']),
        ('Ужасы', ['Книга 2']),
        ('Детективы', ['Книга 3']),
        ('Мультфильмы', ['Книга 4']),
        ('Комедии', ['Книга 5']),
    ])
    def test_get_books_with_specific_genre(self, books_collector, genre, expected_books):
        books_collector.add_new_book('Книга 1')
        books_collector.add_new_book('Книга 2')
        books_collector.add_new_book('Книга 3')
        books_collector.add_new_book('Книга 4')
        books_collector.add_new_book('Книга 5')

        books_collector.set_book_genre('Книга 1', 'Фантастика')
        books_collector.set_book_genre('Книга 2', 'Ужасы')
        books_collector.set_book_genre('Книга 3', 'Детективы')
        books_collector.set_book_genre('Книга 4', 'Мультфильмы')
        books_collector.set_book_genre('Книга 5', 'Комедии')

        assert books_collector.get_books_with_specific_genre(genre) == expected_books

    # 5. Тест для метода get_books_genre
    # Проверка, что метод возвращает весь словарь books_genre.
    def test_get_books_genre(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.add_new_book('Книга 2')
        assert books_collector.get_books_genre() == {'Книга 1': '', 'Книга 2': ''}

    # 6. Тест для метода get_books_for_children
    # Проверка, что метод возвращает книги с допустимыми для детей жанрами.
    @pytest.mark.parametrize('genre',[
        'Фантастика',
        'Мультфильмы',
        'Комедии',
    ])
    def test_get_books_for_children_should_include_book(self, books_collector, genre):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', genre)
        assert 'Книга' in books_collector.get_books_for_children()

    # Проверка, что метод не возвращает книги с недопустимыми для детей жанрами.
    @pytest.mark.parametrize('genre',[
        'Ужасы',
        'Детективы',
     ])
    def test_get_books_for_children_should_not_include_book(self, books_collector, genre):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', genre)
        assert 'Книга' not in books_collector.get_books_for_children()

    # 7. Тест для метода add_book_in_favorites
    # Проверка, что книга добавляется в избранное.
    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in books_collector.get_list_of_favorites_books()

    # Проверка, что книга не добавляется повторно, если она уже в избранном.
    def test_add_book_in_favorites_twice(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.add_book_in_favorites('Книга 1')
        books_collector.add_book_in_favorites('Книга 1') # Попытка добавить книгу повторно
        assert len(books_collector.get_list_of_favorites_books()) == 1

    # 8. Тест для метода delete_book_from_favorites
    # Проверка, что книга удаляется из избранного.
    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.add_book_in_favorites('Книга 1')
        books_collector.delete_book_from_favorites('Книга 1')
        assert 'Книга 1' not in books_collector.get_list_of_favorites_books()

    # Проверка, что повторное удаление книги не изменяет список избранного.
    def test_delete_book_from_favorites_twice(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.add_book_in_favorites('Книга 1')
        books_collector.delete_book_from_favorites('Книга 1')
        books_collector.delete_book_from_favorites('Книга 1') # Повторное удаление книги
        assert len(books_collector.get_list_of_favorites_books()) == 0

    # Проверка, что удаление несуществующей книги не изменяет список избранного.
    def test_delete_non_existing_book_from_favorites(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.add_book_in_favorites('Книга 1')
        books_collector.delete_book_from_favorites('Несуществующая книга') # Удаление несуществующей книги
        assert len(books_collector.get_list_of_favorites_books()) == 1

    # 9. Тест для метода get_list_of_favorites_books
    # Проверка, что метод возвращает список избранных книг.
    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book('Книга 1')
        books_collector.add_new_book('Книга 2')
        books_collector.add_book_in_favorites('Книга 1')
        books_collector.add_book_in_favorites('Книга 2')
        assert books_collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']
