"""
Упражнение 9.
Напишите программу, которая позволит пользователю преобразовывать числа из одной системы счисления в другую
произвольным образом. Ваша программа должна поддерживать все системы счисления в диапазоне от 2 до 16 как для входных,
так и для выходных данных. Если пользователь выберет систему с основанием, выходящим за границы допустимого, на экран
должна быть выведена ошибка. Разделите код программы на несколько функций, включая функцию, конвертирующую число из
произвольной системы счисления в десятичную, и обратную функцию, переводящую значение из десятичной системы в
произвольную. В основной программе необходимо запросить у пользователя исходную систему счисления, целевую систему,
а также число для преобразования.
"""


def run_task_09():
    symbols_to_values = {str(i): i for i in range(10)} | {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    values_to_symbols = {symbols_to_values[i]: i for i in symbols_to_values}

    def to_decimal_value(string_with_number: str, source_system_base: int) -> int:
        digit_list = map(lambda digit_symbol: symbols_to_values[digit_symbol], string_with_number)
        decimal_value = 0
        for digit in digit_list:
            decimal_value = decimal_value * source_system_base + digit
        return decimal_value

    def from_decimal_value(value: int, target_system_base: int) -> str:
        digit_symbol_list = []
        while value > 0:
            digit_symbol_list.append(values_to_symbols[value % target_system_base])
            value = value // target_system_base
        return ''.join(reversed(digit_symbol_list))

    source_system_base = int(input('Введите основание системы счисления исходного числа (от 2 до 16): '))
    if not (1 < source_system_base < 17):
        print('Основание системы счисления должно быть от 2 до 16')
        return

    target_system_base = int(input('Введите основание системы счисления для целевого числа (от 2 до 16): '))
    if not (1 < target_system_base < 17):
        print('Основание системы счисления должно быть от 2 до 16')
        return

    string_with_number = input(
        f'Введите число в системе счисления с основанием {source_system_base} для перевода: ')

    print(f'Введенное число в системе счисления с основание {target_system_base}:',
          from_decimal_value(to_decimal_value(string_with_number, source_system_base), target_system_base))
