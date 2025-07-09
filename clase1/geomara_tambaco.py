"""
Ejercicio 1: Números primos
Crea un programa que solicite al usuario un número `n` y muestre todos los números primos del 1 al `n`.
Sugerencia:
Usa una función `es_primo()` para verificar si un número es primo.
Concepto Número Primo.- Un número es primo cuando es divisible para si mismo y para la unidad.

"""

#Función para determinar si un número es primo

def esPrimo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Bucle para validar entrada correcta
while True:
    entrada = input("Ingresa un número entero positivo mayor o igual a 2: ")
    if entrada.isdigit():  # Verifica que solo tenga dígitos (no negativos ni decimales)
        n = int(entrada)
        if n >= 2:
            break
        else:
            print("El número debe ser mayor o igual a 2.")
    else:
        print("Entrada inválida. Por favor ingresa solo números enteros positivos.")

print(f"Números primos hasta {n}:")

for num in range(2, n + 1):
    if esPrimo(num):
        print(num)


"""
Ejercicio 2: Menú interactivo
Crea un menú con al menos 3 opciones usando `if` y `elif`:
- Mostrar una frase motivacional.
- Mostrar la fecha actual.
- Salir del programa.
"""

#Importamos el módulo datetime para poder obtener la fecha y hora actual.
import datetime

while True:
    print("\n--- Menú interactivo ---")
    print("1. Mostrar frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        print("A sonreir que la función debe continuar.")
    elif opcion == "2":
        fecha_actual = datetime.datetime.now()
        print("Fecha y hora actual:", fecha_actual.strftime("%d/%m/%Y %H:%M:%S"))
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
