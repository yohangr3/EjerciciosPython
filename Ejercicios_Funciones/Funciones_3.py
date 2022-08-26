# Escribir una función que reciba un número entero positivo y devuelva su factorial.



def factorial(n):
    fact = 1
    for i in range(1,n+1): 
        fact = fact * i 
      
    print ("El factorial de " + str(n) + " es : " + str(fact))

factorial(int(input("Digite un número : ")))