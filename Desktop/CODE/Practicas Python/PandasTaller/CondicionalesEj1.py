''' Ejercicio 1:
Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son.'''
import math

numero1 = int(input("Dame tu primer numero: "))
if numero1%2==0:
        print(f"Tu numero {numero1} es par")
else:
        print(f"Tu numero {numero1} impar")

numero2 = int(input("Dame tu segundo numero: "))

if numero2%2==0:
    print(f"El segundo numero {numero2} es par")
else:
     print(f"Tu segundo numero es {numero2} impar")

if numero1%2==0 and numero2%2==0:
    print("Ambos son pares")
else:
    print("Ambos numeros son impar")


