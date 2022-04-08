months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def number_to_month(month):
    if month > 12 or month < 0:
        return "Error, month number must be between 1 and 12."
    else:
        return months[month - 1]

print(number_to_month(0))
print(number_to_month(4))
