def es_primo(num):
    """Devuelve True si num es un número primo, False en caso contrario."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mostrar_primos_hasta(n):
    """Muestra todos los números primos desde 1 hasta n."""
    print(f"Números primos entre 1 y {n}:")
    for i in range(1, n + 1):
        if es_primo(i):
            print(i, end=' - ')
    print()  # Salto de línea final

# Programa principal
try:
    n = int(input("Introduce un número entero positivo: "))
    if n < 1:
        print("Por favor, introduce un número mayor o igual a 1.")
    else:
        mostrar_primos_hasta(n)
except ValueError:
    print("Entrada inválida. Debes ingresar un número entero.")

import datetime
import random

# Lista de frases motivacionales
frases = [
    "🌟 Cree en ti y todo será posible.",
    "🚀 Cada día es una nueva oportunidad para mejorar.",
    "💪 El esfuerzo de hoy es el éxito de mañana.",
    "🔥 No te detengas hasta estar orgulloso.",
    "🌈 Si puedes soñarlo, puedes lograrlo.",
    "🧠 La mente es poderosa. Llénala de pensamientos positivos.",
    "🌱 El crecimiento comienza al salir de tu zona de confort.",
    "⏳ El tiempo es ahora. ¡Aprovecha el momento!",
    "🛠️ Cada error es una oportunidad para aprender.",
    "🏆 La perseverancia es la clave del triunfo."
]

def mostrar_menu():
    print("\n=== MENÚ INTERACTIVO ===")
    print("1. Mostrar una frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        frase = random.choice(frases)
        print(f"\n{frase}")
    elif opcion == "2":
        fecha_actual = datetime.datetime.now()
        print(f"\n📅 Fecha actual: {fecha_actual.strftime('%d/%m/%Y - %H:%M:%S')}")
    elif opcion == "3":
        print("\n👋 ¡Hasta luego!")
        break
    else:
        print("\n❌ Opción no válida. Intenta de nuevo.")
