palabras_ingresadas =0 
palindromos = 0
no_palindromos= 0
palabra = 0
while palabra!= "aloha" and palabra !="bye":
    palabra= input("Ingrese una palabra: ")    
    if(palabra) ==(palabra)[::-1]:
        print("es palindromo")
        palindromos +=1
        palabras_ingresadas +=1
    else: 
        print("No es palindromo")
        palabras_ingresadas +=1
        no_palindromos +=1
else:
    print("fin del programa")
    
print("total de palabras fue: ",palabras_ingresadas)
print("total de palindromos fue: ",palindromos)
print("total de palabras no palindromos fue: ",no_palindromos)   
          