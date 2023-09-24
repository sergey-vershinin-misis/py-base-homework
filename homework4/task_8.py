"""
Упражнение 8 (Задача просто на классы, без обработки исключений).
Для одной задачи необходимо реализовать следующее - при соединении двух элементов получается новый. У нас есть 4
базовых элемента: Вода, Воздух, Огонь, Земля. Из них как раз и получаются новые: Шторм, Пар, Грязь, Молния, Пыль, Лава.
Вот таблица преобразований:
  Вода + Воздух = Шторм
  Вода + Огонь = Пар
  Вода + Земля = Грязь
  Воздух + Огонь = Молния
  Воздух + Земля = Пыль
  Огонь + Земля = Лава

Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
Если результат не определен - то возвращается None.
Примечание: сложение объектов можно реализовывать через магический метод add, вот пример использования:
"""
from _testcapi import instancemethod


class Element:
    def __init__(self):
        self.__class_name = type(self)

    @property
    def class_name(self):
        return self.__class_name

    def __repr__(self):
        return str(type(self).__name__)


class Water(Element):
    def __add__(self, other):
        if isinstance(other, Water):
            return Water()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Element):
            return other + self
        else:
            return None


class Air(Element):
    def __add__(self, other):
        if isinstance(other, Air):
            return Air()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Element):
            return other + self
        else:
            return None


class Fire(Element):
    def __add__(self, other):
        if isinstance(other, Fire):
            return Fire()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Element):
            return other + self
        else:
            return None


class Earth(Element):
    def __add__(self, other):
        if isinstance(other, Earth):
            return Earth()
        elif isinstance(other, Element):
            return other + self
        else:
            return None


class FifthElement(Element):
    def __add__(self, other):
        if isinstance(other, FifthElement):
            return FifthElement()
        elif isinstance(other, Element):
            return Life()
        else:
            return None


class Life:
    pass


class Storm:
    pass


class Steam:
    pass


class Dirt:
    pass


class Lightning:
    pass


class Dust:
    pass


class Lava:
    pass


def run_task_8():
    print("Вода + Воздух = Воздух + Вода = Шторм: ",
          isinstance(Water() + Air(), Storm) and isinstance(Air() + Water(), Storm))

    print("Вода + Огонь = Огонь + Вода = Пар: ",
          isinstance(Water() + Fire(), Steam) and isinstance(Fire() + Water(), Steam))

    print("Вода + Земля = Земля + Вода = Грязь: ",
          isinstance(Water() + Earth(), Dirt) and isinstance(Earth() + Water(), Dirt))

    print("Воздух + Огонь = Огонь + Воздух = Молния: ",
          isinstance(Air() + Fire(), Lightning) and isinstance(Fire() + Air(), Lightning))

    print("Воздух + Земля = Земля + Воздух = Пыль: ",
          isinstance(Air() + Earth(), Dust) and isinstance(Earth() + Air(), Dust))

    print("Огонь + Земля = Земля + Огонь = Лава: ",
          isinstance(Fire() + Earth(), Lava) and isinstance(Earth() + Fire(), Lava))

    print("Пятый элемент + Любой из 4х элементов = Жизнь: ",
          isinstance(FifthElement() + Earth(), Life) and isinstance(FifthElement() + Fire(), Life) and
          isinstance(Air() + FifthElement(), Life))

    print("\n\nЗемля + Пыль = None: ", isinstance(Earth() + Dust(), type(None)))
    print("Земля + Земля = Земля: ", isinstance(Earth() + Earth(), Earth))
    print(isinstance(FifthElement() + FifthElement(), FifthElement))
