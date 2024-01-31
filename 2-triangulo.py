print("Hacemos un triangulo")
fila = int(input("Ingrese número filas quieres formar: "))

i = 1
for i in range(fila):
    print(' ' * (fila - i), "*" * (2 * i + 1))
    