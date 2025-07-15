"""
Explicar que es el objeto que hace y el proque de la elección:
    - Eleji el objeto de "Servicios de Diseño" poruqe es el servicio que ofrezco como diseñadora y que me permite demostrar el uso de clases y objetos en Python.
"""


"""
EJERCICIO 1: Objetos
    
"""

"""
Funcion para promocionar un servicio
    
"""

class SevicioDiseno:
    def __init__ (self, disenador, estudios, habilidades):
        self.disenador = disenador
        self.estudios = estudios
        self.habilidades = habilidades

    def mostrar_informacion(self):
        print(f" 📣 Diseñador: {self.disenador}")
        print(f"Estudios: {self.estudios}")
        print(f"Habilidades: {', '.join(self.habilidades)}\n")

"""
Funcion para promocionar un servicio
    
"""
def promocionar_servicio(servicio):
    print(f"📢  Promocionando a: {servicio.disenador} con habilidades en : {', '.join(servicio.habilidades)}")
    print(f"APROVECHA EL 15 % DE DESCUENTO EN TODOS LOS SERVICIOS DE DISEÑO\n"),


"""
Lista de Servicios de Diseño
    
""" 
servicios = [
    SevicioDiseno(
        "Andrea Yanez",
        "Universidad Tecnica de Cotopaxi",  
        ["Photoshop, Illustrator, Affter Effects"]
    ),
    SevicioDiseno(
        "Carlos Lopez",
        "Universidad Tecnica de Ambato",  
        ["Figma, Canva, Indesign"]
    )
]

"""
Informacion de Servicios de Diseño
    
""" 
print("Servicios de Diseño Disponibles:\n")
for servicio in servicios:
    servicio.mostrar_informacion(),

"""
Promociones Actuales
    
""" 

print("Promociones actuales:\n")
for servicio in servicios:
    promocionar_servicio(servicio)
    

"""
EJERCICIO 2: Listas y diccionarios
    
"""

"""
Diccionario de peliculas favoritas
    
"""
fav_peliculas = {
    "Olvida de mi":{
        "genero": "Drama",
        "año" : 2004
    },
    "El origen":{
        "genero": "Romance",
        "año": 2009
    },
    "El numero 13":{
        "genero": "Misterio",
        "año": 2006
    }
}


"""
Lista de peliculas favoritas
    
"""
pelis_favoritas = list(fav_peliculas.keys())

print("\nMis 3 películas favoritas son:")
for peli in pelis_favoritas:
    print(f"- {peli}")


"""
Informacion peliculas favoritas
    
"""
print("\nMis películas favoritas:")
for peli in pelis_favoritas:
    genero = fav_peliculas[peli]["genero"]
    año = fav_peliculas[peli]["año"]
    print(f"- {peli} - Género: {genero}, Año: {año}")

"""
Operaciones con el diccionario de peliculas favoritas
    
""" 
print("\n - Generos de mis peliculas favoritas:")
for peli in pelis_favoritas:
  print(f"{peli} : {fav_peliculas[peli]['genero']}")

print("\n - Años de mis peliculas favoritas:")
for peli in pelis_favoritas:   
    print(f"{peli} : {fav_peliculas[peli]['año']}")

"""
Operaciones con el diccionario de peliculas favoritas
    
""" 
print("\n - Peliculas del año 2006:")
for peli in fav_peliculas:
    if fav_peliculas [peli]["año"] == 2006:
        print(f"- {peli} ({fav_peliculas[peli]['año']})") 

"""
EJERCICIO 2: Trivia con POO
    
"""
"""
Crear clase de pregunta
    
"""
class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
    

    def mostrar(self):
        print(f"\n{self.enunciado}")
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion}")

    def verificar_respuesta(self, seleccion_usuario):
        if self.opciones[seleccion_usuario - 1].lower () == self.respuesta_correcta.lower():
            print ("Respuesta Correcta")
        else:
            print(f"Incorrecto, La respuesta correcta es: {self.enunciado}")

"""
Crear la pregunta
    
"""
pregunta1 = Pregunta(
    "¿Cuál es el servicio de diseño que se centra en identidad de marca?",
    ["diseño publicitario","Branding","Diseño editorial","Diseño Web"],
    "Branding"
)

"""
Responder pregunta
 
"""
pregunta1.mostrar()

try: 
    numero = int(input("Ingrese una de las opciones (1-4): "))
    if 1 <= numero <= len(pregunta1.opciones):
        pregunta1.verificar_respuesta(numero)
    else:   
        print("Opcion Incorrecta")
except ValueError:
        print("Ingresa una opncion del 1 al 4")