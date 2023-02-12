class AcElectricMachine:
    """Базовый класс электрических машин переменного тока."""
    def __init__(self, name: str, voltage: int, current: int, rotation: int, frequency: int):
        """
        Метод конструктор объекта 'AcElectricMachine'.

        :param name: Наименование
        :param voltage: Напряжение (Вольт)
        :param current: Ток (Ампер)
        :param rotation: Скорость вращения (об/мин)
        :param frequency: Частота тока (Герц)
        """
        # Текущие значения параметров электрических машин переменного тока
        self.voltage_value: int = 0
        self.current_value: int = 0
        self.rotation_value: int = 0
        self.frequency_value: (int, float) = 0

        if not isinstance(name, str):
            raise TypeError("Наименование должно быть типа str")
        self._name = name

        if not isinstance(voltage, int):
            raise TypeError("Ток должен быть типа int")
        if voltage <= 0:
            raise ValueError("Напряжение должно быть положительным числом")
        self._voltage = voltage

        if not isinstance(current, int):
            raise TypeError("Ток должен быть типа int")
        if current <= 0:
            raise ValueError("Ток должен быть положительным числом")
        self._current = current

        if not isinstance(rotation, int):
            raise TypeError("Скорость вращения должна быть типа int")
        if rotation <= 0:
            raise ValueError("Скорость вращения должна быть положительным числом")
        self._rotation = rotation

        if not isinstance(frequency, int):
            raise TypeError("Частота тока должна быть типа int")
        if frequency <= 0:
            raise ValueError("Частота тока должна быть положительным числом")
        self._frequency = frequency

    # Защищаем номинальные параметры оборудования. Изменяться могут только текущие значения (при эксплуатации).
    @property
    def name(self) -> str:
        """Возвращает наименование электрической машины переменного тока."""
        return self._name

    @property
    def voltage(self) -> int:
        """Возвращает значение напряжения электрической машины переменного тока."""
        return self._voltage

    @property
    def current(self) -> int:
        """Возвращает значение тока электрической машины переменного тока."""
        return self._current

    @property
    def rotation(self) -> int:
        """Возвращает значение скорости вращения электрической машины переменного тока."""
        return self._rotation

    @property
    def frequency(self) -> int:
        """Возвращает значение частоты электрической машины переменного тока."""
        return self._frequency

    def __str__(self) -> str:
        """Возвращает f-строку."""
        return f"Электрическая машина переменного тока {self.name}. Напряжение {self.voltage}. Ток {self.current}. " \
               f"Скорость вращения {self.rotation}. Частота тока {self.frequency}."

    def __repr__(self) -> str:
        """Возвращает f-строку."""
        return f"{self.__class__.__name__}(name={self.name!r}, voltage={self.voltage}, current={self.current}, " \
               f"rotation= {self.rotation}, frequency={self.frequency})"

    def switch_on(self) -> None:
        """Метод включает электрическую машину."""
        # Исходные текущие значения возрастают до номинальных
        self.voltage_value += self._voltage
        self.current_value += self._current
        self.rotation_value += self._rotation
        self.frequency_value += self._frequency

    def switch_off(self) -> None:
        """Метод отключает электрическую машину."""
        # Текущие значения параметров снижаются до нуля.
        self.voltage_value = 0
        self.current_value = 0
        self.rotation_value = 0
        self.frequency_value = 0

    def display_voltage(self) -> None:
        """Метод показывает текущее значение напряжения электрической машины переменного тока."""
        if not isinstance(self.voltage_value, int):
            raise TypeError("Напряжение должно быть типа int")
        if self.voltage_value < 0:
            raise ValueError("Напряжение не может быть отрицательным числом")
        if self.voltage_value == 0:
            print(f"{self.voltage_value} - электрическая машина отключена")
        if self.voltage_value < (0.9 * self._voltage):
            print(f"{self.voltage_value} - напряжение электрической машины < 0.9 Uном")
        if self.voltage_value > (1.1 * self._voltage):
            print(f"{self.voltage_value} - напряжение электрической машины > 1.1 Uном")
        else:
            print(f"{self.voltage_value} - допустимое значение напряжения электрической машины")

    def display_current(self) -> None:
        """Метод показывает текущее значение тока электрической машины переменного тока."""
        if not isinstance(self.current_value, int):
            raise TypeError("Ток должен быть типа int")
        if self.current_value < 0:
            raise ValueError("Ток не может быть отрицательным числом")
        if self.current_value == 0:
            print(f"{self.voltage_value} - электрическая машина отключена")
        if self.current_value < self._current:
            print(f"{self.current_value} - электрическая машина работает на холостом ходу")
        if self.current_value > self._current:
            print(f"{self.current_value} - электрическая машина перегружена")
        if self.current_value == self._current:
            print(f"{self.current_value} - ток электрической машины номинальный")


class AsynchronousMotor(AcElectricMachine):
    """Дочерний класс асинхронных электродвигателей."""
    def __init__(self, name: str, voltage: int, current: int, rotation: int, frequency: (int, float), use_power: int):
        super().__init__(name, voltage, current, rotation, frequency)
        """
        Метод конструктор объекта "AsynchronousMotor".
        
        :param use_power: Потребляемая мощность (Ватт)
        """
        self.use_power_value = 0  # текущее значение потребляемой мощности (электродвигатель отключен)

        if not isinstance(use_power, int):
            raise TypeError("Потребляемая мощность должна быть типа int")
        if use_power <= 0:
            raise ValueError("Потребляемая мощность должна быть положительным числом")
        self._use_power = use_power

    # Защищаем номинальные параметры оборудования. Изменяться могут только текущие значения (при эксплуатации).
    @property
    def use_power(self) -> int:
        """Возвращает значение потребляемой мощности электродвигателя."""
        return self._use_power

    def __str__(self) -> str:
        """Возвращает f-строку."""
        return f"Электрическая машина переменного тока {self.name}. Напряжение {self.voltage}. Ток {self.current}. " \
               f"Скорость вращения {self.rotation}. Частота тока {self.frequency}. " \
               f"Потребляемая мощность {self.use_power}."

    def __repr__(self) -> str:
        """Возвращает f-строку."""
        return f"{self.__class__.__name__}(name={self.name!r}, voltage={self.voltage}, current={self.current}, " \
               f"rotation= {self.rotation}, frequency={self.frequency}, use_power={self.use_power})"

    def switch_on(self) -> None:
        """Метод (перегружаемый). Включает электродвигатель."""
        self.voltage_value += self._voltage
        self.current_value += self._current
        self.rotation_value += self._rotation
        self.frequency_value += self._frequency
        self.use_power_value += self._use_power  # вносим параметр электродвигателей

    def switch_off(self) -> None:
        """Метод (перегружаемый). Отключает электродвигатель."""
        self.voltage_value = 0
        self.current_value = 0
        self.rotation_value = 0
        self.frequency_value = 0
        self.use_power_value = 0

    def display_use_power(self) -> None:
        """Метод показывает текущее значение потребляемой мощности электродвигателя."""
        if not isinstance(self.use_power_value, int):
            raise TypeError("Потребляемая мощность должна быть типа int")
        if self.use_power_value < 0:
            raise ValueError("Потребляемая мощность не может быть отрицательным числом")
        if self.use_power_value == 0:
            print(f"{self.use_power_value} - электродвигатель отключен")
        if self.use_power_value < self._use_power:
            print(f"{self.use_power_value} - электродвигатель работает на холостом ходу")
        if self.use_power_value == self._use_power:
            print(f"{self.use_power_value} - потребляемая мощность номинальная")
        if self.use_power_value > self._use_power:
            print(f"{self.use_power_value} - электродвигатель перегружен")


class SynchronousGenerator(AcElectricMachine):
    """Дочерний класс синхронных генераторов."""
    def __init__(self, name: str, voltage: int, current: int, rotation: int, frequency: (int, float), gen_power: int):
        super().__init__(name, voltage, current, rotation, frequency)
        """
        Метод конструктор объекта "SynchronousGenerator".
        
        :param gen_power: Вырабатываемая мощность
        """
        self.gen_power_value = 0  # текущее значение вырабатываемой мощности (генератор отключен)

        if not isinstance(gen_power, int):
            raise TypeError("Вырабатываемая мощность должна быть типа int")
        if gen_power <= 0:
            raise ValueError("Вырабатываемая мощность должна быть положительным числом")
        self._gen_power = gen_power

    # Защищаем номинальные параметры оборудования. Изменяться могут только текущие значения (при эксплуатации).
    @property
    def gen_power(self) -> int:
        """Возвращает значение вырабатываемой мощности электродвигателя."""
        return self._gen_power

    def __str__(self) -> str:
        """Возвращает f-строку."""
        return f"Электрическая машина переменного тока {self.name}. Напряжение {self.voltage}. Ток {self.current}. " \
               f"Скорость вращения {self.rotation}. Частота тока {self.frequency}. " \
               f"Вырабатываемая мощность {self.gen_power}."

    def __repr__(self) -> str:
        """Возвращает f-строку."""
        return f"{self.__class__.__name__}(name={self.name!r}, voltage={self.voltage}, current={self.current}, " \
               f"rotation= {self.rotation}, frequency={self.frequency}, gen_power={self.gen_power})"

    def switch_on(self) -> None:
        """Метод (перегружаемый). Запускает (включает) генератор."""
        self.voltage_value += self._voltage
        self.current_value += self._current
        self.rotation_value += self._rotation
        self.frequency_value += self._frequency
        self.gen_power_value += self._gen_power  # вносим параметр генераторов

    def switch_off(self) -> None:
        """Метод (перегружаемый). Останавливает (отключает) генератор."""
        self.voltage_value = 0
        self.current_value = 0
        self.rotation_value = 0
        self.frequency_value = 0
        self.gen_power_value = 0

    def display_gen_power(self) -> None:
        """Метод показывает текущее значение потребляемой мощности электродвигателя."""
        if not isinstance(self.gen_power_value, int):
            raise TypeError("Вырабатываемая мощность должна быть типа int")
        if self.gen_power_value < 0:
            raise ValueError("Вырабатываемая мощность не может быть отрицательным числом")
        if self.gen_power_value > self._gen_power:
            raise ValueError("Вырабатываемая мощность генератора не может быть больше номинальной")
        if self.gen_power_value == 0:
            print(f"{self.gen_power_value} - генератор отключен")
        if self.gen_power_value < self._gen_power:
            print(f"{self.gen_power_value} - генератор недогружен")
        if self.gen_power_value == self._gen_power:
            print(f"{self.gen_power_value} - вырабатываемая мощность номинальная")


if __name__ == "__main__":
    # Write your solution here
    motor = AsynchronousMotor("AMA 450L4L", 10000, 51, 1489, 50, 710000)  # инициализация
    print(motor.current_value)
    motor.switch_on()
    print(motor.use_power_value)
    motor.display_current()
