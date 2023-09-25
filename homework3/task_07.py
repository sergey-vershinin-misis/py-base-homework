"""
Упражнение 7.
Строка называется палиндромом, если она пишется одинаково в обоих направлениях. Например, палиндромами в английском
языке являются слова «anna», «civic», «level», «hannah». Напишите программу, запрашивающую у пользователя строку и
при помощи цикла определяющую, является ли она палиндромом.
"""


def run_task_07():
    input_str = input('Введите строку для проверки на палиндром: ')
    input_str = input_str.replace(' ', '').lower()

    is_palindrome = True
    for l in range(len(input_str) // 2):
        r = -1 * l - 1

        if input_str[l] != input_str[r]:
            is_palindrome = False
            break

    print('Строка является палиндромом: ', is_palindrome)

