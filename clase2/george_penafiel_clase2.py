# Clase 2 - GEORGE ANTHONY PEÑAFIEL ALVARADO

# 🧪 Ejercicio 1: Objetos
print("\n--- EJERCICIO 1: OBJETOS ---")
class Celular:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def llamar(self, numero):
        return f"Llamando al {numero} desde un {self.marca} {self.modelo}"

    def enviar_mensaje(self, mensaje):
        return f"Mensaje enviado: {mensaje}"

mi_celular = Celular("Samsung", "Galaxy A52", 2021, "Negro")
print(mi_celular.llamar("0999999999"))
print(mi_celular.enviar_mensaje("Hola, ¿cómo estás?"))

# 🧪 Ejercicio 2: Listas y Diccionarios
print("\n--- EJERCICIO 2: LISTAS Y DICCIONARIOS ---")
peliculas = ["Interestelar", "Inception", "El origen"]
info = {
    "nombre": "Juan",
    "genero": "Masculino",
    "año": 2000
}
print("Películas favoritas:", peliculas)
print("Información personal:", info)
print("Primera película:", peliculas[0])
print("Nombre del usuario:", info["nombre"])

# 🧪 Ejercicio 3: Trivia con POO
print("\n--- EJERCICIO 3: TRIVIA ---")
class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

    def mostrar(self):
        print(self.enunciado)
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion}")

    def responder(self, respuesta_usuario):
        if self.opciones[respuesta_usuario - 1] == self.respuesta_correcta:
            print("¡Correcto!")
        else:
            print("Incorrecto. La respuesta correcta era:", self.respuesta_correcta)

pregunta1 = Pregunta(
    "¿Cuál es el planeta más grande del sistema solar?",
    ["Tierra", "Marte", "Júpiter", "Venus"],
    "Júpiter"
)

pregunta1.mostrar()
respuesta = int(input("Selecciona una opción (1-4): "))
pregunta1.responder(respuesta)
