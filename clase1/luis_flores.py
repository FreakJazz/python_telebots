#NUMEROS PRIMOS DEPENDE EL RANGO QUE ASIGNES
print("Ingres el rango que deseas saber de los numeros primos")
for numero in range(1, 10):
    if numero >1:
        cont=0
        i=2
        while i <numero and cont==0:
            resto=numero%i
            if resto ==0:
                cont+=1
            i+=1
        if cont==0:
            print(numero)
            
# MENU INTERATIVO

import datetime

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Mostrar una frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir del programa")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        print("\n🌟 'El éxito es la suma de pequeños esfuerzos repetidos día tras día.' 🌟")
    elif opcion == "2":
        fecha_actual = datetime.datetime.now()
        print("\n📅 Fecha actual:", fecha_actual.strftime("%d/%m/%Y %H:%M:%S"))
    elif opcion == "3":
        print("\n¡Hasta pronto!")
        break
    else:
        print("\n❗ Opción no válida. Por favor, elige 1, 2 o 3.")