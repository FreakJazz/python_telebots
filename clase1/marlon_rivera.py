# ## 🧪 Ejercicio 1: Números primos

# Crea un programa que solicite al usuario un número `n` y muestre todos los números primos del 1 al `n`.

# ### 💡 Sugerencia:
# Usa una función `es_primo()` para verificar si un número es primo.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese un número entero positivo: "))

print(f"Números primos entre 1 y {n}:")
for num in range(1, n + 1):
    if es_primo(num):
        print(num, end=" ")


# ## 🧪 Ejercicio 2: Menú interactivo

# Crea un menú con al menos 3 opciones usando `if` y `elif`:

# - Mostrar una frase motivacional.
# - Mostrar la fecha actual.
# - Salir del programa.

import datetime

while True:
    print("MENÚ")
    print("1. Mostrar una frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir del programa")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        print("Eres capaz de TODO.")
    elif opcion == "2":
        fecha_actual = datetime.datetime.now()
        print("Fecha y hora actual:", fecha_actual.strftime("%Y-%m-%d %H:%M:%S"))
    elif opcion == "3":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")


