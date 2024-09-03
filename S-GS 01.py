# OPERADORES BÁSICOS


# Operadores aritméticos
print (" ")
print ("- Operadores aritméticos")
print (" ")
## Suma
print (f"Suma: 1 + 2 = {1 + 2}")
sum = 1 + 3
print (f"1 + 3 = {sum}")
## Resta
print (f"Resta: 2 - 1 = {2 - 1}")
## Multiplicación
print (f"Multiplicación: 2 * 2 = {2 *2 }")
## División
print (f"División: 4 / 2 = {4 / 2}")
## Módulo
print (f"Módulo: 25 % 4 = {25 % 4}")
## Potencia
print (f"Potencia: 4 ** 2 = {4 ** 2}")
## División entera
print (f"Dvisión entera: 10 // 3 = {10 // 3}")
print (" ")


# Operadores de comparación
print ("- Operadores de comparación")
print (" ")
## Mayor que
print (f"Mayor que: 3 > 2 = {3 > 2}")
## Menor que
print (f"Menor que: 2 < 3 = {2 < 3}")
## Igual que
print (f"Igual que: 2 = 2 = {2 == 2}")
## Mayor o igual que
print (f"Mayor o igual que: 2 >= 2 = {2 >= 2}")
## Menor o igual que
print (f"Menor o igual que: 2 <= 3 = {2 <= 3}")
##Diferente de
print (f"Diferente de: 2 != 3 = {2 != 3}")
print (" ")


# Operadores de Lógicos
print ("- Operadores de Lógicos")
print (" ")
## AND
print (f"AND &&: 10 > 3 and 5 < 7 is {10 > 3 and 5 < 7} ")
## OR
print (f"OR ||: 10 > 3 or 5 < 7 is {10 > 3 or 5 < 7} ")
# NOT
print (f"NOT !: not 5 > 7 is {not 5 > 7} ")
print (" ")


# Operadores de Asignación
print (" ")
print ("- Operadores de Asignación")
#Asignación
my_number = 11
print (f"Asignación: my_number = {my_number}")
#Suma y asignación
my_number += 1
print (f"Suma y asignación: my_number += 1 = {my_number}")
#Resta y asignación
my_number -= 2
print (f"Resta y asignación: my_number -= 2 = {my_number}")
#Producto y asignación
my_number *= 3
print (f"Producto y asignación: my_number *= 3 = {my_number}")
#División y asignación
my_number /= 2
print (f"División y asignación: my_number /= 2 = {my_number}")
print (" ")


# Operadores de Identidad
print (" ")
print ("- Operadores de Identidad")
## Misma posición de memoria
my_number1 = my_number
print (f"Misma posición de memoria: my_number1 is my_number is {my_number1 is my_number}")
## Distinta posición de memoria
print (f"Distinta posición de memoria: my_number1 is not my_number is {my_number1 is not my_number}")
print (" ")


# Operadores de Pertenencia
print (" ")
print ("- Operadores de Pertenencia")
## Pertenencia a
print (f"Pertenece a: 'v' in 'salva' is {'v' in 'salva'}")
print (f"Pertenece a: 'e' in 'salva' is {'e' in 'salva'}")
## No pertenencia a
print (f"No pertenece a: 'x' not in 'salva' is {'x' not in 'salva'}")
print (f"No pertenece a: 'l' not in 'salva' is {'l' not in 'salva'}")
print (" ")


# Operadores de Bit
print (" ")
print ("- Operadores de Bit")
a = 10 # 1010
b = 3 # 0011
##AND & (Comparación bit a bit. Si los dos bit son 1 = 1, si alguno es diferente de 1 = 0)
print (f"AND: 10 & 3 = {10 & 3}") # 10 & 3 = 2 -> 1010 & 0011 = 0010
##OR | (Comparación bit a bit. Si uno de los dos bit es 1 = 1, si los dos son diferentes de 1 = 0)
print (f"OR: 10 | 3 = {10 | 3}") # 10 | 3 = 11 -> 1010 | 0011 = 1011
##XOR | (Comparación bit a bit. Si los dos bits son iguales = 0, si los bits son diferentes = 1)
print (f"XOR: 10 ^ 3 = {10 ^ 3}") # 10 ^ 3 = 9 -> 1010 ^ 0011 = 1001
##NOT | (Cambia 0 por 1 )
print (f"NOT: ~ 10 = {~ 10 }") # ~10 = -11  -> 1010 =

## YT 1:02:41

