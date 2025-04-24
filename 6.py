"""
6) Crear una lista con números del 10 al 30 (incluído),
 haciendo saltos de 5 en 5 y mostrar por 
 pantalla los dos primeros. 
"""
#se crea la lista vacia
mi_lista = []

#se usa la funcion range para crear desde el 10 hasta el 31
#porque el 31 no se incluye que va de 5 en 5
mi_lista = list(range(10,31,5))

#mostramos por pantalla el primer y segundo subindice de la lista
print(f"{mi_lista[0]}, {mi_lista[1]}")