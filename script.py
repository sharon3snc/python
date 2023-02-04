#para usar funciones de math hay que importarlo primero
import math #para redondear math.floor()
import json


#def es lo mismo que funcion
def suma(num1, num2): 
    result= num1 + num2
    return result

print(math.floor(20.3))

num1= input("Dame un numero\n")
num1=int(num1)
num2= input("Dame otro numero\n")
num2=int(num2)
r1=suma(num1,num2)
print(r1)





