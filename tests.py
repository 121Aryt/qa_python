import pytest
from main import BooksCollector


class TestBooksCollector:

    # === add_new_book ===

    @pytest.mark.parametrize('name', [
        'Гордость и предубеждение и зомби',
        'Что делать, если ваш кот хочет вас убить'
    ])
    def test_add_new_book_add_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        collector.add_new_book('Очень длинное имя книги, которое превышает сорок символов и не должно добавиться')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

    # === set_book_genre ===

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_book_not_in_collection(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Неизвестный жанр')
        assert collector.get_book_genre('Книга') == ''

    # === get_book_genre ===

    def test_get_book_genre_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_get_book_genre_not_exists(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    # === get_books_with_specific_genre ===

    def test_get_books_with_specific_genre_found(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        collector.set_book_genre('Книга 3', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1', 'Книга 3']

    def test_get_books_with_specific_genre_not_found(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_books_with_specific_genre('Неизвестный жанр') == []

    # === get_books_genre ===

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        expected = {'Книга 1': '', 'Книга 2': ''}
        assert collector.get_books_genre() == expected

    # === get_books_for_children ===

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        collector.set_book_genre('Книга 3', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Книга 1', 'Книга 3']

    # === add_book_in_favorites ===

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_collection(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    # === delete_book_from_favorites ===

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_list(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    # === get_list_of_favorites_books ===

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']