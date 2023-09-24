"""
Упражнение 9.
Программа написана верно, однако содержит места потенциальных ошибок.
найдите потенциальные источники ошибок (укажите номера строк в строке документации);
используя конструкцию try добавьте в код обработку соответствующих исключений.
"""


class NoAccountError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Печать аккаунтов."""
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    """Выполнить перевод 'value' денег со счета 'account_from' на 'account_to'.

    При переводе денежных средств необходимо учитывать:
        - хватает ли денег на счету, с которого осуществляется перевод;
        - перевод состоит из уменьшения баланса первого счета и увеличения
          баланса второго; если хотя бы на одном этапе происходит ошибка,
          аккаунты должны быть приведены в первоначальное состояние
          (механизм транзакции)
          см. https://ru.wikipedia.org/wiki/Транзакция_(информатика).

    Исключения (raise):
        - NoMoneyToWithdrawError: на счету 'account_from'
                                  не хватает денег для перевода;
        - PaymentError: ошибка при переводе.
        - NoAccountError: в перечне аккаунтов нет аккаунта с заданным именем
    """
    account_from_value = accounts.get(account_from)
    if account_from_value is None:
        raise NoAccountError('Отсутствует акканут для: ' + account_from)

    account_to_value = accounts.get(account_to)
    if account_to_value is None:
        raise NoAccountError('Отсутствует акканут для: ' + account_to)

    if account_from_value < value:
        raise NoMoneyToWithdrawError('Недостаточно средств на аккаунте: ' + account_from)

    try:
        accounts[account_from] = account_from_value - value
        accounts[account_to] = account_to_value + value
    except Exception:
        accounts[account_from] = account_from_value
        accounts[account_to] = account_to_value
        raise PaymentError(f'При переводе {value} c аккаунта {account_from} на аккаунт {account_to} '
                           f'произошка ошибка. Перевод отменен')


def run_task_9():
    accounts = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов"
    }

    print("Перевод от {account_from} для {account_to}...".
          format(**payment_info))

    """
    FIXED: Преобразование введенного значения к int не было обернуто в try except. В случае ввода суммы, которая не 
    приводится к целочисленному значению, программа завершалась с ошибкой
    """
    try:
        payment_info["value"] = int(input("Сумма = "))
    except ValueError:
        print('Введенная сумма имеет некорректный формат')
        return

    transfer_money(accounts, **payment_info)

    print("OK!")

    print_accounts(accounts)
