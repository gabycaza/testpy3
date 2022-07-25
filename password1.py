import random

mayusculas = ["A","B", "C", "D","E", "F", "G"]
minusculas = ["a", "b", "c", "d", "e","f", "g"]
numeros = ["1", "2", "3", "4", "5", "6", "7"]
simbolos = [ "+", "-", "*", "%", "$", "#"]

quiere_mayusculas = input ("quiere mayusculas en su contaseña? (S/N  ")
quiere_minusculas = input ("quiere minusculas en su contaseña? (S/N  ")
quiere_numeros = input ("quiere numeros en su contaseña? (S/N  ")
quiere_simbolos = input ("quiere simbolos en su contaseña? (S/N  ")

cantidad = int (input( "cual es la longitud que desea en su contaseña?  "))

lista_de_caracteres = [ ]

if quiere_mayusculas == "S":
    lista_de_caracteres = lista_de_caracteres + mayusculas
if quiere_minusculas == "S":
    lista_de_caracteres = lista_de_caracteres + minusculas 
if quiere_numeros == "S":
    lista_de_caracteres = lista_de_caracteres + numeros
if quiere_simbolos == "S":
    lista_de_caracteres = lista_de_caracteres + simbolos    

def get_random_password():
    random_source = mayusculas + minusculas +numeros + simbolos
    
    password_list = list(lista_de_caracteres)
    random.SystemRandom().shuffle(lista_de_caracteres)
    password = ''.join(lista_de_caracteres)
    return password
    
print("la contraseña es    " , get_random_password())

