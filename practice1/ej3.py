gasto = float(input("Ingresar gasto: \n"))
pago = float(input("Dinero recibido: \n"))
vuelto = pago - gasto
centavos = int(((pago - gasto) - int(vuelto)) * 100)

print("\nVuelto")
print("\nPesos:\n" + str(vuelto))
print("Centavos:\n" + str(centavos))
