#!/usr/bin/env python3

# Imprimir en pantalla la tabla de multiplicar del numero que ingrese el usuario hasta el 10.
# Debe utilizarse (for, while, o do while)


x = str(input("Ingresa un numero para mostrar su tabla de multiplicar: "))
dash = '-' * 42

if x.isnumeric():
  print("\n{}".format(dash))
  print("Tabla del {}: ".format(x))
  print("{} \n".format(dash))
  x = int(x)
  for i in range(1,11):
    print("{} * {} = {}".format(x, i, x * i))
else:
  print("Ingresa un numero valido.")
