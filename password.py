import random
def mayuscula():
    lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    pos=random.randint(0,len(lista)-1)
    letra=lista[pos]
    return letra

def minuscula():
    letra=mayuscula()
    letra=letra.lower()
    return letra

def numero():
    numero=random.randint(0,10000)
    return numero

def simbolos():
    lista=['+','-','%','$','&','#']
    pos=random.randint(0,len(lista)-1)
    letra=lista[pos]
    return letra

def generador(numeros):
    contraseña=''
    for i in range(numeros):
        lista=[mayuscula(),minuscula(),numero(),simbolos()]
        pos=random.randrange(0,len(lista))
        contraseña+=str(lista[pos])
    return contraseña





cantidad=int(input("Ingrese cantidad de digitos de su contraseña: "))
print(generador(cantidad))