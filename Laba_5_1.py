f = open('in.txt', 'r')
lst = str(f.read()).replace(',', '').replace('.', '').split()
word = input("Введите слово: ")
for i in lst:
    if i == word:
        lst.remove(i)
f.close()
f = open('out.txt', 'w')
for i in lst:
    f.write(i + " ")
f.close()
