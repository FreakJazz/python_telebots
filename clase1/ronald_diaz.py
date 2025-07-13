"""
Ejercio 1
Numeros primos

Ejercicio 2 
Menu
"""
from datetime import datetime

def es_primo(num):
    bandera = 0
    for contador in range(1, num+1):
        if num % contador==0:
            bandera +=1
    if bandera <= 2:
        print(num)

def ejercicio1():
    try:
        while True:
            numero = int(input("Ingrese un número entero positivo:"))
            if numero > 0:
                break
        for cont in range(1, numero+1):
            es_primo(cont)
    except:
        print("Debe ingresar un número entero")
    

def menu():
    while True:
        print("*********************************************************")
        print("Seleccione una opción del menú (ingrese el número)")
        print("*********************************************************")
        print("1: Frase Motivacional")
        print("2: Fecha Actual")
        print("3: Salir")
        print("*********************************************************")
        try:
            opcion= int(input("Opción: "))
            if opcion == 1:
                print("Cree que puedes, y ya estarás a mitad de camino")
            elif opcion == 2:
                print(f"Fecha: {datetime.now().year} - {datetime.now().month} - {datetime.now().day} ")
            elif opcion == 3:
                break
            else:
                print("Debe seleccionar una de las opciones del menu")

        except:
            print("Debe ingresar un numero")

def ejercicio2():
    menu()

if __name__ == "__main__":
    ejercicio1()
    ejercicio2()
    

