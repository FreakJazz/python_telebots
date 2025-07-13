## 🧪 Ejercicio 1:   Objetos

#Este objeto se llama ClienteContable. Representa a un cliente que tiene un negocio y puede necesitar declarar impuestos.

class ClienteContable:
    def __init__(self, nombre, tipo_negocio, necesita_declarar):
        self.nombre = nombre
        self.tipo_negocio = tipo_negocio
        self.necesita_declarar = necesita_declarar

    def mostrar_info(self):
        print(f"📌 Cliente: {self.nombre}")
        print(f"🏪 Tipo de negocio: {self.tipo_negocio}")
        print(f"🧾 ¿Debe declarar impuestos?: {'Sí' if self.necesita_declarar else 'No'}")

    def declarar_impuestos(self):
        if self.necesita_declarar:
            print(f"✅ Declarando impuestos para {self.nombre}...")
            self.necesita_declarar = False
        else:
            print(f"❌ {self.nombre} ya está al día con sus impuestos.")

# Crear un objeto cliente
cliente1 = ClienteContable("Cristina Moya", "Tienda Cris", True)

# Usar los métodos del objeto
cliente1.mostrar_info()
cliente1.declarar_impuestos()
cliente1.mostrar_info()

## 🧪 Ejercicio 2: Listas y diccionarios
# Lista de películas favoritas
peliculas = ["Coco", "Titanic", "Rapidos y Furiosos"]

# Diccionario con info de las películas
info_peliculas = {
    "Coco": {"genero": "Animación", "año": 2017},
    "Titanic": {"genero": "Romance", "año": 1997},
    "Rapidos y Furiosos": {"genero": "Acción", "año": 2001}
}

# Mostrar menú
print("🎬 MIS PELÍCULAS FAVORITAS")
print("1. Agregar una nueva película")
print("2. Buscar posición de una película")
print("3. Reemplazar una película por otra")

# Opción del usuario
opcion = input("Elige una opción (1-3): ")

if opcion == "1":
    nueva = input("Escribe el nombre de la nueva película: ")
    peliculas.append(nueva)
    print("Película agregada correctamente.")
    print("Lista actual:", peliculas)

elif opcion == "2":
    buscar = input("Escribe el nombre de la película que quieres buscar: ")
    if buscar in peliculas:
        posicion = peliculas.index(buscar)
        print(f"La película '{buscar}' está en la posición {posicion}.")
    else:
        print("La película no está en la lista.")

elif opcion == "3":
    antigua = input("¿Qué película quieres reemplazar?: ")
    if antigua in peliculas:
        nueva = input("¿Por cuál la quieres reemplazar?: ")
        index = peliculas.index(antigua)
        peliculas[index] = nueva
        print("Película reemplazada correctamente.")
        print("Lista actual:", peliculas)
    else:
        print("La película que quieres reemplazar no está en la lista.")

else:
    print("Opción no válida.")

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

    def verificar(self, respuesta_usuario):
        if self.opciones[respuesta_usuario - 1] == self.respuesta_correcta:
            print("✅ ¡Correcto!")
            return 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {self.respuesta_correcta}")
            return 0

# Lista de preguntas
pregunta1 = Pregunta("¿Cuál es la capital de Ecuador?", ["Guayaquil", "Quito", "Cuenca"], "Quito")
pregunta2 = Pregunta("¿Cuánto es 5 + 3?", ["6", "8", "10"], "8")
pregunta3 = Pregunta("¿Qué color resulta de mezclar azul y amarillo?", ["Verde", "Rojo", "Naranja"], "Verde")

preguntas = [pregunta1, pregunta2, pregunta3]

# Variable para llevar el puntaje
puntaje = 0

# Juego de trivia
print("BIENVENIDO A LA TRIVIA")
for pregunta in preguntas:
    pregunta.mostrar()
    try:
        respuesta = int(input("Tu respuesta (1-3): "))
        if 1 <= respuesta <= 3:
            puntaje += pregunta.verificar(respuesta)
        else:
            print("⚠️ Respuesta no válida. Debe ser 1, 2 o 3.")
    except:
        print("⚠️ Entrada inválida. Debe ser un número.")

# Resultado final
print(f"\n🏁 Fin del juego. Tu puntaje final es: {puntaje} de {len(preguntas)}")
