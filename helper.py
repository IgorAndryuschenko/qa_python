from test_data import test_books_data

def add_one_book_and_set_valid_genre(collector):
    collector.add_new_book(test_books_data[0][0])
    collector.set_book_genre(test_books_data[0][0], test_books_data[0][1])
    return collector


def add_one_book_and_add_in_favorites (collector):
    collector.add_new_book(test_books_data[0][0])
    collector.add_book_in_favorites (test_books_data[0][0])
    return collector

def collector_with_books(collector):
    for name, genre in test_books_data:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector