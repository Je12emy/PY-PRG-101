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

numero = 55
adivinanza = int(input("Intentar adivinar un numero: "))

if (adivinanza == numero):
  print("Felicidades.")
elif (adivinanza < numero):
  print("Es mayor.")
else:
  print("Es menor")
