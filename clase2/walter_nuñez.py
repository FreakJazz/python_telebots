# 📱 Ejercicio 1: Objetos
class Celular:
    """
    Clase Celular:
    - Atributos:
        - marca
        - modelo
        - año
        - color
    - Métodos:
        - llamar()
        - enviar_mensaje()
    """
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def llamar(self, numero):
        print(f"Llamando al número {numero} desde un {self.marca} {self.modelo}...")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a {numero}: '{mensaje}'")

def ejercicio_1():
    mi_celular = Celular("Samsung", "Galaxy S22", 2022, "Negro")
    mi_celular.llamar("0999999999")
    mi_celular.enviar_mensaje("0999999999", "Hola, ¿cómo estás?")
    print("Este objeto representa un celular moderno con métodos para llamar y enviar mensajes.")


# 🎬 Ejercicio 2: Listas y Diccionarios
def ejercicio_2():
    peliculas = ["Inception", "Interestelar", "Matrix"]
    persona = {
        "nombre": "Walter",
        "genero": "Masculino",
        "año": 2025
    }

    print("Mis películas favoritas son:")
    for pelicula in peliculas:
        print("-", pelicula)

    print("\nDatos personales:")
    for clave, valor in persona.items():
        print(f"{clave.capitalize()}: {valor}")


# ❓ Ejercicio 3: Trivia con POO
class Pregunta:
    def __init__(self, enunciado, opciones, respuesta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta = respuesta

    def mostrar(self):
        print("\n🧠 Pregunta:")
        print(self.enunciado)
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion}")

    def verificar_respuesta(self, eleccion_usuario):
        if self.opciones[eleccion_usuario - 1].lower() == self.respuesta.lower():
            print("✅ ¡Respuesta correcta!")
        else:
            print(f"❌ Respuesta incorrecta. La correcta era: {self.respuesta}")

def ejercicio_3():
    pregunta = Pregunta(
        "¿Cuál es el lenguaje de programación más popular en 2025?",
        ["Python", "Java", "C++", "JavaScript"],
        "Python"
    )
    pregunta.mostrar()
    try:
        eleccion = int(input("Elige una opción (1-4): "))
        if 1 <= eleccion <= 4:
            pregunta.verificar_respuesta(eleccion)
        else:
            print("Opción fuera de rango.")
    except ValueError:
        print("Entrada no válida. Debe ser un número.")


# Menú principal
if __name__ == "__main__":
    print("\n📋 MENÚ DE EJERCICIOS")
    print("1. Ejercicio de Objeto (Celular)")
    print("2. Ejercicio de Listas y Diccionarios")
    print("3. Ejercicio de Trivia con POO")
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        ejercicio_1()
    elif opcion == "2":
        ejercicio_2()
    elif opcion == "3":
        ejercicio_3()
    else:
        print(" Opción inválida.")
