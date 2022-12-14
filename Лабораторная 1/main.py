import doctest


class Video:
    def __init__(self, length: float, format_: str):
        """
        Метод конструктор объекта "Video"

        :param length: Продолжительность видео (мин)
        :param format_: Формат видео

        Примеры:
        >>> video_ = Video(35.48, "mp4")  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Продолжительность видео должна быть типа int или float")
        if length <= 0:
            raise ValueError("Продолжительность видео должна быть положительным числом")
        self.length = length

        if not isinstance(format_, str):
            raise TypeError("Формат видео должен быть типа str")
        self.format_ = format_

    def cut_(self, cut_lenght: float) -> None:
        """
        Метод, который обрезает видео

        :param cut_lenght: Фрагмент видео, который необходимо обрезать (мин)
        :raise ValueError: Ошибка, если фрагмент видео, который необходимо обрезать, больше или равен
        продолжительности видео

        :return: Продолжительность видео уменьшается на значение обрезаемого фрагмента

        Примеры:
        >>> video_ = Video(35.48, "mp4")
        >>> video_.cut_(12.37)
        """
        if not isinstance(cut_lenght, (int, float)):
            raise TypeError("Фрагмент видео, который необходимо обрезать, должен быть типа int или float")
        if cut_lenght <= 0:
            raise ValueError("Фрагмент видео, который необходимо обрезать, должен быть положительным числом")
        ...

    def formatting_(self, new_format: str) -> None:
        """
        Метод изменяет формат видео

         :param new_format: Новый формат видео

         :return: Возвращается новый формат видео

         Примеры:
         >>> video_ = Video(35.48, "mp4")
         >>> video_.formatting_("avi")
        """
        if not isinstance(new_format, str):
            raise TypeError("Новый формат видео должен быть типа str")
        ...

    def playback_speed(self, speed: float) -> None:
        """
        Метод изменяет скорость воспроизведения видео

        :param speed: Требуемая скорость воспроизведения видео

        :return: Изменяется скорость воспроизведения видео

        Примеры:
        >>> video_ = Video(35.48, "mp4")
        >>> video_.playback_speed(1.5)
        """
        if not isinstance(speed, float):
            raise TypeError("Скорость видео должна быть типа float")
        if not 0.25 <= speed <= 2:
            raise ValueError("Не соответствие диапазону изменения значений скорости воспроизведения видео")
        ...


class SmartPhone:
    def __init__(self, model: str, display_diagonal: float, internal_memory: int):
        """
        Метод конструктор объекта "SmartPhone"

        :param model: Модель телефона
        :param display_diagonal: Диагональ дисплея телефона (дюйм)
        :param internal_memory: Внутренняя память телефона (Гбайт)

        Примеры:
        >>> phone = SmartPhone("Xiaomi 13", 6.36, 128)  # инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Модель телефона должна быть типа str")
        self.model = model

        if not isinstance(display_diagonal, (int, float)):
            raise TypeError("Диагональ дисплея телефона должна быть типа int или float")
        if display_diagonal <= 0:
            raise ValueError("Диагональ дисплея телефона должна быть положительным числом")
        self.display_diagonal = display_diagonal

        if not isinstance(internal_memory, int):
            raise TypeError("Внутренняя память телефона должна быть типа int")
        if internal_memory <= 0:
            raise ValueError("Внутренняя память телефона должна быть положительным числом")
        self.internal_memory = internal_memory

    def check_memory(self) -> bool:
        """
        Метод проверяет достаточно ли памяти на телефоне для установки требуемого приложения

        :return: Достаточно ли памяти на телефоне

        Примеры:
        >>> phone = SmartPhone("Xiaomi 13", 6.36, 128)
        >>> phone.check_memory()
        """
        ...

    def increase_memory(self, microsdxc: int) -> None:
        """
        Метод увеличивает память телефона с помощью добавления карты памяти

        :param microsdxc: Объем карты памяти (Гбайт)

        :return: Увеличение памяти телефона

        Примеры:
        >>> phone = SmartPhone("Xiaomi 13", 6.36, 128)
        >>> phone.increase_memory(128)
        """
        if not isinstance(microsdxc, int):
            raise TypeError("Объем карты памяти должен быть типа int")
        if microsdxc <= 0:
            raise ValueError("Объем карты памяти должен быть положительным числом")
        ...

    def formatting_memory(self) -> None:
        """
        Метод форматирует память телефона

       :return: Полная очистка памяти, сброс настроек до заводских

       Примеры:
       >>> phone = SmartPhone("Xiaomi 13", 6.36, 128)
       >>> phone.formatting_memory()
        """
        ...


class Fruit:
    def __init__(self, name: str, current_weight: float, country: str, price: float):
        """
        Метод конструктор класса Fruit.

        :param name: Название фруктов
        :param current_weight: Текущий вес фруктов (в тоннах)
        :param country: Страна-поставщик фруктов
        :param price: Цена фруктов (за тонну в $)

        Примеры:
        >>> fruit = Fruit("Tangerine", 12.5, "Morocco", 642.93)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название фруктов должно быть типа str")
        self.name = name

        if not isinstance(current_weight, (int, float)):
            raise TypeError("Текущий вес фруктов должен быть типа int или float")
        if current_weight <= 0:
            raise ValueError("Текущий вес фруктов должен быть положительным")
        self.current_weight = current_weight

        if not isinstance(country, str):
            raise TypeError("Страна-поставщик фруктов должна быть типа str")
        self.country = country

        if not isinstance(price, (int, float)):
            raise TypeError("Цена фруктов должна быть типа int или float")
        if price <= 0:
            raise ValueError("Цена фруктов должна быть положительным числом")
        self.price = price

    def buy(self, buy_: float) -> None:
        """
        Метод увеличивает кол-во (вес) фруктов при покупке

        :param buy_: Вес покупаемых фруктов (в тоннах)

        :return: Увеличивается вес фруктов

        Примеры:
        >>> fruit = Fruit("Tangerine", 12.5, "Morocco", 642.93)
        >>> fruit.buy(2.5)
        """
        if not isinstance(buy_, (int, float)):
            raise TypeError("Вес покупаемых фруктов должен быть типа int или float")
        if buy_ <= 0:
            raise ValueError("Вес покупаемых фруктов должен быть положительным числом")
        ...

    def sell(self, sell_: float) -> None:
        """
        Метод уменьшает кол-во (вес) фруктов при продаже

        :param sell_: Вес продаваемых фруктов (в тоннах)

        :raise ValueError: Ошибка, если вес продаваемых фруктов будет больше, чем текущий вес фруктов

        :return: Уменьшается вес фруктов

         Примеры:
        >>> fruit = Fruit("Tangerine", 12.5, "Morocco", 642.93)
        >>> fruit.sell(5.5)
        """
        if not isinstance(sell_, (int, float)):
            raise TypeError("Вес продаваемых фруктов должен быть типа int или float")
        if sell_ <= 0:
            raise ValueError("Вес продаваемых фруктов должен быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
