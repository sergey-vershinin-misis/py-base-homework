"""
Упражнение 1.
Дан список из чисел.
Определите их НОК (наименьшее общее кратное) и НОД (наибольший общий делитель).
"""
from math import floor


# TO BE DONE SOON
def run_task_01():
    def prime_dividers(number: int) -> dict:
        initial_number = number
        dividers = dict()
        for divider in range(2, number // 2):
            while number % divider == 0:
                dividers[divider] = dividers.get(divider, 0) + 1
                number = number // divider
        if len(dividers) == 0:
            dividers[initial_number] = 1
        return dividers

    def number_from_dividers(dividers: dict) -> int:
        result = 1
        for key, value in dividers.items():
            result *= key ** value
        return result

    def intersect_common_dividers(*args) -> dict:
        if len(args) == 0:
            return None

        dividers1 = args[0]
        for dividers2 in args[1:]:
            dividers1 = {key: min(dividers1[key], dividers2[key]) for key in dividers2 if key in dividers1}

        return dividers1

    def unite_common_dividers(*args) -> dict:
        if len(args) == 0:
            return None

        dividers1 = args[0]
        for dividers2 in args[1:]:
            primes = set(dividers1) & set(dividers1)
            dividers1 = {key: max(dividers1.get(key, 0), dividers2.get(key, 0)) for key in primes}

        return dividers1

    def greatest_common_divider(*args: list[int]) -> int:
        return number_from_dividers(intersect_common_dividers(*map(lambda arg: prime_dividers(arg), args)))

    def least_common_multiple(*args: list[int]) -> int:
        return number_from_dividers(unite_common_dividers(*map(lambda arg: prime_dividers(arg), args)))

    args = [59459400, 2156220, 650650]
    print('Числа, для которых вычисляется НОД и НОК: ', args)
    print('НОД:', greatest_common_divider(*args))
    print('НОК:', least_common_multiple(*args))
