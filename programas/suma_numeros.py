limite = int(input("Ingrese un limite: "))

# Acumulador
i = 0
# Otro acumulador
suma = 0

# limite = 4
# i = 4
# suma = 10
while i < limite:
    # numero = 2
    numero = int(input("Ingrese un número: "))
    suma = suma + numero
    i = i + 1

print("La suma es: " + str(suma))
