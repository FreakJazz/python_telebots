# Clase que representa un celular
class Celular:
    def __init__(self, marca, modelo, año, color):
        """Constructor del objeto celular."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def llamar(self, numero):
        """Simula una llamada a un número."""
        print(f"Llamando al {numero} desde un {self.marca} {self.modelo}...")

    def enviar_mensaje(self, numero, mensaje):
        """Simula el envío de un mensaje a un número."""
        print(f"Enviando mensaje a {numero}: {mensaje}")


# Crear una instancia (objeto) de la clase Celular
mi_celular = Celular("Apple", "iPhone 13", 2021, "Negro")

# Operaciones con el objeto
mi_celular.llamar("0987654321")
mi_celular.enviar_mensaje("0987654321", "Hola, ¿cómo estás?")

"""
Este objeto representa un celular. Lo elegí porque es un dispositivo con el que interactuamos a diario.
Tiene atributos como marca, modelo, año y color, y puede realizar acciones como llamar y enviar mensajes.
Esto muestra cómo en POO los objetos agrupan datos y funciones relacionados.
"""

# EJERCICIO 2 Explicación del objeto

peliculas_favoritas = ["Interestelar", "El Origen", "Matrix"]

mis_datos = {
    "nombre": "Belén",
    "genero": "Femenino",
    "año": 2025
}

print("🎬 Mis películas favoritas son:", peliculas_favoritas)

for peli in peliculas_favoritas:
    print("👉", peli)

print("📄 Mis datos personales son:", mis_datos)

print("👤 Nombre:", mis_datos["nombre"])
print("♀️ Género:", mis_datos["genero"])
print("📅 Año:", mis_datos["año"])

# EJERCICIO 3 Clase que representa una pregunta de trivia
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
            print("❌ Respuesta incorrecta. La correcta era:", self.respuesta)


# Crear una instancia de la clase Pregunta
pregunta1 = Pregunta(
    "¿Cuál es el lenguaje de programación que estás aprendiendo?",
    ["Java", "Python", "C++", "JavaScript"],
    "Python"
)

# Mostrar la pregunta y pedir respuesta al usuario
pregunta1.mostrar()
eleccion = int(input("Elige una opción (1-4): "))

# Verificar la respuesta del usuario
pregunta1.verificar_respuesta(eleccion)
