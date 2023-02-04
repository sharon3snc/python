import math

letras= ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']

num_dni= input('Dime tu DNI\n')

if len(num_dni) ==8:
    num_dni= int(num_dni)
else:
    exit()

if num_dni <0 or num_dni >99999999:
    print('El dni es incorrecto')
    exit(1)

letra_dni= input('Dime la letra de tu DNI\n')

posicion= num_dni % 23
letra_calc=letras[posicion]

if letra_calc== letra_dni:
    print('Todo correcto')
else:
    print('la letra del Dni es incorrecta')


