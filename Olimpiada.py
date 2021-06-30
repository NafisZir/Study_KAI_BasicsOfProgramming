q = int(input())
s = input()
arr = list()

for i in s:
    arr.append(i)

l = 0
r = 0
result = 0
for k in arr:
    if k == 'L':
        l += 1
    else:
        r += 1

if l < r:
    if arr[q-1] == 'L':
        result = (l-1)
    else:
        result = l

elif r == l:
    if arr[q-1] == 'L':
        result = l-1
    if arr[0] == 'R':
        result = r-1
    else:
        result = r

else:
    if arr[0] == "R":
        result = (r-1)
    else:
        result = r

print(result)
