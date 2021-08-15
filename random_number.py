#!/usr/bin/env python3
from random import seed
from random import randint
import secrets
# Generar un numero al azar entre 1 y 100
# El usuario tiene 5 intentos para adivinar
# Dar pistas al usuario, ejemplo:
# Si el numero ingresado es menor al generado al azar, mostrar mensaje que diga "Mas arriba"
# Si el numero ingresado es mayor al generado al azar, mostrar mensaje que diga "Mas abajo"


def random_number(x, v, count):

  error_messsage = "Ingresa un numero valido."
  input_message = "Ingresa un numero: "
  success_message = "Felicidades!!! Adivinaste el numero."

  if x is None:
    count = 1
    seed(secrets.token_hex(64))
    v = randint(0,100)
    x = str(input(input_message))
    if x.isnumeric():
      x = int(x)
    else:
      print(error_message)
      return

  if count < 5:
    if x == v:
      print(success_message)
      return
    elif x > v:
      print("Mas abajo. ")
      x = str(input(input_message))
      if x.isnumeric():
        random_number(int(x), v, count + 1)
      else:
        print(error_message)
        return
    elif x < v:
      print("Mas arriba. ")
      x = str(input(input_message))
      if x.isnumeric():
        random_number(int(x), v, count + 1)
      else:
        print(error_message)
        return
  else:
    print("Perdiste, superaste el limite maximo de intentos (5), el valor a adivinar es: {} ".format(v))


dash = '-' * 62

print(dash)
print("Intenta adivinar el numero aleatorio generado por el CPU")
print("Tienes 5 intentos, Suerte!!!")
print("{} \n".format(dash))
random_number(None, None, None)
