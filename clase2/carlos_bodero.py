#Clase 2 ejercios ,2  y 3
#Ejercicio 1
""" Celular:
Propiedades:
    Marca --> define la marca o fabricante del dispositivo
    Modelo --> el modelo del dispositivo
    Año --> el año de fabricación
    Color  --> el color del dispositivo
Metodos:
    Llamar  --> realiza una llamada 
    Enviar mensaje --> enviar mensaje de texto a un número de teléfono
    Tomar_foto  --> toma una fotografía
    Escuchar_Musica --> abre la aplicación para escuchar música
    Ver_Video  --> abre la aplicación para ver un video
"""

class Celular:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.anio = ""
        self.color = ""

    def __init__(self,marca,modelo,anio,color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def mostrarInfo(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.anio} Color: {self.color}")

    def llamar(self,numero):
        print(f"Lamando {numero}....")

    def enviarMensaje(self,numero,mensaje):
        print(f"Enviado el mensaje :{mensaje}\nDestino: {numero}")

    def tomarFoto(self):
        print(f"El celular {self.modelo} está tomando foto")

    def escucharMusica(self):
        print(f"El celular {self.modelo} está utilizando una app para reproducir música ")

    def verVideo(self):
        print(f"El celular {self.modelo} esta mostrando video desde una app")

# clase para ejercicio 3 trivia con POO
class Pregunta:
    opciones = []
    def __init__(self,pregunta,respuesta,opciones):
        self.pregunta = pregunta
        self.opciones = list(opciones)
        self.respuesta = respuesta

    def mostrarPregunta(self):
        print(f" {self.pregunta} : ")
        indice = 1
        for opcion in self.opciones:
            print(f" {indice} {opcion}")
            indice += 1

    def validarRespuesta(self,respuestaUsuario):
        if self.respuesta == respuestaUsuario:
            return True
        else:
            return False
    

          
        
        


if __name__ == "__main__":
    print("Ejercicio 1: Probando objeto...")
    eltelefono = Celular("Samsung","A11","2023","blanco")
    eltelefono.mostrarInfo()
    eltelefono.color = "Azul"
    eltelefono.mostrarInfo()
    eltelefono.llamar("0983334678")
    eltelefono.enviarMensaje("mensaje de prueba","0999243659")
    eltelefono.escucharMusica()
    eltelefono.tomarFoto()
    eltelefono.verVideo()
    print("-"*50)
    
    print("Ejercicio 2 Listas y Diccionarios")

    infoPelicula1 = {"Nombre":"Amelie","genero":"drama","Anio":2000}
    infoPelicula2 = {"Nombre":"Caída del Halcón Negro","genero":"bélico","Anio":2001}
    infoPelicula3 = {"Nombre":"Batman","genero":"accion","Anio":2020}

    Listado = [infoPelicula1,infoPelicula2,infoPelicula3]

    for pelicula in Listado:
        print(pelicula)

    infoPelicula3["genero"]="super heroes"
    infoPelicula3["Anio"] = 2021

    infoPelicula4 = {"Nombre":"El origen","genero":"accion","Anio":2011}

    Listado.append(infoPelicula4)
    Listado.remove(infoPelicula1)

    print("Después de realizar operaciones")

    for pelicula in Listado:
        print(pelicula)

    print("-"*50)
    print("Ejercicio 3 Trivia con POO")
    pregunta1 = Pregunta("Cuál es la capital de Ecuador",3,["Ambato","Cuenca","Quito","Manta"])
    
    pregunta1.mostrarPregunta()

    respuestaU = int(input("Su respuesta es (ingrese el número correspondiente):"))

    if pregunta1.validarRespuesta(respuestaU):
        print("Respuesta correcta")
    else:
        print("Respuesta Incorrecta")


    

    
