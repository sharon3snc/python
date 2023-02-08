#TERNARIOS

security_level= 3
access_level= 4
access = False #este false es opcional

if access_level > security_level:
    acess= 'adelante'
else:
    access= 'no puedes pasar'

#es lo mismo que 
access= print('adelante') if access_level > security_level else print('no puedes pasar')

#STRINGS
full_name='Alvaro Sanchez Perez'
name= 'alvaro'

full_name [0]
len(full_name)
full_name[-1]   #ultimo caracter -1
full_name[0:6]  #caracteres del primero al 6to
full_name[::] #todos los caracteres
full_name[::2] #va de 2 en 2

full_name.split #separa el nombre por espacios
full_name.replace #reempplazar ('anterior','nueva')

mensaje= 'lalala'
if len(mensaje) >= 50: print(mensaje[50])
#si solo imprimo mensaje y no tiene elemento 50, daria error, con este if ya no da error
#una vez que defino una variable, no me deja cambiar los componentes, hay que definir toda la variable nuevamente
#o puedes jugar con los arrays para concatenar

mensaje.upper() #pasa las letras a mayusculas
mensaje.lower() #pasa las letras a minuscula
mensaje.capitalize() #1ra mayuscula, siguientes minusculas

dir(mensaje) #te saca el listado de cosas y metodos que tiene esa variable

"alvaro sanchez, {} años, {} altura". format(25,172)

age=25
altura=172
f"alvaro sanchez, {age} años, {altura} altura"

name='alvaro'
name in full_name

#LISTAS
datos_l=['alvaro sanchez', '25', [60,'kg'], [172,'cm'] ]
datos_l[2:4]

datos_l[-1]= 'guapo'

datos_l[3][0]

datos_l.pop() #elimina la ultima posicion
del(datos_l[0]) #elimina la primera posicion

datos_l.append('guapa') #agrega dato al final
datos_l.insert(0, 'sharon') #agrega dato en 1ra posicion

#TUPLAS parecido a las listas, pero no deja modificar uno de los elementos
#se tiene que crear una nueva tupla
#sirve para asignar variables facilmente
datos_t= ('alvaro sanchez', '25', [60,'kg'], [172,'cm'])

datos_t.index(25)  #saber si existe un 25 en la lista (encontrar elementos)
25 in datos_l #preguntar si algo esta en una lista

(name, edad, peso, altura) = datos_l  #de esta forma se asignan variables a la tupla

#DICCIONARIOS
#permiten modificar el interior y gestion de datos
#tarda menos en coger datos
datos_d = {
    'name':'alvaro sanchez',
    'age': 25,
    'weight' : 60
}

#ALIASING
a=5
b=a
a=7 #en este caso no se modifica b, es una copia de lo que antes era a

a=[5,10]
b=a
a.append(15)
#si es un elemento complejo no se crea una copia, sino que replica siempre el valor de a
#cuando es una lista, tupla o diccionario

b=a[]  #si hago esto, si se hace una copia



#ejercicio vavacars

lineas.texto.split("\n")
marca, modelo= lineas[0].upper().split(" ")
year, km, transmision, combustible, matricula= lineas[2].split("|")
#en el split se pone lo que separa los elementos
km= int(km.split(' ')[0].replace(".", ""))

coche: {
    "marca": marca.
    "modelo":modelo
}

print(coche)


