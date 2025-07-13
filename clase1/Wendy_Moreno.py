## 🧪 Ejercicio 1: Números primos
# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Solicita al usuario un número
n = int(input("Ingresa un número: "))

# Verifica si el número ingresado es primo
if es_primo(n):
    print(f"✅ El número {n} es primo.")
    
    # Lista para guardar los números primos del 1 al n
    primos = []
    for i in range(1, n + 1):
        if es_primo(i):
            primos.append(i)

    # Muestra la lista de números primos
    print(f"Números primos del 1 al {n}:")
    print(primos)
else:
    print(f"❌ El número {n} NO es primo.")


## 🧪 Ejercicio 2: Menu interactivo
import random
from datetime import datetime

# Lista con 10 frases motivacionales
frases = [
    "✨ Cree en ti y todo será posible.",
    "💪 Nunca te rindas, los grandes logros toman tiempo.",
    "🚀 El éxito es la suma de pequeños esfuerzos repetidos cada día.",
    "🌟 Hoy es un buen día para empezar algo nuevo.",
    "🔥 Si puedes soñarlo, puedes lograrlo.",
    "🌱 Cada paso te acerca a tu meta.",
    "💫 El límite es el cielo, y tú tienes alas.",
    "🏆 El fracaso es solo una oportunidad para comenzar de nuevo con más inteligencia.",
    "📈 Sigue adelante, lo mejor aún está por venir.",
    "🎯 La disciplina tarde o temprano vence al talento."
]

# Menú interactivo
while True:
    print("\n📋 MENÚ INTERACTIVO:")
    print("1. Mostrar una frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        indice = random.randint(0, len(frases) - 1)
        print("\n🧠 Frase motivacional:")
        print(frases[indice])
    elif opcion == "2":
        ahora = datetime.now()
        print("\n📅 Fecha actual:")
        print(ahora.strftime("%d/%m/%Y - %H:%M:%S"))
    elif opcion == "3":
        print("\n👋 ¡Gracias por usar el programa! ¡Hasta pronto!")
        break
    else:
        print("❌ Opción no válida. Por favor, elige 1, 2 o 3.")



