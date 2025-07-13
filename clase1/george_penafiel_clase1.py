## 🧪 Ejercicio 1: Números primos

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

n = int(input("Ejercicio 1\nIngresa un número para ver todos los primos del 1 al n: "))

print(f"\nNúmeros primos del 1 al {n}:")
for i in range(1, n + 1):
    if es_primo(i):
        print(i, end=" ")

print("\n")

import datetime

## 🧪 Ejercicio 2: Menú interactivo

while True:
    print("\n----- MENÚ -----")
    print("1. Mostrar una frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir del programa")

    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        print("¡Tú puedes lograrlo, no te rindas nunca!")
    elif opcion == "2":
        fecha_actual = datetime.datetime.now()
        print("La fecha y hora actual es:", fecha_actual)
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")

