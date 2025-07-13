import datetime

def es_primo(n):
    """Determina si un número es primo."""
    if n <= 1:
        return False
    if n == 2:  # El único primo par
        return True
    if n % 2 == 0:  # Descartar pares
        return False
    # Verificar divisores hasta √n (optimización)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def ejercicio1():
    """Solicita un número al usuario y verifica si es primo."""
    try:
        numero = int(input("Ingrese un número para verificar si es primo: "))
        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Mostrar frase motivacional")
    print("2. Mostrar fecha actual")
    print("3. Salir")

def ejercicio2():
    frases_motivacionales = [
        "¡Tú puedes lograr todo lo que te propongas! 💪",
        "Cada día es una nueva oportunidad para ser mejor. 🌟",
        "La perseverancia es la clave del éxito. 🚀",
        "No te rindas, el éxito está más cerca de lo que piensas. 🌈",
        "Cree en ti mismo y todo será posible. ✨"
    ]
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == "1":
            import random
            frase = random.choice(frases_motivacionales)  # Selecciona una frase ale
            print(f"\nFrase motivacional: {frase}")
        elif opcion == "2":
            fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
            print(f"\nLa fecha actual es: {fecha_actual}")
        elif opcion == "3":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("\n❌ Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    print("Bienvenido al programa de ejercicios.")
    ejercicio1()
    ejercicio2()
    print("Gracias por participar. ¡Hasta la próxima!")