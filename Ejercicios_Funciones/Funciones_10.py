def decimal_binario(decimal):

    binario = ""
    
    while decimal > 0:
        
        residuo = int(decimal % 2)
        
        decimal = int(decimal / 2)
        
        binario = str(residuo) + binario
    return binario


decimal = int(input("Ingresa un número decimal: "))
binario = decimal_binario(decimal)
print(f"El número {decimal} es {binario} en binario")

    

    

