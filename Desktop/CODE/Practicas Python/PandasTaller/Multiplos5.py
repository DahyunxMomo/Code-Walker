lista1=[]

num1=int(input("Añade tu primer valor: "))
if num1%5==0:
    print(f" '{num1}' Es multiplo de cinco")
    lista1.append(num1)
else:
    print(f"{num1} No es multiplo de cinco")

num2=int(input("Añade tu segundo valor: "))   
if num2%5==0:
    print(f" '{num2}' Es multiplo de cinco")
    lista1.append(num2)
else:
    print(f"{num2} No es multiplo de cinco")
    
num3=int(input("Añade tu tercer valor: "))
if num3%5==0:
    print(f" '{num3}' Es multiplo de cinco")
    lista1.append(num3)
else:
    print(f"{num3} No es multiplo de cinco")
num4=int(input("Añade tu cuarto valor: "))
if num4%5==0:
    print(f" '{num4}' Es multiplo de cinco")
    lista1.append(num4)
else:
    print(f"{num4} No es multiplo de cinco")    
num5=int(input("Añade tu quinto valor: "))
if num5%5==0:
    print(f" '{num5}' Es multiplo de cinco")
    lista1.append(num5)
else:
    print(f"{num5} No es multiplo de cinco")
num6=int(input("Añade tu sexto valor: "))
if num6%5==0:
    print(f" '{num6}' Es multiplo de cinco")
    lista1.append(num6)
else:
    print(f"{num6} No es multiplo de cinco")
num7=int(input("Añade tu septimo valor: "))
if num7%5==0:
    print(f" '{num7}' Es multiplo de cinco")
    lista1.append(num7)
else:
    print(f"{num7} No es multiplo de cinco")    

num8=int(input("Añade tu octavo valor: "))
if num8%5==0:
    print(f" '{num8}' Es multiplo de cinco")
    lista1.append(num8)
else:
    print(f"{num8} No es multiplo de cinco")

num9=int(input("Añade tu noveno valor: "))        
if num9%5==0:
    print(f" '{num9}' Es multiplo de cinco")
    lista1.append(num9)
else:
    print(f"{num9} No es multiplo de cinco")   

num10=int(input("Añade tu decimo valor: "))
if num10%5==0:
    print(f" '{num10}' Es multiplo de cinco")
    lista1.append(num10)
else:
    print(f"{num10} No es multiplo de cinco")    



print(f"Tus numeros multiplos de cinco son: {lista1}")
print("Hay",(len(lista1)),"números multiplos de 5 en tu lista")