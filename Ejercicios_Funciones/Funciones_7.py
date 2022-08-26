# Escribir una función que reciba una muestra de números en una lista y devuelva otra
#  lista con sus cuadrados.


def cuadrados(n):
    nc= []

    for i in n:
        nc.append(i**2)
    return nc

print(cuadrados([1,2,3,4,5]))

