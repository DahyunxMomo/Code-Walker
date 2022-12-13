#While

num = int (input("Escribe un número positivo:"))
while num < 0: 
    print("Este es un número negativo, intenta de nuevo")
    num = int (input("Escribe un número positivo:"))
print("El numero es: ", num)