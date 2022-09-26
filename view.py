def get_data():
    a = int(float(input("Введите переменную: ")))
    b = int(float(input("Введите переменную: ")))
    return a, b


def get_chois():
    a = int(input("Введите 1, если деление без остатка или 2, если остаток от деления: "))
    return a


def get_rezult(rezult):
    print(f'Результат вашей операции: {rezult}')
