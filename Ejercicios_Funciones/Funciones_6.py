# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

n = [1,2,3,4,5,6,10,20]
suma = 0
for i in n:
    suma = suma + i
    media = suma/len(n)
print(suma)
print(media)