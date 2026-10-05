import pytest
from main import BooksCollector


class TestBooksCollector:

    # 1. Тест для add_new_book: проверка длины имени книги
    @pytest.mark.parametrize('name, expected_length', [
        ('Гордость и предубеждение и зомби', 1),
        ('Очень длинное имя книги, которое превышает сорок символов и не должно добавиться', 0),
        ('', 0)
    ])
    def test_add_new_book_name_length(self, name, expected_length):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_length

    # 2. Тест для add_new_book: добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 3. Тест для set_book_genre: установка жанра
    @pytest.mark.parametrize('book_name, genre, add_book, expected_genre', [
        ('Книга 1', 'Фантастика', True, 'Фантастика'),
        ('Книга 2', 'Ужасы', True, 'Ужасы'),
        ('Несуществующая книга', 'Фантастика', False, None),
        ('Книга 3', 'Неизвестный жанр', True, '')
    ])
    def test_set_book_genre(self, book_name, genre, add_book, expected_genre):
        collector = BooksCollector()
        if add_book:
            collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    # 4. Тест для get_book_genre: получение жанра книги
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'
        assert collector.get_book_genre('Несуществующая книга') is None

    # 5. Тест для get_books_with_specific_genre: получение списка книг с определенным жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        collector.set_book_genre('Книга 3', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1', 'Книга 3']
        assert collector.get_books_with_specific_genre('Неизвестный жанр') == []

    # 6. Тест для get_books_genre: получение всего словаря книг
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        expected = {'Книга 1': '', 'Книга 2': ''}
        assert collector.get_books_genre() == expected

    # 7. Тест для get_books_for_children: получение книг, подходящих детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        collector.set_book_genre('Книга 3', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Книга 1', 'Книга 3']

    # 8. Тест для add_book_in_favorites: добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

        # Добавляем несуществующую книгу
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()

        # Повторно добавляем ту же книгу
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 9. Тест для delete_book_from_favorites: удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

        # Удаляем книгу, которой нет в избранном
        collector.delete_book_from_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    # 10. Тест для get_list_of_favorites_books: получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']