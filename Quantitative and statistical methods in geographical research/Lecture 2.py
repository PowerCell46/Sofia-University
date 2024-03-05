import math


def avg(*args):
    return sum(*args) / len(*args)


# Dispersion

def range(*args):
    return max(args) - min(args)


def standard_deviation_sample(*args):
    average_value = avg(args)  # 1. Изчислете средно аритметично за групата
    res2 = 0  # 4. Сумирайте всички получени стойности
    for value in args:  # 2. Извадете средно аритметичното от всеки резултат
        res2 += (value - average_value) ** 2  # 3. Поставете на квадрат получените разлики.
    res3 = res2 / (len(args) - 1)  # 5. Разделете на сумата на елементите
    return math.sqrt(res3)  # 6. Поставете резултата под корен квадратен


def standard_deviation_population(*args):
    average_value = avg(args)  # 1. Изчислете средно аритметично за групата
    res2 = 0  # 4. Сумирайте всички получени стойности
    for value in args:  # 2. Извадете средно аритметичното от всеки резултат
        res2 += (value - average_value) ** 2  # 3. Поставете на квадрат получените разлики.
    res3 = res2 / len(args)  # 5. Разделете сумата на n-1
    return math.sqrt(res3)  # 6. Поставете резултата под корен квадратен


def variance_sample(*args):  # Стандартното отклонение за група от стойности и го поставим на втора степен
    return standard_deviation_sample(*args) ** 2


def variance_population(*args):  # Стандартното отклонение за група от стойности и го поставим на втора степен
    return standard_deviation_population(*args) ** 2


values1 = [98, 86, 77, 56, 48]

print(range(*values1))

values2 = [8, 8, 8, 7, 6, 6, 5, 5, 4, 3]

print(f'{standard_deviation_sample(*values2):.2f}')

print(f'{standard_deviation_population(*values2):.2f}')

print(f'{variance_sample(*values2):.2f}')

print(f'{variance_population(*values2):.2f}')
