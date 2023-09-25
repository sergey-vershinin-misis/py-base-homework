"""
Упражнение 2.
Даны n предложений. Определите, сколько из них содержат хотя бы одну цифру.
"""
def run_task_02():
    sentences = [
        'Предложение 1.',
        'Предложение два',
        'Предложение 23',
        'Предложение 44',
        'Предложение шесть'
    ]

    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

    target_counter = 0
    for sentence in sentences:
        target_counter += int(any(char in digits for char in sentence))

    print(f'В списке предложений {target_counter} содержат хотя бы одну цифру')
