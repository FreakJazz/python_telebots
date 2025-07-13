"""
# Ejercicio 1:   Objetos

Objeto elegido: Celular
Como atributos hemos elegido:
Marca: 
Modelo:
Color:
Almacenamiento:
peso:
Como método elegimos:
Mostrar la información
Encender
Apagar
Llamar
Enviar Mensajes
Instalar aplicaciones
"""
print(" -----EJERCICIO 1-----")
class Celular:
    def __init__(self, marca, modelo,color,almacenamiento,peso):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.almacenamiento = almacenamiento
        self.peso = peso

    def mostrar_info(self):
        print(f"Información general de tu celular")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Peso: {self.peso} gramos")

    def encender(self):
        print(f"Tu celular {self.marca} está encendido")

    def apagar(self):
        print(f"Tu celular {self.modelo}  se va apagar")
    
    def llamar(self):
        print(f"Llamando a Juan López desde tu celular {self.marca} ")

    def enviar(self):
        print(f"Mensaje enviado a Valeria desde un celular {self.modelo} de color {self.color}")

    def instalar_app(self):
        print(f"Tu celular tiene {self.almacenamiento} ocupados. No hay espacio disponible. ")

        

celular1 = Celular("Samsung", "Galaxy S24", "Gris", "256 GB", 233)
celular2 = Celular("Apple", "iPhone 15 Pro", "Negro espacial", "512 GB", 221)
celular3 = Celular("Xiaomi", "Redmi Note 13", "Azul", "128 GB", 205)
celular4 = Celular("Motorola", "Edge 50 Pro", "Verde bosque", "256 GB", 186)
celular5 = Celular("Google", "Pixel 8", "Rosa", "128 GB", 187)
celular6 = Celular("OnePlus", "12R", "Negro mate", "256 GB", 207)


# Lista con los celulares
lista_celulares = [celular1, celular2, celular3, celular4, celular5, celular6]

# Función para obtener el peso promedio
def peso_promedio(celulares):
    total = sum(celular.peso for celular in celulares)
    return total / len(celulares)

# Mostrar resultado
print(f"El peso promedio de los celulares es: {peso_promedio(lista_celulares):.2f} gramos")
    
celular1.mostrar_info()
celular2.encender()
celular3.apagar()
celular4.llamar()
celular5.enviar()
celular6.instalar_app()

"""
Ejercicio 2
## Ejercicio 2: Listas y diccionarios

Crea:
- Una lista con tus 3 películas favoritas.
- Un diccionario con su nombre, genero, año.
- Imprime las operaciones.

---

"""
print(" -----EJERCICIO 2-----")

lista_peliculas=["El gato con botas", "Chespirito","Alicia en el país de mas maravillas"]

# Agrega al final
lista_peliculas.append("Avatar")  
# Inserta en posición 1    
lista_peliculas.insert(1, "Titanic") 
# Mostrar cuántas películas hay
print(f"\nTotal de películas: {len(lista_peliculas)}")
# Ordenar alfabéticamente
lista_peliculas.sort()
# Eliminar una película si existe
if "Chespirito" in lista_peliculas:
    lista_peliculas.remove("Chespirito")

#Imprimimos la lista
for i, pelicula in enumerate(lista_peliculas, start=1):
    print(f"{i}. {pelicula}")



diccionario_peliculas = [{
    "nombre":"El gato con botas",
    "género":"Comedia",
    "año":2005
},
{    "nombre":"Chespirito",
    "género":"Drama",
    "año":2025
},
{
    "nombre":"Alicia en el país de las maravillas",
    "género":"Comedia",
    "año":200
}
]


diccionario_peliculas = [
    {
        "nombre": "El gato con botas",
        "género": "Comedia",
        "año": 2005
    },
    {
        "nombre": "Chespirito",
        "género": "Drama",
        "año": 2025
    },
    {
        "nombre": "Alicia en el país de las maravillas",
        "género": "Comedia",
        "año": 2000    }
]

for pelicula in diccionario_peliculas:
    print("." * 30)
    print(f"Nombre: {pelicula['nombre']}")
    print(f"Género: {pelicula['género']}")
    print(f"Año: {pelicula['año']}")
    
print(" -----EJERCICIO 3-----")

class Pregunta:
    def __init__(self, enunciado, opciones, respuesta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta = respuesta

    def mostrar(self):
        print("\n" + self.enunciado)
        for i, opcion in enumerate(self.opciones):
            print(f"{i + 1}. {opcion}")
        seleccion = int(input("Seleccione una opción (1-{}): ".format(len(self.opciones))))
        return seleccion - 1

    def es_correcta(self, seleccion_usuario):
        return seleccion_usuario == self.respuesta


preguntas = [
    Pregunta("¿Cuál es la capital de Ecuador?", ["Quito", "Guayaquil", "Cuenca", "Loja"], 0),
    Pregunta("¿Cuál es el río más largo de Ecuador?", ["Río Esmeraldas", "Río Napo", "Río Guayas", "Río Pastaza"], 1),
    Pregunta("¿En qué año se independizó Ecuador?", ["1822", "1810", "1820", "1830"], 0),
    Pregunta("¿Cuál es el volcán más alto de Ecuador?", ["Cotopaxi", "Chimborazo", "Tungurahua", "Sangay"], 1),
]

indice = 0

while indice < len(preguntas):
    pregunta = preguntas[indice]
    seleccion = pregunta.mostrar()

    if pregunta.es_correcta(seleccion):
        print("¡Correcto!")
    else:
        correcta = pregunta.opciones[pregunta.respuesta]
        print(f"Incorrecto. La respuesta correcta era: {correcta}")

    continuar = input("\n¿Quieres responder otra pregunta? (s/n): ").lower()
    if continuar != "s":
        break

    indice += 1


