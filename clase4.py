#while y for

n=10

while n>=0:
    if n==7:
        n-=1
        continue
    if n==3:
        break

    print(n)
    n-=1


temperaturas_list = [-2.1, -2.3, -1.3, 3.4, 6.9, 6.3, 4.1]
#si quiero recorrer el array
for temp in temperaturas_list:
    print(temp)

    if (temp>6):
        break
else:
    print("Finished!!")  #solo se ejecuta cunaod el bucle for se ejecuta correctamente

#si quiero recorrer varias veces
list(range(10))

for i in range(10):
    print(i)

# en tuplas

temperaturas_tuple = ( 
    [ "2023-02-15", -2.1 ],  
    [ "2023-02-16", -2.3 ], 
    [ "2023-02-17", -1.3 ], 
    [ "2023-02-18", 3.4 ],
    [ "2023-02-19", 6.9 ], 
    [ "2023-02-20", 6.3 ],
    [ "2023-02-21", 4.1 ],)


for fecha, temp in temperaturas_tupla:
    print (fecha,temp)

#en diccionarios
for key in temperaturas_dict:
        print(key)
        print(temperaturas_dict[key])

#es lo mismo que
for key, values in temperaturas.dict.items():
    print(key)
    print(values)


#bucles comprehension list/dicts
temp_fahr= [temperatura *1.8 + 32 for temperatura in temperaturas_list]

temperaturas_positivas = [temperatura for temperatura in temperaturas_list if temperatura>=0]

#en diccionarios (para crear nuevo diccionario)
temperaturas_positivas = { temperatura : temperatura * 1.8 + 32 for temperatura in temperaturas_list if temperatura>=0}




