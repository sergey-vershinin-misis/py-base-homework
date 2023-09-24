"""
Упражнение 7.
Создать классы для травоядного животного и травы. Животное должно уметь поедать траву, если испытывает голод,
в противном случае отказываться от лакомства. Трава должна обладать питательностью, в зависимости от которой
животное будет насыщаться.
"""


class Grass:
    def __init__(self, nutritional_value: int):
        if nutritional_value < 1:
            raise ValueError('Питательная ценность травы не может быть меньше 1')
        self.__nutritional_value = nutritional_value

    @property
    def nutritional_value(self):
        return self.__nutritional_value

    def __repr__(self):
        return f'трава ценностью {self.nutritional_value} единиц'


class Animal:
    def __init__(self, hunger_threshold: int = 2):
        self.__satiety_level = 0.
        self.__hunger_threshold = hunger_threshold

    @property
    def satiety_level(self) -> int:
        return self.__satiety_level

    def feels_hunger(self) -> bool:
        return self.__satiety_level <= self__hunger_threshold

    def eat_grass(self, grass: Grass) -> bool:
        if not self.feels_hunger():
            return False
        self.__satiety_level += grass.nutritional_value
        return True

    def spend_energy(self, energy_to_spend: int = 1):
        if energy_to_spend < 1:
            raise ValueError('Животное не может расходовать менее одной единицы энергии')
        new_satiety_level = self.__satiety_level - energy_to_spend
        if new_satiety_level < 0:
            new_satiety_level = 0
        self.__satiety_level = new_satiety_level

    def __repr__(self):
        return f'Травоядное (сытость: {self.__satiety_level}, порог голода: {self.__hunger_threshold}, голоден: {self.feels_hunger()})'


def run_task_7():
    animal = Animal(3)
    print(animal)

    grass = Grass(3)
    print(f'\nСкушал траву ({grass}): {animal.eat_grass(grass)}')
    print(animal)

    grass = Grass(3)
    print(f'\nСкушал траву ({grass}): {animal.eat_grass(grass)}')
    print(animal)

    grass = Grass(2)
    print(f'\nСкушал траву ({grass}): {animal.eat_grass(grass)}')
    print(animal)

    animal.spend_energy(2)
    print(f'\nПотратил 2 единицы энергии')
    print(animal)

    grass = Grass(2)
    print(f'\nСкушал траву ({grass}): {animal.eat_grass(grass)}')
    print(animal)

    animal.spend_energy(2)
    print(f'\nПотратил 2 единицы энергии')
    print(animal)

    grass = Grass(2)
    print(f'\nСкушал траву ({grass}): {animal.eat_grass(grass)}')
    print(animal)


