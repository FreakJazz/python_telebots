# Ejercicio 1: Números primos
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def ejercicio1():
    n = int(input("Ingresa un número: "))
    print(f"Números primos del 1 al {n}:")
    for num in range(1, n + 1):
        if es_primo(num):
            print(num, end=" ")
    print()

# Ejercicio 2: Menú interactivo
def ejercicio2():
    print("\n--- MENÚ INTERACTIVO ---")
    while True:
        print("\n1. Mostrar frase motivacional")
        print("2. Mostrar fecha actual")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("¡Hoy es un gran día para lograr tus metas!")
        elif opcion == "2":
            from datetime import datetime
            fecha = datetime.now()
            print(f"Fecha actual: {fecha.strftime('%d/%m/%Y %H:%M:%S')}")
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")

def main():
    print("EJERCICIO 1 - NÚMEROS PRIMOS")
    ejercicio1()
    
    print("\nEJERCICIO 2 - MENÚ INTERACTIVO")
    ejercicio2()

if __name__ == "__main__":
    main()
    print("¡Programa terminado!")