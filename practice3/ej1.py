import math

# Create a dictionary with the coefficients of the equation
coefs = {"a": 0.0, "b": 0.0, "x1": 0.0, "x2": 0.0}

# Assign values to coefficients
for key in coefs:
    coefs[key] = float(input(f"Ingrese el coeficiente {key.upper()}: "))

# Print coefficients values
for key in coefs:
    print(f"El coeficiente {key.upper()} de su ecuación de la recta es: {coefs[key]}")

# Print equation
print(f"\nPara la siguiente ecuación:\nY = {coefs['a']}X + {coefs['b']}")

# Calculate y1 and y2
y1 = coefs["a"] * coefs["x1"] + coefs["b"]
y2 = coefs["a"] * coefs["x2"] + coefs["b"]

# Print both points
print(f"\nDados los siguiente puntos:\n\tP1 ({coefs['x1']}, {y1})\n\tP2 ({coefs['x2']}, {y2})")

# Calculate the distance between the points and print it
distance = math.sqrt((coefs["x1"] - coefs["x2"]) ** 2 + (y1 - y2) ** 2)
print(f"La distancia entre ellos es: {distance}")
