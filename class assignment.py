import math
#quadratic equation
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print(x1)
print(x2)