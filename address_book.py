nombre_apellido = input ("ingrese su nombre y apellido ")
direccion= input ("ingrese su dirección ")
telefono = input ("ingrese su número de teléfono ")

from random import random
id = []
for i in range(1):
    id.append(random())
print(f"el ID de {nombre_apellido} es {id}")

from datetime import date
fecha_registro = date.today()

print("La fecha de registro es", fecha_registro)

libreta_direcciones = [nombre_apellido, direccion, telefono, id, fecha_registro]

import csv

with open('adresses.csv', 'w') as csvfile:
    fieldnames = [nombre_apellido, direccion, telefono, id, fecha_registro]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader
    writer.writerow({'nombre_apellido',
                     'direccion',
                     'telefono',
                     'id',
                     'fecha_registro'})

print ("datos insertados")
