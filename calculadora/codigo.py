# Funciones de operaciones matemáticas
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir entre cero"

# Función principal para la calculadora
def calculadora():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Recibe la elección del usuario
    seleccion = input("Ingresa el número de la operación (1/2/3/4): ")

    if seleccion in ('1', '2', '3', '4'):
        # Solicita los números al usuario
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar números válidos.")
            return

        # Realiza la operación según la elección
        if seleccion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif seleccion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif seleccion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif seleccion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Selección no válida. Por favor, elige una opción entre 1 y 4.")