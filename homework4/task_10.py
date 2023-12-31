"""
Упражнение 10.
Напишите программу, которая будет суммировать все числа, введенные пользователем, игнорируя при этом нечисловой ввод.
Выводите на экран текущую сумму чисел после каждого очередного ввода. Ввод пользователем значения, не являющегося
числовым, должен приводить к появлению соответствующего предупреждения, после чего пользователю должно быть предложено
ввести следующее число. Выход из программы будет осуществляться путем пропуска ввода. Удостоверьтесь, что ваша программа
 корректно обрабатывает целочисленные значения и числа с плавающей запятой.
"""


def run_task_10():
    sum = 0.0
    while True:

        input_str = input('Введите следующее число:')
        if len(input_str) == 0:
            break

        value = None
        try:
            value = int(input_str)
        except Exception:
            pass

        try:
            value = float(input_str)
        except Exception:
            pass

        if value is None:
            print(f'Не удалось преобразовать строку {input_str} в числовое значение.')
            continue

        sum += value
        print(f'Общая сумма введенных чисел равна {sum}')

