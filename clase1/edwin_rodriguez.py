import math

# ===============================================================
# PASO 1: Definir la función que comprueba si un número es primo
# ===============================================================
def es_primo(numero):
    """
    Función auxiliar que determina si un número es primo.
    Devuelve True si lo es, y False si no lo es.
    """
    # Los números menores o iguales a 1 no son considerados primos.
    if numero <= 1:
        return False
    
    # El 2 es el único número primo que es par.
    if numero == 2:
        return True
    
    # Si el número es par y no es 2, no es primo.
    if numero % 2 == 0:
        return False

    # Revisamos solo los divisores impares hasta la raíz cuadrada del número.
    # Es una optimización clave que acelera mucho el proceso.
    limite = int(math.sqrt(numero)) + 1
    for divisor in range(3, limite, 2):  # El '2' al final hace que salte de 2 en 2 (3, 5, 7...)
        if numero % divisor == 0:
            return False # Si encontramos un divisor, ya no es primo.
            
    # Si el bucle termina sin encontrar divisores, el número es primo.
    return True

# ===============================================================
# PASO 2: Escribir el programa principal que usa la función
# ===============================================================

# --- Programa Principal ---

print("--- Buscador de Números Primos --- por Edwin Rodriguez con el apoyo de IA :-)")

# 1. Solicitar el número al usuario y validarlo
while True:
    try:
        n_str = input("Introduce un número entero hasta el cual buscar primos: ")
        n = int(n_str)
        if n >= 2:
            break # El número es válido, salimos del bucle.
        else:
            print("Por favor, introduce un número que sea 2 o mayor.")
    except ValueError:
        print("Entrada no válida. Debes introducir un número entero.")

# 2. Crear una lista para almacenar los números primos encontrados
lista_primos_encontrados = []

# 3. Recorrer todos los números desde 2 hasta n
print(f"\nBuscando números primos del 1 al {n}...")
for numero_a_evaluar in range(2, n + 1):
    
    # 4. Llamar a nuestra función para cada número
    if es_primo(numero_a_evaluar):
        # Si la función devuelve True, añadimos el número a la lista
        lista_primos_encontrados.append(numero_a_evaluar)

# 5. Mostrar el resultado final al usuario
print("\n¡Búsqueda completada!")
print(f"Los números primos encontrados son:")
print(lista_primos_encontrados)


# Importamos los módulos necesarios al principio del script.
# - 'random' para elegir una frase al azar.
# - 'datetime' para obtener la fecha actual.
# - 'locale' para mostrar la fecha en español (opcional pero recomendado).
import random
from datetime import date
import locale

# --- Configuración Inicial (Opcional pero mejora la experiencia) ---
# Intentamos configurar el idioma a español para que la fecha se muestre correctamente.
# Si el sistema no tiene el paquete de idioma 'es_ES.UTF-8', usará el formato por defecto.
try:
    # Para sistemas Linux/macOS
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    try:
        # Para sistemas Windows
        locale.setlocale(locale.LC_TIME, 'Spanish')
    except locale.Error:
        print("Advertencia: No se pudo configurar el idioma a español. La fecha se mostrará en el formato del sistema.")


# --- Lista de Frases Motivacionales ---
frases_motivacionales = [
    "El único modo de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
    "La vida es 10% lo que te pasa y 90% cómo reaccionas a ello. - Charles R. Swindoll",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día. - Robert Collier",
    "Cree que puedes y ya estás a medio camino. - Theodore Roosevelt",
    "No esperes. El momento nunca será el adecuado. - Napoleon Hill"
]


# --- Bucle Principal del Menú ---
# Usamos un bucle 'while True' para que el menú se muestre repetidamente
# hasta que el usuario elija la opción de salir.
while True:
    # 1. Mostrar las opciones del menú al usuario
    print("\n" + "="*30)
    print("      MENÚ PRINCIPAL USANDO ASISTENTE DE IA  ")
    print("="*30)
    print("1. Mostrar una frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir del programa")
    print("="*30)

    # 2. Solicitar la elección del usuario
    opcion = input("Por favor, elige una opción (1, 2 o 3): ")

    # 3. Procesar la elección usando if/elif/else
    if opcion == '1':
        # Opción 1: Mostrar frase motivacional
        print("\n✨ Frase del día ✨")
        frase_elegida = random.choice(frases_motivacionales)
        print(f"-> {frase_elegida}")
        input("\n(Presiona Enter para volver al menú...)") # Pausa para que el usuario pueda leer

    elif opcion == '2':
        # Opción 2: Mostrar la fecha actual
        print("\n📅 Fecha Actual 📅")
        fecha_de_hoy = date.today()
        # Usamos .strftime() para formatear la fecha de una manera legible
        # %A: Nombre completo del día de la semana (Lunes)
        # %d: Día del mes (01, 31)
        # %B: Nombre completo del mes (Enero)
        # %Y: Año con 4 dígitos (2023)
        print(f"-> Hoy es {fecha_de_hoy.strftime('%A, %d de %B de %Y')}")
        input("\n(Presiona Enter para volver al menú...)") # Pausa

    elif opcion == '3':
        # Opción 3: Salir del programa
        print("\n¡Gracias por usar el programa! ¡Hasta luego! 👋")
        break  # 'break' rompe el bucle 'while True' y termina el programa

    else:
        # Si el usuario introduce algo diferente a '1', '2' o '3'
        print("\n❌ Opción no válida. Por favor, introduce un número del 1 al 3.")
        input("\n(Presiona Enter para intentarlo de nuevo...)")