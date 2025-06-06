import pytest
from helper import *
from main import BooksCollector
from test_data import test_books_data


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_same_name(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['S', 'Гордость и предубеждение и философский к'])
    def test_add_new_book_add_book_1_and_40_len(self, collector, name):
        collector.add_new_book(name)
        list_name= collector.get_books_genre()
        assert 1 == len(list_name)

    @pytest.mark.parametrize('name', ['', 'Гордость и предубеждение и философский ка'])
    def test_add_new_book_not_add_0_and_41_len(self, collector, name):
        collector.add_new_book(name)
        list_name = collector.get_books_genre()
        assert 0 == len(list_name)

    def test_set_book_genre_valid_data(self, collector):
        add_one_book_and_set_valid_genre(collector)
        assert collector.books_genre['Гарри Поттер'] == 'Фантастика'

    def test_set_book_genre_not_name(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Драко Малфой', 'Фантастика')
        genre_draco = collector.get_book_genre('Драко Малфой')
        assert None == genre_draco

    def test_set_book_genre_not_valid_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фанфик')
        genre_gp = collector.get_book_genre('Гарри Поттер')
        assert '' == genre_gp

    def test_get_book_genre_valid_data(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.books_genre['Гарри Поттер'] = 'Фантастика'
        genre_gp = collector.get_book_genre('Гарри Поттер')
        assert genre_gp == 'Фантастика'

    def test_get_books_with_specific_genre(self,collector):
        collector_with_books(collector)
        list_fantasy = collector.get_books_with_specific_genre("Фантастика")
        assert 'Гарри Поттер' in list_fantasy and 'Песнь льда и пламени' in list_fantasy

    def test_get_books_genre(self, collector):
        add_one_book_and_set_valid_genre(collector)
        list_books_genre = collector.get_books_genre()
        assert {'Гарри Поттер':'Фантастика'} == list_books_genre

    def test_get_books_for_children(self, collector):
        collector_with_books(collector)
        list_for_kids = collector.get_books_for_children()
        assert 'Гарри Поттер' in list_for_kids and 'Песнь льда и пламени' in list_for_kids and 'Лунтик' in list_for_kids

    def test_add_book_in_favorites_add_one(self,collector):
        add_one_book_and_add_in_favorites(collector)
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self, collector):
        add_one_book_and_add_in_favorites(collector)
        collector.add_book_in_favorites('Лунтик')
        collector.delete_book_from_favorites('Лунтик')
        list_book_in_favorites = collector.get_list_of_favorites_books()
        assert list_book_in_favorites == ['Гарри Поттер']

    def test_get_list_of_favorites_books(self, collector):
        add_one_book_and_add_in_favorites(collector)
        list_book_in_favorites = collector.get_list_of_favorites_books()
        assert 'Гарри Поттер' in list_book_in_favorites

