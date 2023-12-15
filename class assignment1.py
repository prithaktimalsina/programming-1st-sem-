import math
#quadratic equation
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
p1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
p2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print(p1)
print(p2)


#loan payment formula
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
e = (b/12) * (1 + b/12) ** c
f = (1 + b/12) ** c - 1
z = a * e * f
print(f)

#distance payment
x1 = float(input("x1: "))
x2 = float(input("x2: "))
y1 = float(input("y1: "))
y2 = float(input("y2: "))
z = math.sqrt((x2-x1)**2) + ((y2-y1)**2)
print(z)
