def fibo(n):
    lista=[]
    for i in range(0,n):
        if i==0 or i==1:
            lista.append(1)
        else:
            lista.append(lista[-2]+lista[-1])
    return lista
        
def lista_fibo(Lista):
    for i in lista:
        print(f"{i}")
            
numero = int(input("ingresa un numero: "))
if numero >0:
    lista= fibo(numero)
    lista_fibo(lista)
else:                 
    print("ingrese otro numero: ")
    