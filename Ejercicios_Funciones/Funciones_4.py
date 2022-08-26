# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA
# , deberá aplicar un 21%.

def factura(total,iva=0.21):

    totalf = (total*iva) + total
    print (totalf)

factura(20000,0.21)
factura(20000,0.15)


