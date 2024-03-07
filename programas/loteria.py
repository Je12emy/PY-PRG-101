# Te han contratado para crear un sistema para verificar si un usuario ha ganado un tiquete
# de loteria. Aca, el usuario *ingresa su numero de tiquete* y el sistema le muestra un mensaje
# si ga ganado.

# Sintaxis para declarar una variable
# <nombre> = <valor>
# numero = 10
# Tiquete

# Yo tengo el tiquete 200
tiquete = int(input("Ingrese su número de tiquete: "))
# El tiquete ganador es el 25
ganador = 25

# = asignación
# == igualdad
# Si mi tiquete tiene el valor de ganador
if (tiquete == ganador):
  # Gane
  print("ganaste")
else:
  # Perdi
  print("¡perdiste!")
