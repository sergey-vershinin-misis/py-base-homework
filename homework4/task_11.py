"""
Упражнение 11.
Напишите программу, выполняющую перевод из буквенных оценок в числовые и обратно. Программа должна позволять
пользователю вводить несколько значений для перевода – по одному в каждой строке. Для начала предпримите попытку
сконвертировать введенное пользователем значение из числового в буквенное. Если возникнет исключение, попробуйте
выполнить обратное преобразование – из буквенного в числовое. Если и эта попытка окончится неудачей, выведите
предупреждение о том, что введенное значение не является допустимым. Пусть ваша программа конвертирует оценки
до тех пор, пока пользователь не оставит ввод пустым. При решении данного задания вам поможет таблица перевода оценок
"""


def run_task_11():

    grade_options = [[5, 'A'], [4, 'B'], [4, 'C'], [3, 'D'], [3, 'E'], [2, 'F']]

    def get_numerical_grade(grade_option):
        return grade_option[0]

    def get_literal_grade(grade_option):
        return grade_option[1]

    while True:

        input_str = input('Введите очередную оценку: ').upper()
        if len(input_str) == 0:
            break

        try:
            numerical_value = int(input_str)
        except Exception:
            numerical_value = None

        if numerical_value is not None:
            if (numerical_value > 1) and (numerical_value < 6):
                found_grade_options = filter(lambda opt: get_numerical_grade(opt) == numerical_value, grade_options)
                grades = list(map(get_literal_grade, found_grade_options))
                print('Вызможны следующие буквенные оценки: ', " или ".join(grades))
                continue

        if len(input_str) and (input_str in "".join(map(get_literal_grade, grade_options))):
            found_grade_options = filter(lambda opt: get_literal_grade(opt) == input_str, grade_options)
            grades = list(map(get_numerical_grade, found_grade_options))
            print('Вызможны следующие числовые оценки: ', " или ".join(map(str, grades)))
            continue

        print(f'Не удалось преобразовать оценку "{input_str}" к другой форме')



