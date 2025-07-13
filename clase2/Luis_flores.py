## 🧪 Ejercicio 1:   Objetos
# Creamos la clase Celular
class Celular:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def llamar(self, numero):
        print(f"Llamando al {numero} desde un {self.marca} {self.modelo}...")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a {numero}: {mensaje}")


# Crear un objeto de la clase Celular
mi_celular = Celular("Samsung", "Galaxy S21", 2021, "Negro")

# Operaciones con el objeto
mi_celular.llamar("0991234567")
mi_celular.enviar_mensaje("0991234567", "¡Hola! ¿Cómo estás?")

#----------------------------------------------------------------------

## 🧪 Ejercicio 2: Listas y diccionarios
# Lista con mis 3 películas favoritas
peliculas = ["Interestelar", "Inception", "El Señor de los Anillos"]

# Diccionario con información de una película
pelicula_info = {
    "nombre": "Interestelar",
    "genero": "Ciencia Ficción",
    "año": 2014
}

# Operaciones
print("🎬 Mis películas favoritas son:")
for peli in peliculas:
    print("-", peli)

print("\n📄 Información de una película:")
for clave, valor in pelicula_info.items():
    print(f"{clave.capitalize()}: {valor}")
    

#------------------------------------------------
## 🧪 Ejercicio 3: Trivia con POO
# Clase Pregunta
class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

    def mostrar(self):
        print("\n❓", self.enunciado)
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion}")

    def verificar_respuesta(self, seleccion):
        if self.opciones[seleccion - 1].lower() == self.respuesta_correcta.lower():
            print("✅ ¡Respuesta correcta!")
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {self.respuesta_correcta}")


# Crear una pregunta
pregunta1 = Pregunta(
    "¿Cuál es el lenguaje principal para programar en ciencia de datos?",
    ["Java", "Python", "C++", "Ruby"],
    "Python"
)

# Mostrar y evaluar la pregunta
pregunta1.mostrar()
respuesta_usuario = int(input("Elige la opción correcta (1-4): "))
pregunta1.verificar_respuesta(respuesta_usuario)