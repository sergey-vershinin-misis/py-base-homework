"""
Упражнение 6.
Напишите функцию, которая принимает неограниченное количество числовых аргументов и возвращает кортеж из двух списков:
отрицательных значений (отсортирован по убыванию);
неотрицательных значений (отсортирован по возрастанию).
"""


def run_task_06():

    negative_numbers = []
    non_negative_numbers = []
    while True:
        string_input = input('Введите число (для перехода к расчету - введите пустую строку):')
        if len(string_input) == 0:
            break

        number = int(string_input)
        if number < 0:
            negative_numbers.append(number)
        else:
            non_negative_numbers.append(number)

    result = (sorted(negative_numbers, reverse=True), sorted(non_negative_numbers))
    print('Результат:\n', result)

