"""
Упражнение 5.
Используя шифр Цезаря (достаточно только букв русского алфавита, знаки препинания не изменяются),
зашифруйте, а затем расшифруйте введенную строку.
"""


def run_task_05():
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def encrypt(symbol: str, key: int) -> str:
        if symbol not in alphabet:
            return symbol

        i = alphabet.index(symbol)
        i = (i + key) % len(alphabet)
        result = alphabet[i]
        return result

    def decrypt(symbol: str, key: int) -> str:
        return encrypt(symbol, -1 * key)

    sentence = input('Введите предложение, которое хотите зашифровать: ')
    key = int(input('Введите ключ шифрования - натуральное число:' ))

    encrypted = "".join([encrypt(symbol, key) for symbol in sentence])
    print('Зашифрованное предложение:', encrypted)

    decrypted = "".join([decrypt(symbol, key) for symbol in encrypted])
    print('Расшифрованное предложение:', decrypted)

