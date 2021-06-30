import random
try:
    quantity = int(input("Введите количество: "))
    lst = [random.randint(-10, 10) for lst in range(quantity)]
    print(lst)
    i, k, g, r = 0, 0, 0, 0
    while i < quantity-3:
        if (lst[i] > 0) and (lst[i+1]) < 0:
            k = i+1
            while (lst[i+2] < 0) and ((i + 2) < (quantity - 1)):
                i += 1
            g = i+1
            r = (g-k)
            if r < 1:
                i += 1
                continue
            if lst[i + 2] > 0:
                while g >= k:
                    lst.pop(g)
                    g -= 1
                i -= (r + 2)
                quantity -= r + 1
                continue
        i += 1
    print(lst)
except ValueError:
    print("Ошибка ввода!Перезапустите программу.")
