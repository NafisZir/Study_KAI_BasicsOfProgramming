import math

# Task 1

print("\nTask 1")
a = float(input("Enter the value of the first cathet: "))
b = float(input("Enter the value of the second cathet: "))

c = (a**2 + b**2)**0.5
P = a + b + c

print("Hypotenuse is equal = ", c ,"\nPerimetr is equal = ", P )

# Task 2

print("\nTask 2")
radius1 = float(input("Enter a larger radius value: "))
radius2 = float(input("Enter a smaller radius value: "))

Pi = math.pi
s1 = Pi*radius1**2

s2 = Pi*radius2**2
s3 = s1-s2

type(Pi)

print("The area of the big circle is: ", s1, "\nThe area of a small circle is: ", s2, "\nThe area of the ring is: ", s3)

# Task 3

print("\nTask 3")
X = float(input("Enter the mass of chocolates: "))
A = float(input("Enter their price: "))
Y = float(input("Enter the mass of toffee: "))
B = float(input("Enter their price: "))

XA = A/X
YB = B/Y
AAA = XA/YB

print("1 kg chocolates: ", XA, "\n1 kg toffee: ", YB, "\nChocolate is more expensive than toffee on: ", AAA)

# Task 4

print("\nTask 4")
AA = float(input("Enter an integer A greater than zero: "))
BB = float (input("Enter integer B, which 0 < B < A : "))

AB = AA + BB
H = AB//BB

print(H)

# Task 5

print("\nTask 5")
q = float(input("Enter a three digit number: "))

x1 = q // 100
x2 = (q - x1*100) // 10
x3 = (q - x1*100) % 10

Summ = x1 + x2 + x3
Proiz = x1*x2*x3

print("Sum of digits: ", Summ, "\nProduct of numbers: ", Proiz)

# Task 6

print("\nTask 6")
Q = int(input("Enter a three digit number: "))

y1 = Q // 100
y2 = (Q - y1*100) // 10
y3 = (Q - y1*100) % 10

print(y3, y2, y1)

# Task 7

print("\nTask 7")
W = int(input("Enter a three digit number: "))

z1 = W // 100
z2 = (W - z1*100) // 10
z3 = (W - z1*100) % 10

print(z2, z3, z1)
