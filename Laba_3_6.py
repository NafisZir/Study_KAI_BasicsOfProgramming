import random
try:
    minimum = int(input("Введите минимальное число: "))
    maximum = int(input("Введите максимальное число: "))

    T = [[[random.randint(minimum, maximum) for i in range(7)] for j in range(5)] for l in range(3)]
    for i in range(0, 3):
        for l in range(0, 5):
            print(T[i][l])
        print("\n")
    number = 0
    k, h, j = 0, 0, 0
    for x in range(3):
        for y in range(5):
            for z in range(7):
                if T[k][h][j] < T[x][y][z]:
                    number = T[x][y][z]
                    k = x
                    h = y
                    j = z
    print("Наибольшое число:", number, "\nЕго индексы", k, h, j)
except ValueError:
    print("Ошибка ввода! Перезапустите программу.")
