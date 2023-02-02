from typing import Union

import doctest


class Video:
    def __init__(self, length: Union[int, float], video_format: str):
        """
        Метод конструктор объекта "Video".

        :param length: Продолжительность видео
        :param video_format: Формат видео

        Примеры:
        >>> new_video = Video(35.48, 'mp4')  # инициализация экземпляра класса
        """
        self.playback_speed = 1

        if not isinstance(length, (int, float)):
            raise TypeError("Продолжительность видео должна быть типа int или float")
        if length <= 0:
            raise ValueError("Продолжительность видео должна быть положительным числом")
        self.length = length

        if not isinstance(video_format, str):
            raise TypeError("Формат видео должен быть типа str")
        self.video_format = video_format

    def cropping(self, crop_video: Union[int, float]) -> (int, float):
        """
        Метод обрезает видео.

        :param crop_video: Обрезаемый фрагмент видео

        Примеры:
        >>> new_video = Video(35.48, 'mp4')
        >>> new_video.cropping(12.37)
        12.37
        """
        if not isinstance(crop_video, (int, float)):
            raise TypeError("Обрезаемый фрагмент видео должен быть типа int или float")
        if crop_video <= 0:
            raise ValueError("Обрезаемый фрагмент видео должен быть положительным числом")
        if crop_video >= self.length:
            raise ValueError("Обрезанный фрагмент должен быть меньше продолжительности видео")
        self.length = crop_video
        return crop_video

    def reformat(self, new_format: str) -> str:
        """
        Метод изменяет формат видео.

        :param new_format: Новый формат видео

        Примеры:
        >>> new_video = Video(35.48, 'mp4')
        >>> new_video.reformat('avi')
        'avi'
        """
        if not isinstance(new_format, str):
            raise TypeError("Новый формат видео должен быть типа str")
        self.video_format = new_format
        return new_format

    def speed(self, new_speed: Union[int, float]) -> (int, float):
        """
        Метод изменяет скорость воспроизведения видео.

        :param new_speed: Требуемая скорость воспроизведения видео

        Примеры:
        >>> new_video = Video(35.48, 'mp4')
        >>> new_video.speed(1.5)
        1.5
        """
        if not isinstance(new_speed, (int, float)):
            raise TypeError("Скорость видео должна быть типа int или float")
        if not 0.25 <= new_speed <= 2:
            raise ValueError("Не соответствие диапазону изменения значений скорости воспроизведения видео")
        self.playback_speed = new_speed
        return new_speed


class SmartPhone:
    def __init__(self, model: str, diagonal: Union[int, float], internal_memory: int):
        """
        Метод конструктор объекта "SmartPhone".

        :param model: Модель телефона
        :param diagonal: Диагональ дисплея телефона (дюйм)
        :param internal_memory: Внутренняя память телефона (Гбайт)

        Примеры:
        >>> phone = SmartPhone("Xiaomi 13", 6.36, 128)
        """
        if not isinstance(model, str):
            raise TypeError("Модель телефона должна быть типа str")
        self.model = model

        if not isinstance(diagonal, (int, float)):
            raise TypeError("Диагональ дисплея телефона должна быть типа int или float")
        if diagonal <= 0:
            raise ValueError("Диагональ дисплея телефона должна быть положительным числом")
        self.diagonal = diagonal

        if not isinstance(internal_memory, int):
            raise TypeError("Внутренняя память телефона должна быть типа int")
        if internal_memory <= 0:
            raise ValueError("Внутренняя память телефона должна быть положительным числом")
        self.internal_memory = internal_memory

    def check_memory(self) -> bool:
        """
        Метод проверяет наличие свободного места в памяти телефона.

        :return: Достаточно ли памяти на телефоне

        Примеры:
        >>> phone = SmartPhone("Xiaomi 13", 6.36, 128)
        >>> phone.check_memory()
        """
        pass

    def increase_memory(self, memory_card: int) -> int:
        """
        Метод увеличивает память телефона с помощью добавления карты памяти.

        :param memory_card: Объем карты памяти (Гбайт)
        :return: Увеличение памяти телефона

        Примеры:
        >>> phone = SmartPhone("Xiaomi 13", 6.36, 128)
        >>> phone.increase_memory(128)
        256
        """
        if not isinstance(memory_card, int):
            raise TypeError("Объем карты памяти должен быть типа int")
        if memory_card <= 0:
            raise ValueError("Объем карты памяти должен быть положительным числом")
        return self.internal_memory + memory_card

    def formatting_memory(self) -> None:
        """
        Метод форматирует память телефона.

       Примеры:
       >>> phone = SmartPhone("Xiaomi 13", 6.36, 128)
       >>> phone.formatting_memory()
        """
        pass


class Fruit:
    def __init__(self, name: str, current_weight: Union[int, float], country: str, price: Union[int, float]):
        """
        Метод конструктор объекта "Fruit".

        :param name: Название фруктов
        :param current_weight: Текущий вес фруктов (в тоннах)
        :param country: Страна-поставщик фруктов
        :param price: Цена фруктов (за тонну в $)

        Примеры:
        >>> fruit = Fruit("Tangerine", 12.5, "Morocco", 642.93)
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

    def buy(self, buy_fruit: Union[int, float]) -> (int, float):
        """
        Метод увеличивает кол-во (вес) фруктов при покупке.

        :param buy_fruit: Вес покупаемых фруктов (в тоннах)
        :return: Увеличивает кол-во (вес) фруктов

        Примеры:
        >>> fruit = Fruit("Tangerine", 12.5, "Morocco", 642.93)
        >>> fruit.buy(2.5)
        15.0
        """
        if not isinstance(buy_fruit, (int, float)):
            raise TypeError("Вес покупаемых фруктов должен быть типа int или float")
        if buy_fruit <= 0:
            raise ValueError("Вес покупаемых фруктов должен быть положительным числом")
        return self.current_weight + buy_fruit

    def sell(self, sell_fruit: Union[int, float]) -> (int, float):
        """
        Метод уменьшает кол-во (вес) фруктов при продаже.

        :param sell_fruit: Вес продаваемых фруктов (в тоннах)
        :return: Уменьшает кол-во (вес) фруктов

        Примеры:
        >>> fruit = Fruit("Tangerine", 12.5, "Morocco", 642.93)
        >>> fruit.sell(5.5)
        7.0
        """
        if not isinstance(sell_fruit, (int, float)):
            raise TypeError("Вес продаваемых фруктов должен быть типа int или float")
        if sell_fruit <= 0:
            raise ValueError("Вес продаваемых фруктов должен быть положительным числом")
        if sell_fruit > self.current_weight:
            raise ValueError("Вес продаваемых фруктов не должен превышать текущий вес фруктов")
        return self.current_weight - sell_fruit


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
