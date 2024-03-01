## VARIANTE B
## DIEGO GUEVARA 0901-22-1312
##Define una función llamada "inverso_palabra" que reciba una cadena como parámetro y devuelva la cadena invertida. 
##Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp"


print("2. PROGRAMA QUE DEVUELVE LA CADENA INVERTIDA.\n")
def inverso_palabra(cadena):
    return cadena[::-1]

cadena_1 = "Programación III"
resultado = inverso_palabra(cadena_1)

print(f"El inverso de la palabra es: {resultado}.")

