<<<<<<< HEAD
from datetime import datetime

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("El número", num, "no es primo:", n, "es divisor")
            return False
    print("El número", num, "es primo")
    return True

def menu(num2):
    if num2 == 1:
        print("La frase motivacional es: '¡Sigue adelante, nunca te rindas!'")
    elif num2 == 2:
        print("La fecha de hoy es:", datetime.now().strftime("%d/%m/%Y"))
    elif num2 == 3:
        print("La hora actual es:", datetime.now().strftime("%H:%M:%S"))
    else:
        print("¡Gracias por usar el programa!")
    
if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    es_primo(num1)
    es_primo(num2)
    
    num3 = int(input("Ingrese un número para el menú (1-4): "))
=======
from datetime import datetime

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("El número", num, "no es primo:", n, "es divisor")
            return False
    print("El número", num, "es primo")
    return True

def menu(num2):
    if num2 == 1:
        print("La frase motivacional es: '¡Sigue adelante, nunca te rindas!'")
    elif num2 == 2:
        print("La fecha de hoy es:", datetime.now().strftime("%d/%m/%Y"))
    elif num2 == 3:
        print("La hora actual es:", datetime.now().strftime("%H:%M:%S"))
    else:
        print("¡Gracias por usar el programa!")
    
if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    es_primo(num1)
    es_primo(num2)
    
    num3 = int(input("Ingrese un número para el menú (1-4): "))
>>>>>>> 3d963b71f3488bde9135583b06a8c96b20a825b6
    menu(num3)