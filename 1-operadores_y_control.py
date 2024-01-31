"""
Operadores
"""

# Operadores aritméticos
print(f"Suma: {10 + 3}")
print(f"Resta: {10 - 3}")
print(f"Multiplicación: {10 * 3}")
print(f"División: {10 / 3}")
print(f"Módulo: {10 % 3}")
print(f"Exponente: {10 ** 3}")
print(f"División entera: {10 // 3}")

# Operadores de comparación
print(f"Igualdad: {10 == 3}")
print(f"Desigualdad: {10 != 3}")
print(f"Mayor que: {10 > 3}")
print(f"Menor que: {10 < 3}")
print(f"Mayor o igual que: {10 >= 10}")
print(f"Menor o igual que: {10 <= 3}")

# Operadores lógicos
print(f"AND {4 == 13 and 4 == 4}")
print(f"OR {4 == 13 or 4 == 4}")
print(f"NOT {not 14 == 14}")

# Operadores de asignación
my_number = 11  # asignación
print(my_number)
my_number += 1  # suma y asignación
print(my_number)
my_number -= 1  # resta y asignación
print(my_number)
my_number *= 2  # multiplicación y asignación
print(my_number)
my_number /= 2  # división y asignación
print(my_number)
my_number %= 2  # módulo y asignación
print(my_number)
my_number **= 1  # exponente y asignación
print(my_number)
my_number //= 1  # división entera y asignación
print(my_number)

# Operadores de pertenencia
print('e' in 'Sergio')
print('b' not in 'Sergio')

# Condicionales
name = "Sergio"

if name == "Osmel":
    print("Mi nombre es 'Osmel'")
elif name == "Sergio":
    print("Mi nombre es 'Sergio'")
else:
    print("Mi nombre no es 'Osmel' ni 'Sergio'")

# Iterativas
list = ["manzana", "pera", "platano"]
for x in list:
    print(x)

for i in range(11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1
    
# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
    
"""
Extra
"""
for number in range(10, 55):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)