"""
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
 Utilizar la función range.
"""

#se crea la lista comenzando del 4 hasta 100 con paso 4
mi_lista = list(range(4,101,4))

#iteramos sobre la lista con los numeros multiplos de 4
for i in mi_lista:
    print(i)