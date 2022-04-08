import math

a = -3
b = 7
c = 4

def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0 or a == 0:
        return "()"
    elif discriminant == 0:
        r = -b / (2 * a)
        return f"(r = {r})"
    else:
        r1 = (-b - math.sqrt(discriminant)) / (2 * a)
        r2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return f"r1 = {r1}, r2 = {r2})"

def valueY(a, b, c, x):
    return a * x ** 2 + b * x + c

def toString(a, b, c):
    return f"y = {a}X² + {b}X + {c}"

def derivation(a, b):
    return f"y' = {2 * a}X + {b}"


print(roots(a, b, c))
print(valueY(a, b, c, 20))
print(toString(a, b, c))
print(derivation(a, b))
