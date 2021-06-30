def polinom(n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        p = ((2*n-1)*polinom(n-1)-(n-1)*polinom(n-2))/n
        return p


x = int(input("Введите значение х-са: "))
n = int(input("Введите значение n: "))
result = polinom(n)
print("Ответ с рекурсией: ", result)

lst_pol = [1, x]
i = 1
while len(lst_pol)-1 != n:
    i += 1
    p = ((2*i-1)*lst_pol[i-1]-(i-1)*lst_pol[i - 2])/i
    lst_pol.append(p)
print("Ответ с циклом: ", lst_pol[n])
