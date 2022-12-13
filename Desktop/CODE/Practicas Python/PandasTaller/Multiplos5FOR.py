#bucle for, utilizamos esto para hace repeticiones
"1. ELABORA UN PROGRAMA QUE PEMRITA LEER 10 NÚMEROS, AL FINAL IMPRIMA CUNATOS NÚMEROS SON MÚLTIPLOS DE 5"
lista= []


for x in range(0,10):
    num=int(input("Dame un valor:"))
    if num%5==0:
        lista.append(num)
    #else:                                              NO NECESITAMOS ESTA LINEA PARA COMPLETAR EL EJERCICIO
    #    print(f"{num} No es multiplo de cinco")        NO NECESITAMOS ESTA LINEA PARA COMPLETAR EL EJERCICIO
#print(f"Tus numeros multiplos de cinco son: {lista}")  NO NECESITAMOS ESTA LINEA PARA COMPLETAR EL EJERCICIO
print("Hay",(len(lista)),"números multiplos de 5 en tu lista")

