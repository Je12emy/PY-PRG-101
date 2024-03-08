import datetime

def registrar_edad(age):
    print("Su edad es: " + str(age))
    if age > 17:
        print("Usted es mayor de edad.")
    else:
        print("Usted es menor de edad.")
    print("Solviendo al menu principal.\n")

def show_main_menu():
    print("MENU PRINCIPAL")
    print("1. Registrar edad.")
    print("2. Registrar.")
    print("3. Registrar.")
    print("3. Registrar.")
    print("5. Salir.")

while True:

    year = int(input("Ingrese su año de nacimiento (ej. 1998): "))
    # NOTE: Este código fue escrito en el 2024
    # Calcular el año actual con la libreria datetime
    # de esta manera el programa funcionara independientemente de cuando se ejecuta
    # por ejemplo, si uso 2024, la edad no se calculara correctamente si ejecuto
    # el programa ene l 2025.
    current_date = datetime.datetime.now()
    age = current_date.year - year

    first_digit = int(inpur("Ingrese el primer digito de su cédula: "))

    show_main_menu()
    option = int(input("Ingrese una opcion"))

    if option == 1:
        registrar_edad()
    elif option = 2:
    elif option = 5:
        confirm = input("¿Seguro que quiere terminar con el programa? Presione [s] para confirmar: ")
        if confirm == "y":
            break:


