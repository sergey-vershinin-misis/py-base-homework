"""
Упражнение 4.
Описать класс десятичного счётчика. Он должен обладать внутренней переменной, хранящей текущее значение, методами
повышения значения (increment) и понижения (decrement), получения текущего значения get_counter. Учесть, что счётчик
не может опускаться ниже 0.
"""


class Counter:
    def __init__(self):
        self.__current_value = 0

    def get_counter(self):
        return self.__current_value

    def decrement(self, steps: int = 1):
        if steps < 1:
            return
        new_value = self.__current_value - steps
        if new_value < 0:
            self.__current_value = 0
        else:
            self.__current_value = new_value

    def increment(self, steps: int = 1):
        self.__current_value += steps


def run_task_4():
    counter = Counter()
    print('Начальное состояние счетчика: ', counter.get_counter())
    counter.decrement()
    print('Уменьшили на 1: ', counter.get_counter())
    counter.increment(3)
    print('Увеличили на 3: ', counter.get_counter())
    counter.decrement(4)
    print('Уменьшили на 4: ', counter.get_counter())
