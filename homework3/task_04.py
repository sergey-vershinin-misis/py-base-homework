"""
Упражнение 4.
Для введенного предложения выведите статистику символ=количество. Регистр букв не учитывается.
"""


def run_task_04():
    sentence = input('Введите предложение:').lower()
    stat_dict = dict()

    for symbol in sentence:
        stat_dict[symbol] = stat_dict.get(symbol, 0) + 1

    print('Символы и число их использований в предложении:\n', stat_dict)
