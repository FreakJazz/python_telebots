import datetime

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def ejercicio_1():
    try:
        n = int(input("Ingrese un número: "))
        print(f"Números primos del 1 al {n}:")
        for i in range(1, n + 1):
            if es_primo(i):
                print(i, end=" ")
        print("\n")  # Salto de línea final
    except ValueError:
        print("Por favor, ingrese un número válido.\n")

def ejercicio_2():
    while True:
        print("\n--- MENÚ EJERCICIO 2 ---")
        print("1. Mostrar una frase motivacional")
        print("2. Mostrar la fecha actual")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            print(" ¡Sigue adelante, lo mejor está por venir!")
        elif opcion == "2":
            fecha_actual = datetime.datetime.now()
            print("Fecha actual:", fecha_actual.strftime("%Y-%m-%d %H:%M:%S"))
        elif opcion == "3":
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ejecutar Ejercicio 1: Números primos")
        print("2. Ejecutar Ejercicio 2: Menú interactivo")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            print(" ¡Programa finalizado!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
