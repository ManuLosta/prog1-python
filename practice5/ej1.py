lastName = 'Longo'
name = 'Juan'
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

next_letter = abc[abc.index(lastName[0].upper()) + 1]
passwd = f"{lastName[:3]}{name[:3]}"


print(f"El apellido {lastName} comienza con una letra que esta antes de la {next_letter}")
print(f"La clave generada es: {passwd}")
