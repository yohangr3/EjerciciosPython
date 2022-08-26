# Escribir una función que reciba una muestra de números en una lista y devuelva 
# un diccionario con su media, varianza y desviación típica.

def cuadrados(n):
    nc= []

    for i in n:
        nc.append(i**2)
    return nc

def estadistica(n):

    estad={}
    estad["media"] = sum(n)/len(n)
    estad["varianza"] = sum(sqtr(n))/len(n)-estad['media']**2

print(estadistica([1, 2, 3, 4, 5]))
print(estadistica([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))