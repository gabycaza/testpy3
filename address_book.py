import random
import datetime
from csv import writer

nombre_apellido = str(input ("ingrese su nombre y apellido "))
direccion= input ("ingrese su dirección ")
telefono = int(input ("ingrese su número de teléfono "))

from random import random
id = []
for i in range(1):
    id.append(random())
print(f"el ID de {nombre_apellido} es {id}")

from datetime import date
fecha_registro = date.today().strftime('%d/%m/%y')

print("La fecha de registro es", fecha_registro)

libreta_direcciones = [nombre_apellido, direccion, telefono, id, fecha_registro]

with open('addresses.csv', 'a', newline='') as registro:
    csv_writer = writer(registro)
    csv_writer.writerow(libreta_direcciones)
