# Задание №1
# Пункт 1
string = input("Введите строку: ")
length = len(string)
d = string[:length - 1:]
lst = d.replace('*', '')
lst = lst.split()

# Пункт 2
quantityWord = len(lst)

# Пункт 3
i = 0
k = 0
for j in range(1, len(lst)):
    if len(lst[i]) < len(lst[j]):
        i = j
    if len(lst[k]) > len(lst[j]):
        k = j
longWord = len(lst[i])
shortWord = len(lst[k])

# Пункт 4
string2 = ''
for q in string:
    if q == '*':
        continue
    string2 += q * 2

print("a) ", length, "\nb) ", quantityWord, "\nc) Количество символов в длинном слове: ", longWord)
print("Cимволы в коротком слове: ", shortWord, "\nd) ", string2)
