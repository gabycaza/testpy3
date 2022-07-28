contador_de_frases = 0
palabras_totales = 0

frase= input ("ingrese una frase: ")

cantidad_de_palabras = frase.count (' ')+1
contador_de_frases = contador_de_frases +1
print (f"la frase tiene   ", cantidad_de_palabras, "palabras")
print (f"la cantidad de frase es   ", contador_de_frases)

f = open ("frases.txt",'a')
f.write(frase+'\n')

while frase != "the end":
    frase = input ("ingrese una frase: ")
    
    cantidad_de_palabras = frase.count (' ')+1
    contador_de_frases = ( contador_de_frases)+1
    
    print (f"la cantidad de palabras son   ", cantidad_de_palabras, "palabras")
    print (f"la cantidad de frases total es  " , contador_de_frases)

palabras_total = (palabras_totales+cantidad_de_palabras )

print (f"la cantidad de palabras totales son  ", cantidad_de_palabras , "palabras")
print (f"la cantidad de frases totales son   ",  contador_de_frases, "frases")
