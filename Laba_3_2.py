# Задание №2
import random
try:
    i = 0
    while i < 1:
        quantity = int(input("Введите количество элементов списка: "))
        if quantity < 0:
            continue
        i += 1
    while i < 2:
        minimum = int(input("Введите минимальное число: "))
        maximum = int(input("Введите максимальное число: "))
        if minimum > maximum:
            print("Максимальное значение должно быть больше минимального.")
            continue
        i += 1

    lst = [random.randint(minimum, maximum) for lst in range(quantity)]
    print(lst)
    a = len(lst) -1
    i = 1
    while i <= a:
        if lst[i] >= 0:
            i += 2
            continue
        if lst[i] < 0:
            b = lst.pop(i)
            lst = [b] + lst
        i += 2
    print(lst)
except ValueError:
    print("Ошибка ввода! Перезапустите программу.")
