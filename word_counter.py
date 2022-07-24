
frases = input("ingrese una frase     ")

while frases != "the end":

    f = open ("frases.txt",'a')
    f.write(frases+'\n')
    frases = input ("ingrese una frase:    ")

cantidad_de_frases= len (frases)
cantidad_de_palabras =  (frases.split())


print ("la cantidad de frases es   " ,cantidad_de_frases)
print ("la cantidad de palabras es   ", len (cantidad_de_palabras))
