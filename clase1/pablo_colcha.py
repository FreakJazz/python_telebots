
"""## 🧪 Ejercicio 1: Números primos

Crea un programa que solicite al usuario un número `n` y muestre todos los números primos del 1 al `n`.

### 💡 Sugerencia:
Usa una función `es_primo()` para verificar si un número es primo."""

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        print(f"{num} no es primo (menor que 2)")
        return False
    for i in range(2, int(num**0.5) + 1):  # Solo hasta la raíz cuadrada
        if num % i == 0:
            print(f"{num} no es primo (divisible por {i})")
            return False   
    return True

# Solicitar al usuario el valor de n
n = int(input("Ingrese un número entero positivo: "))

print(f"Números primos entre 1 y {n}:")

# Imprimir los números primos desde 1 hasta n
for i in range(1, n + 1):
    if es_primo(i):
        print(f" {i} es primo")
        
"""## 🧪 Ejercicio 2: Menú interactivo

Crea un menú con al menos 3 opciones usando `if` y `elif`:

- Mostrar una frase motivacional.
- Mostrar la fecha actual.
- Salir del programa. """ 

import datetime

while True:
    print("\n--- MENÚ INTERACTIVO ---")
    print("1. Mostrar una frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir del programa")

    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        print("Nunca te rindas. ¡Los grandes logros requieren tiempo y esfuerzo!")
    elif opcion == "2":
        fecha_actual = datetime.datetime.now()
        print(f" La fecha y hora actual es: {fecha_actual.strftime('%d/%m/%Y %H:%M:%S')}")
    elif opcion == "3":
        print(" ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

print("Fin del programa.")
