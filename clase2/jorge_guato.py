# Ejercicio 1: Objetos - Libro
class Libro:
    """
    Clase Libro que representa un libro con sus características básicas.
    
    Atributos:
    - titulo: Nombre del libro
    - autor: Autor del libro
    - año: Año de publicación
    - genero: Género literario
    - paginas: Número de páginas
    - leido: Estado de lectura (True/False)
    
    Métodos:
    - leer(): Marca el libro como leído
    - obtener_info(): Muestra información del libro
    - es_clasico(): Determina si es un libro clásico (más de 50 años)
    """
    
    def __init__(self, titulo, autor, año, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero
        self.paginas = paginas
        self.leido = False
    
    def leer(self):
        """Marca el libro como leído"""
        self.leido = True
        print(f"Has terminado de leer '{self.titulo}'")
    
    def obtener_info(self):
        """Muestra la información completa del libro"""
        estado = "Leído" if self.leido else "No leído"
        return f"""
        Título: {self.titulo}
        Autor: {self.autor}
        Año: {self.año}
        Género: {self.genero}
        Páginas: {self.paginas}
        Estado: {estado}
        """
    
    def es_clasico(self):
        """Determina si el libro es clásico (más de 50 años)"""
        from datetime import datetime
        año_actual = datetime.now().year
        return (año_actual - self.año) > 50

def ejercicio1():
    """Ejercicio 1: Crear y usar objetos Libro"""
    print("=" * 50)
    print("EJERCICIO 1: OBJETOS - LIBRO")
    print("=" * 50)
    
    # Crear objetos libro
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico", 432)
    libro2 = Libro("1984", "George Orwell", 1949, "Distopía", 328)
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Infantil", 96)
    
    # Realizar operaciones
    print("Información inicial de los libros:")
    print(libro1.obtener_info())
    print(libro2.obtener_info())
    print(libro3.obtener_info())
    
    # Leer algunos libros
    libro1.leer()
    libro3.leer()
    
    # Verificar si son clásicos
    print(f"\n¿'{libro1.titulo}' es clásico? {libro1.es_clasico()}")
    print(f"¿'{libro2.titulo}' es clásico? {libro2.es_clasico()}")
    print(f"¿'{libro3.titulo}' es clásico? {libro3.es_clasico()}")
    
    print("\n**Explicación del objeto Libro:**")
    print("Elegí el objeto Libro porque es fácil de entender y útil para gestionar una biblioteca personal.")
    print("Permite almacenar información importante como título, autor, año, género y páginas.")
    print("Los métodos permiten interactuar con el libro: marcarlo como leído, obtener información y verificar si es clásico.")

def ejercicio2():
    """Ejercicio 2: Listas y diccionarios"""
    print("\n" + "=" * 50)
    print("EJERCICIO 2: LISTAS Y DICCIONARIOS")
    print("=" * 50)
    
    # Lista con 3 películas favoritas
    peliculas_favoritas = ["El Padrino", "Pulp Fiction", "Forrest Gump"]
    
    # Diccionario con información de cada película (nombre, género, año)
    informacion_peliculas = {
        "El Padrino": {
            "genero": "Drama",
            "año": 1972
        },
        "Pulp Fiction": {
            "genero": "Crimen",
            "año": 1994
        },
        "Forrest Gump": {
            "genero": "Drama",
            "año": 1994
        }
    }
    
    # Imprimir operaciones
    print("Mis 3 películas favoritas:")
    for i, pelicula in enumerate(peliculas_favoritas, 1):
        print(f"{i}. {pelicula}")
    
    print(f"\nPrimera película favorita: {peliculas_favoritas[0]}")
    print(f"Última película favorita: {peliculas_favoritas[-1]}")
    print(f"Total de películas: {len(peliculas_favoritas)}")
    
    print("\nInformación detallada de cada película:")
    for pelicula in peliculas_favoritas:
        info = informacion_peliculas[pelicula]
        print(f"\n🎬 {pelicula}:")
        print(f"   Género: {info['genero']}")
        print(f"   Año: {info['año']}")
    
    print("\nOperaciones con el diccionario:")
    print(f"Película más antigua: {min(informacion_peliculas.items(), key=lambda x: x[1]['año'])[0]}")
    print(f"Película más reciente: {max(informacion_peliculas.items(), key=lambda x: x[1]['año'])[0]}")
    
    # Contar géneros
    generos = [info['genero'] for info in informacion_peliculas.values()]
    print(f"Géneros: {', '.join(set(generos))}")

# Ejercicio 3: Trivia con POO
class Pregunta:
    """
    Clase Pregunta para crear preguntas de trivia.
    
    Atributos:
    - enunciado: La pregunta a realizar
    - opciones: Lista de opciones posibles
    - respuesta: Número de la opción correcta (1-4)
    """
    
    def __init__(self, enunciado, opciones, respuesta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta = respuesta
    
    def mostrar_pregunta(self):
        """Muestra la pregunta y sus opciones"""
        print(f"\n{self.enunciado}")
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion}")
    
    def verificar_respuesta(self, respuesta_usuario):
        """Verifica si la respuesta del usuario es correcta"""
        return respuesta_usuario == self.respuesta

def ejercicio3():
    """Ejercicio 3: Trivia con POO"""
    print("\n" + "=" * 50)
    print("EJERCICIO 3: TRIVIA CON POO")
    print("=" * 50)
    
    # Crear preguntas de trivia
    preguntas = [
        Pregunta(
            "¿Cuál es la capital de Ecuador?",
            ["Guayaquil", "Quito", "Cuenca", "Ambato"],
            2
        ),
        Pregunta(
            "¿En qué año se fundó Python?",
            ["1989", "1991", "1995", "2000"],
            2
        ),
        Pregunta(
            "¿Cuál es el planeta más grande del sistema solar?",
            ["Tierra", "Marte", "Júpiter", "Saturno"],
            3
        )
    ]
    
    puntuacion = 0
    total_preguntas = len(preguntas)
    
    print("¡Bienvenido a la trivia!")
    print(f"Responde las siguientes {total_preguntas} preguntas:")
    
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {i}:")
        pregunta.mostrar_pregunta()
        
        try:
            respuesta = int(input("Tu respuesta (1-4): "))
            if 1 <= respuesta <= 4:
                if pregunta.verificar_respuesta(respuesta):
                    print("¡Correcto! ✓")
                    puntuacion += 1
                else:
                    print(f"Incorrecto. La respuesta correcta era: {pregunta.respuesta}")
            else:
                print("Opción inválida. Se considera incorrecta.")
        except ValueError:
            print("Por favor, ingresa un número del 1 al 4.")
    
    print(f"\n¡Trivia terminada!")
    print(f"Puntuación final: {puntuacion}/{total_preguntas}")
    if puntuacion == total_preguntas:
        print("¡Excelente! Respondiste todas correctamente.")
    elif puntuacion >= total_preguntas // 2:
        print("¡Bien hecho! Tienes un buen conocimiento.")
    else:
        print("Sigue estudiando, puedes mejorar.")

def main():
    """Función principal que ejecuta todos los ejercicios"""
    print("🎯 PROGRAMA DE EJERCICIOS DE PROGRAMACIÓN")
    print("=" * 60)
    
    # Ejecutar Ejercicio 1: Objetos
    ejercicio1()
    
    # Ejecutar Ejercicio 2: Listas y Diccionarios
    ejercicio2()
    
    # Ejecutar Ejercicio 3: Trivia con POO
    ejercicio3()
    
    print("\n" + "=" * 60)
    print("🎉 ¡TODOS LOS EJERCICIOS COMPLETADOS!")
    print("=" * 60)

if __name__ == "__main__":
    main()