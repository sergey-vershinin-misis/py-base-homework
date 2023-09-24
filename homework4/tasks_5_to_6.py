"""
Упражнение 5.
Создать класс для часов. Должна быть возможность установить время при создании объекта. Также необходимо реализовать
методы, с помощью которых можно добавлять по одной минуте/секунде или по одному часу к текущему времени. Помнить, что
значения минут и секунд не могут превышать 59, а часов 23.

Упражнение 6.
Доработать предыдущую задачу, чтобы можно было складывать двое часов друг с другом. Для перегрузки оператора +
использовать метод __add__(self, other).
"""


class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.check_clock_init_values(hours, minutes, seconds)
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def check_clock_init_values(self, hours, minutes, seconds):
        if (hours < 0) or (hours > 23):
            raise ValueError('Количество часов должно лежать в диапазоне от 0 до 23 включительно')
        if (minutes < 0) or (minutes > 59):
            raise ValueError('Количество минут должно лежать в диапазоне от 0 до 59 включительно')
        if (seconds < 0) or (seconds > 59):
            raise ValueError('Количество секунд должно лежать в диапазоне от 0 до 59 включительно')

    def __repr__(self):
        return f'{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}'

    def __add_hours(self, hours_to_add: int = 1):
        self.__hours = (self.__hours + hours_to_add) % 24

    def __add_minutes(self, minutes_to_add: int = 1):
        minutes = self.__minutes + minutes_to_add
        self.__minutes = minutes % 60
        self.__add_hours(minutes // 60)

    def __add_seconds(self, seconds_to_add: int = 1):
        seconds = self.__seconds + seconds_to_add
        self.__seconds = seconds % 60
        self.__add_minutes(seconds // 60)

    def add_hour(self):
        self.__add_hours()

    def add_minute(self):
        self.__add_minutes()

    def add_second(self):
        self.__add_seconds()

    def __add__(self, other: "Clock"):
        new_clock = self.__clone()
        new_clock.add_clock(other)
        return new_clock

    def add_clock(self, other: "Clock"):
        if not isinstance(other, Clock):
            raise ValueError("Сложение может происходить только между жвумя экземплярами класса Clock")

        self.__add_seconds(other.seconds)
        self.__add_minutes(other.minutes)
        self.__add_hours(other.hours)

    def __clone(self):
        return Clock(self.__hours, self.__minutes, self.__seconds)


def run_task_5_to_6():
    c = Clock(3, 45, 45)
    print(c)
    for i in range(20): c.add_second()
    print(c)
    for i in range(20): c.add_minute()
    print(c)
    for i in range(21): c.add_hour()
    print(c)
    c+= Clock(2, 59, 59)
    print(c)