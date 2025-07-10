# close 1 valeria Quiñonez
# Ejercicio 1: Números primos
def es_primo(n):
    if n <= 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Ingrese un número: "))
print (f"Números primos del 1 al n : {n}")
for i in range(1, n + 1):
    if es_primo(i):
        print(i, end=' ')
#Ejercicio 2: Menu interactivo
def menu(frase_motivacional):
    print("Bienvenido al menú interactivo")
    print("1. Frase motivacional")
    print("2. Mostrar la fecha y hora actual")
    print("3. Salir")
opcion = int(input("Seleccione una opción: "))
if opcion == 1:
    print("Haz tu vida un sueño, y tu sueño una realidad.")
elif opcion == 2:
    print("Confia en tus esfuerzos, el éxito llegará.")
elif opcion == 3:
    print("La unica manera de hacer un gran trabajo es amar lo que haces.")
opcion = int(input("Seleccione una opción: 1, 2 o 3: "))
if opcion == 1:
    print("Haz tu vida un sueño, y tu sueño una realidad.")
    from datetime import datetime
    fecha_hora_actual = datetime.now()
    print("Fecha y hora actual: 19:53 pm ", fecha_hora_actual)
