try:
    i = 0
    while i < 1:
        n = int(input("Введите максимальное число: "))
        if n < 0:
            continue
        i += 1
    lst = [i+1 for i in range(1, n)]
    p = 2
    lst2 = []
    for l in lst:
        if l % 7 == 0:
            lst2 += [l]
    j = 1
    while p < n:
        i = 1
        while p < n:
            p = int(p / i)
            i += 1
            p *= i
            try:
                lst.remove(p)
            except ValueError:
                continue
        p = lst[j]
        j += 1
        if lst[len(lst) - 1] == p:
            break
    print(lst2, "\n", [1] + lst)
except ValueError:
    print("Ошибка ввода! Перезапустите программу.")
