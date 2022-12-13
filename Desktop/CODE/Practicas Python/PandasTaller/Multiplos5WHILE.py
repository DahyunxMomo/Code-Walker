#bucle for, utilizamos esto para hace repeticiones
"1. ELABORA UN PROGRAMA QUE PEMRITA LEER 10 NÚMEROS, AL FINAL IMPRIMA CUNATOS NÚMEROS SON MÚLTIPLOS DE 5"
lista= []
x=0

while x < 10:
    num=int(input("Dame un valor:"))
    x+=1  #Esta linea va añadiendo +1 a x, como un contador. 
    if num%5==0:
        lista.append(num)
    #else:                                              NO NECESITAMOS ESTA LINEA PARA COMPLETAR EL EJERCICIO
    #    print(f"{num} No es multiplo de cinco")        NO NECESITAMOS ESTA LINEA PARA COMPLETAR EL EJERCICIO
#print(f"Tus numeros multiplos de cinco son: {lista}")  NO NECESITAMOS ESTA LINEA PARA COMPLETAR EL EJERCICIO

print("Hay",(len(lista)),"números multiplos de 5 en tu lista")
