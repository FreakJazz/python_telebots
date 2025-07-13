""" Crea:
- El objeto que definiste en clase y realiza operaciones con el.
- Explicar que es el objeto que hace y el proque de la elección"""


class Celular:

    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def llamar(self, numero):
        print(f"Llamando al número {numero} desde un {self.marca} {self.modelo}...")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a {numero}: {mensaje}")


# Crear objeto celular
celular = Celular("Samsung", "Galaxy S22", 2022, "Negro")

# Operaciones con el objeto
celular.llamar("0998765432")
celular.enviar_mensaje("0998765432", "Hola, ¿cómo estás?")


"""Ejercicio 2: Listas y diccionarios

Crea:
- Una lista con tus 3 películas favoritas.
- Un diccionario con tu nombre, genero, año.
- Imprime las operaciones."""


# 🎬 Lista de 3 películas favoritas, cada una como un diccionario
p_favoritas = [
    {"nombre": "El señor de los anillos", "genero": "Fantasía", "año": 2001},
    {"nombre": "Avatar", "genero": "Ciencia ficción", "año": 2009},
    {"nombre": "Inception", "genero": "Acción / Ciencia ficción", "año": 2010}
]

# 🔹 Imprimir cada película con su información
print(" Información de mis 3 películas favoritas:\n")
for pelicula in p_favoritas:
    print(f"Nombre: {pelicula['nombre']}")
    print(f"Género: {pelicula['genero']}")
    print(f"Año: {pelicula['año']}")
    print("-" * 30)  # línea separadora
    
    
"""     Ejercicio 3: Trivia con POO

1. Crea una clase `Pregunta` con `enunciado`, `opciones` y `respuesta`.
numero = int(input("Ingrese número: "))
2. Muestra la pregunta y permite al usuario responder.
3. Indica si la respuesta fue correcta o no."""


class Pregunta:

    def __init__(self, enunciado, opciones, respuesta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta = respuesta

    def mostrar(self):
        print("\n Pregunta:")
        print(self.enunciado)
        for i, opcion in enumerate(self.opciones):
            print(f"{i + 1}. {opcion}")

    def verificar(self, eleccion):
        return eleccion - 1 == self.respuesta


# Crear una pregunta
pregunta1 = Pregunta(
    "¿A qué altitud se encuentra Quito?",
    ["1000", "2850", "500", "4000"],
    1  # 2850 es la respuesta correcta (índice 1)
)

# Mostrar la pregunta
pregunta1.mostrar()

# Solicitar respuesta del usuario
try:
    numero = int(input("Ingrese el número de su respuesta: "))
    if pregunta1.verificar(numero):
        print("¡Respuesta correcta!")
    else:
        print(" Respuesta incorrecta.")
except ValueError:
    print(" Entrada no válida. Debes ingresar un número.")


