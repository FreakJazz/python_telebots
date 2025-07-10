from datetime import datetime
# ------------------DEBER 01-------------------
# funcion es primo 

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Ingrese un número: "))
print("Números primos del 1 al", n, ":")
for i in range(1, n + 1):
    if es_primo(i):
        print(i)
        
        
# --------------------------------DEBER 02 -------------
        print("\nMenú de opciones:")
        print("1. Mostrar una frase motivacional")
        print("2. Mostrar la fecha actual")
        print("3. Salir del programa")

        opcion = input("Ingrese una opcion del 1 al 3): ")

        if opcion == "1":
            print("¡Nunca te rindas, cada día es una nueva oportunidad para mejorar!")
        elif opcion == "2":
            print("Fecha actual:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif opcion == "3":
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")