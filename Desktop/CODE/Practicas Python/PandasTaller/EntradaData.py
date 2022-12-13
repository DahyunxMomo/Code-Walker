nombre = input("Digite su nombre: ") #Input guarda datos de tipo cadena

print(f"Hola {nombre}")

numero = int(input("Digite su edad: "))
print(f"su numero es {numero}")
if numero>=18:
    print("Eres mayor de edad")
    numerofloat = float(input("Digite su estatura: "))
    print(f"su numero es: {numerofloat}")
    print(f"Hola {nombre} Tu edad es:{numero} Y mides {numerofloat}m") 

elif numero==0:
    print("No puedes tener esa edad")
elif numero<0:
    print("No puedes tener esa edad")

else:
    print("Eres menor de edad")




