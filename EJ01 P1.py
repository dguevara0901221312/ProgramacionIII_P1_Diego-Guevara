## VARIANTE B
## DIEGO GUEVARA 0901-22-1312
##1. Escribe una función en Python que reciba una lista como parámetro y devuelva la suma de todos los elementos de la lista. 

print("1. PROGRAMA PARA LA SUMA DE ELEMENTOS DE UNA LISTA.\n")

def lista_suma(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

lista1 = [10, 20, 30, 40, 50]
resultado = lista_suma(lista1)

print(f"La suma de esta lista es: {resultado}.")




