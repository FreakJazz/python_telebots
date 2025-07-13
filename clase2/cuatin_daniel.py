
""" 
La clase Heroe representa a un superhéroe con un nombre y un poder.
Tiene un método para presentarse.
Elegimos esta clase para ilustrar el concepto de clases en Python, es una forma 
sencilla de entender cómo funcionan los objetos y métodos.
"""
# Ejercio 1: Definición de una clase Heroe
class Heroe:
    def __init__(self, nombre, genero, identidad_secreta, poder):
        self.nombre = nombre
        self.genero = genero
        self.identidad_secreta = identidad_secreta
        self.poder = poder

    def presentar(self):
        print(f"Soy {self.nombre} y tengo el poder de {self.poder}.", f"mi identidad secreta es {self.identidad_secreta}.")
        
    def to_json(self):
        return {
            "nombre": self.nombre,
            "genero": self.genero,
            "identidad_secreta": self.identidad_secreta,
            "poder": self.poder
        }


        
# Ejercicio 2: Listas y diccionarios

class Pelicula:
    def __init__(self, titulo, director, anio):
        self.titulo = titulo
        self.director = director
        self.anio = anio

    def mostrar_info(self):
        print(f"{self.titulo} ({self.anio}), dirigido por {self.director}.")
        
    
        
# Ejercicio 3: Trivia con POO

class Pregunta:
    def __init__(self, pregunta, opciones, respuesta_correcta):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

    def verificar_respuesta(self, respuesta_usuario):
        try:
            return self.opciones[int(respuesta_usuario) - 1] == self.respuesta_correcta
        except (ValueError, IndexError):
            return False

class Trivia:
    def __init__(self):
        self.preguntas = []
    
    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
    
    def iniciar_trivia(self):
        for pregunta in self.preguntas:
            print(pregunta.pregunta)
            for i, opcion in enumerate(pregunta.opciones, 1):
                print(f"{i}. {opcion}")
            respuesta_usuario = input("Selecciona la opción correcta: ")
            if pregunta.verificar_respuesta(respuesta_usuario):
                print("¡Respuesta correcta!")
            else:
                print(f"Respuesta incorrecta. La respuesta correcta era: {pregunta.respuesta_correcta}")    
    
if __name__ == "__main__":
    # Ejercicio 1: Crear un héroe y presentarlo
    print("************ Ejercicio 1: Clase Heroe ************")
    heroe = Heroe("Superman", "masculino", "Clark Kent", "Super fuerza")
    heroe.presentar()
    heroe.poder = "Volar"
    heroe.presentar()
    heroe_json = heroe.to_json()
    print("Héroe en formato JSON:", heroe_json)
    print("************ Fin del Ejercicio 1 ************\n")
    print("************ Ejercicio 2: Lista de Películas ************")
    # Ejercicio 2: Crear una lista de películas
    peliculas = [
        Pelicula("Toy Story", "John Lasseter", 1995),
        Pelicula("Forrest Gump", "Robert Zemeckis", 1994),
        Pelicula("Insidious", "James Wan", 2010),
        Pelicula("El Padrino", "Francis Ford Coppola", 1972),
    ]
    for pelicula in peliculas:
        pelicula.mostrar_info()
    print("************ Fin del Ejercicio 2 ************\n")
    print("************ Ejercicio 3: Trivia ************")
    # Ejercicio 3: Crear una trivia y iniciarla
    trivia = Trivia()
    pregunta1 = Pregunta(
        "¿Cuál es la capital de Francia?",
        ["Berlín", "Madrid", "París", "Roma"],
        "París"
    )
    trivia.agregar_pregunta(pregunta1)
    pregunta2 = Pregunta(
        "¿Cuál es el océano más grande del mundo?",
        ["Atlántico", "Índico", "Ártico", "Pacífico"],
        "Pacífico"
    )
    trivia.agregar_pregunta(pregunta2)
    pregunta3 = Pregunta(
        "¿Quién escribió 'Cien años de soledad'?",
        ["Gabriel García Márquez", "Mario Vargas Llosa", "Jorge Luis Borges", "Pablo Neruda"],
        "Gabriel García Márquez"
    )
    trivia.agregar_pregunta(pregunta3)
    trivia.iniciar_trivia()
