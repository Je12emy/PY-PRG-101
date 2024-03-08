def suma(a,b):
    resultado = a + b
    return resultado

def resta(a,b):
    resultado = a - b
    return resultado

def multiplicacion(a,b):
    resultado = a * b
    return resultado

def division(a,b):
    resultado = a / b
    return resultado

def imprimir_menu():
    print("MENU PRINCIPAL")
    print("1. Sumar.")   
    print("2. Restar.")   
    print("3. Multiplicar.")   
    print("4. Dividir.")   
    print("5. Salir")   

correr_programa = True

while correr_programa == True:
    imprimir_menu()

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese un número: "))
        resultado_suma = suma(a, b)
        print("El resultado es: ", str(resultado_suma))
    elif opcion == 2:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese un número: "))
        resultado_resta = resta(a, b)
        print("El resultado es: ", str(resultado_resta))
    elif opcion == 3:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese un número: "))
        resultado_multiplicacion = multiplicacion(a, b)
        print("El resultado es: ", str(resultado_multiplicacion))
    elif opcion == 4:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese un número: "))
        resultado_division = division(a, b)
        print("El resultado es: ", str(resultado_division))
    elif opcion == 5:
        correr_programa = False
    else:
        print("Esa no es una opción")

print("FIN DEL PROGRAMA")
