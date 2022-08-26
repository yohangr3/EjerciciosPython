# Escribir una función que calcule el área de un círculo y otra que calcule el volumen
# de un cilindro usando la primera función.

from cmath import pi


def areacirculo(r):

    return pi* r**2

print(areacirculo(5))

def volumendelcilindro(r,h):

    return pi*(r**2)*h
print(volumendelcilindro(5,10))
