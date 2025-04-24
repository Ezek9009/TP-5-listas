"""
5) Analizar el siguiente programa
y explicar con tus palabras qué es lo que realiza.
"""

#en el siguiente codigo se crea la lista numeros
numeros = [8, 15, 3, 22, 7]

#la funcion .remove(max(numeros)) elimina el numero mas grande 
#dentro de la lista
numeros.remove(max(numeros))

#y se muestra en pantalla sin el numero 22
print(numeros)