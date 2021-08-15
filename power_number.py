#!/usr/bin/env python3

# Elevar un numero a una potencia determinada, por ejemplo 5 elevado a la 4ta potencia.
# Utilizar una funcion iterativa, recursiva o ambas.

def power_number(number,exponent):
  error_message = "Ingresa un numero valido."
  if number is None:
    number = str(input("Ingresa base: "))
    if number.isnumeric():
      exponent = str(input("Ingresa exponente: "))
      if exponent.isnumeric():
        number = int(number)
        exponent = int(exponent)
      else:
        return error_message
    else:
      return error_message

  if exponent<=0:
    return 1
  if exponent%2 == 0:
    x = power_number(number, exponent/2)
    return x * x
  else:
    x = power_number(number, (exponent-1)/2)
    return x * x * number



dash = '-' * 72

print(dash)
print("Programa que permite elevar un numero a una potencia determinada.")
print("{} \n".format(dash))
print("El resultado es: {}".format(power_number(None, None)))
