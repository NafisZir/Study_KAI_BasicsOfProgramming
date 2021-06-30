import random
try:
    n = int(input("Введите количество строк и столбцов квадратной матрицы: "))
    matrix = [[random.randint(-5,5) for i in range(n)]for j in range(n)]
    i = 0
    while i < n:
        print(matrix[i])
        i += 1
    j = 0
    k = n
    number, number2 = 0, 0
    while j <= n - 1:
        if float(matrix[j][j]) == 0.0:
            number += 1
        if float(matrix[j][k - 1]) == 0.0:
            number2 += 1
            k -= 1
        j += 1
    print("Нули главной диагонали: ", number, "\nНули побочной диагонали: ", number2)
except ValueError:
    print("Ошибка ввода! Перезапустите программу.")
