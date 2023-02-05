BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Метод конструктор объекта 'Book'.

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books: list = None):
        """
        Метод конструктор объекта 'Library'.

        :param books: Список книг
        """
        self.books = [] if books is None else books

    def get_next_book_id(self) -> int:
        """Метод возвращает идентификатор для добавления новой книги в библиотеку."""
        if self.books is None:
            return 1
        else:
            count_books = len(self.books)
            return count_books + 1

    def get_index_by_book_id(self, number_id) -> int:
        """
        Метод возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса.

        :param number_id: Запрашиваемый идентификатор книги (id)
        :return: Возвращает индекс книги
        """
        for index, book in enumerate(self.books):
            if number_id == book.id_:  # Сравнение с атрибутом экземпляра класса
                return index
        # Конструкция else специально размещается под for
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
