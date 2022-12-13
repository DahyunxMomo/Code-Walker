num1=()
#num1=int(input("Dame un número: "))

#match num1:
#    case num1 if num1 > 200: print(num1,"Es un numero mayor a 200")
#    case num1 if num1 == 200: print(num1,"Es un número igual a 200")
#    case num1 if num1 < 200: print(num1, "es un número menor a 200")
#    case _: print("Error") 





#while num!= 0:
#    x=0
#    print("Menu: 1 (Ver numeros), 0 (Salir)")
#    num=int(input("Opción:"))
#    while x < 10:
#        print(x)
#        x += 1
#print("Saliendo...")
#print("Gracias")



print("Elije una de las siguientes opciones: 1(Ver menu), 0(Salir)")
num1=int(input("Opción:"))

match num1: 
    case num1 if num1 == 1: print(num1, "1, hamburguesa. 2, taco")
        
    case num1 if num1 == 0: print(num1,"Haz elegido salir, adios.")
    

