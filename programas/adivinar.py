# Adivinanza, el usuario va a intentar adivinar un numero
# Si el numero es igual al numero ganador, imprime un mensaje felicitandolo.
# Si el numero es menor al numero ganador, imprimi un mensaje indicando que es menor.
# Si el numero es mayor al numero ganador, imprime un mensaje indicando que es mayor.
# Ejemplo:
# adivinanza 5
# ganador 7.
# Tu número es menor al ganador.
# 9
# Tu número es mayor al ganador.

# <Break>
# Ahora pidele al usuario que ingrese cuantos intentos quiere
# Mientras que tenga intentos, preguntarle la advinanza
# Si el numero es igual al numero ganador, imprime un mensaje felicitandolo.
# Si el numero es menor al numero ganador, imprimi un mensaje indicando que es menor.
# Si el numero es mayor al numero ganador, imprime un mensaje indicando que es mayor.
# Ejemplo:
# > Ingrese cuantos intentos quiere:
# < 4
# > Adivina un número:
# < 3
# > El número ganador es mayor.
# > Adivina un número:
# < 10
# > El número ganador es menor.
# > Adivina un número:
# < 7
# > ¡Felicidades! Has ganado
numero_ganador = 42
intentos = int(input("Ingresa los intententos que quieras: "))
i = 0
while i < intentos:    
  adivinanza = int(input("Intentar adivinar un numero: "))
  i = i + 1
  if adivinanza == numero_ganador:
      print("Felicidades.")
      break
  elif adivinanza < numero_ganador:
      print("Es mayor.")
  else:
      print("Es menor.")
