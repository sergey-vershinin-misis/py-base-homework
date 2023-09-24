"""
Упражнение 1.
Создайте класс Point, экземпляры которого будут создаваться из координат x и y.

Упражнение 2.
Создайте класс прямоугольник — Rectangle. Метод __init__ принимает две точки — левый нижний и правый верхний угол.
Каждая точка представлена экземпляром класса Point. Реализуйте методы вычисления площади и периметра прямоугольника.

Упражнение 3.
Добавьте в класс Rectangle метод contains. Метод принимает точку и возвращает True, если точка находится внутри
прямоугольника и False в противном случае.

"""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'


class Rectangle:
    def __init__(self, lower_left: Point, upper_right: Point):
        if lower_left.x >= upper_right.x:
            raise ValueError('Координата X левой точки больше или равна координате X правой точки')
        if lower_left.y >= upper_right.y:
            raise ValueError('Координата Y нижней точки больше или равна координате Y верхней точки')

        self.lower_left = lower_left
        self.upper_right = upper_right

        self.__width = upper_right.x - lower_left.x
        self.__height = upper_right.y - lower_left.y

    def get_width(self) -> int:
        return self.upper_right.x - self.lower_left.x

    def get_height(self) -> int:
        return self.upper_right.y - self.lower_left.y

    def get_area(self) -> int:
        return self.get_height() * self.get_width()

    def get_perimeter(self) -> int:
        return (self.get_height() + self.get_width()) * 2

    def contains(self, point: Point) -> bool:
        return ((self.lower_left.x <= point.x <= self.upper_right.x) and
                (self.lower_left.y <= point.y <= self.upper_right.y))

    def __repr__(self):
        return f'Прямоугольник [{self.lower_left}, {self.upper_right}]'


def run_tasks_1_to_3() -> None:
    rect = Rectangle(Point(0, 0), Point(20, 10))
    print(rect)
    print("Площадь: ", rect.get_area())
    print('Периметр: ', rect.get_perimeter())

    point = Point(0, 11)
    print(f'{rect} содержит точку {point}: {rect.contains(point)}')

