import math

coefs = {"a": 0.0, "b": 0.0, "x1": 0.0, "x2": 0.0}

# Assign values to coefs
for i in coefs:
    coefs[i] = float(input(f"Ingrese el coeficiente {i.upper()}: "))

# Print coefs values
for i in coefs:
    print(f"El coeficiente {i.upper()} de su ecuación de la recta es: {coefs[i]}")

print(f"\nPara la siguiente ecuación:\nY = {coefs['a']}X + {coefs['b']}")

y1 = coefs["a"] * coefs["x1"] + coefs["b"]
y2 = coefs["a"] * coefs["x2"] + coefs["b"]

print(f"\nDados los siguiente puntos:\n\tP1 ({coefs['x1']}, {y1})\n\tP2 ({coefs['x2']}, {y2})")

distance = math.sqrt((coefs['x1'] - coefs['x2']) ** 2 + (y1 - y2)**2) 
print(f"La distancia entre ellos es: {distance}")
