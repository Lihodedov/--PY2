class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Метод конструктор объекта "Book".

        :param name: Название (неизменяемый атрибут)
        :param author: Автор (неизменяемый атрибут)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name

        if not isinstance(author, str):
            raise TypeError("Автор должен быть типа str")
        self.author = author

    @property
    def name(self) -> str:
        """ Возвращает название книги. """
        return self._name

    @property
    def author(self) -> str:
        """ Возвращает автора книги. """
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс описывает модель бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        """
        Метод конструктор объекта "PaperBook".
        
        :param pages: Количество страниц
        """
        self.pages = pages

    @property
    def pages(self) -> int:
        """ Возвращает количество страниц в книге. """
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        """ Устанавливает количество страниц в книге. """
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self) -> str:
        return f"Бумажная книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """ Класс описывает модель аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        """
        Метод конструктор объекта "AudioBook".

        :param duration: Продолжительность
        """
        self.duration = duration

    @property
    def duration(self) -> float:
        """ Возвращает продолжительность аудиокниги. """
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        """ Устанавливает новую продолжительность аудиокниги. """
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration

    def __str__(self) -> str:
        return f"Аудиокнига {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
