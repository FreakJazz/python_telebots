"""
Que es objeto : un objeto es una instancia de una clase. 
Es como un bloque de construcción que contiene datos (llamados atributos) 
y funcionalidades (métodos)

Clase Celular
Atributos:
 - Marca,Modelo,Año,Color
Metodos:
- Llamar,Enviar mensaje    
"""
class Celular:
    def __init__(self,marca,modelo,ano,color):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color
    def llamar(self):
        print(f"Llamando desde un {self.marca} {self.modelo}...")
    
    def enviar_mensaje(self):
        print(f"Enviando mensaje desde un {self.marca} {self.modelo}...")
            
if __name__ =="__main__":
    mi_celular = Celular("Samsung", "Galaxy S21", 2021, "Negro")
    mi_celular.llamar()
    mi_celular.enviar_mensaje()
    

## 🧪 Ejercicio 2: Listas y diccionarios

# Ejercicio 2 Lista

peliculas = ["Guerra de las galaxias","Star Trek","Mira quien habla"]
print("Lista original ----> ", peliculas)
# operaciones con listas
print("OPERACIONES CON LISTAS")
peliculas.append("Juan de Dios")
print("agregar elemento a una lista ------>  ", peliculas)
peliculas.sort()
print("peliculas ordenadas -------> ", peliculas)
peliculas.remove("Star Trek")
print("eliminar elemento de una lista -------> ", peliculas)
peliculas.reverse()
print("lista en orden inverso -------> ", peliculas)




# diccionario

datos = {
    "nombre": "Boris",
    "genero": "masculino",
    "edad": 2025
}
print("-------Diccionario------")
print("Diccionario origen ------->", datos)

# Operaciones con diccionarios
# 1.- Agregar a Diccionario
datos["peso"] = 145
datos["altura"] = 1.70
print("Diccionario agregado", datos)

# 2.- Eliminar
datos.pop("edad")
print("Diccionario eliminado", datos)

# 3.- Consultar
print("Consultar llaves del diccionario:", datos.keys())
print("Consultar valores del diccionario:", datos.values())
print("Consultar items del diccionario:", datos.items())



## 🧪 Ejercicio 3: Trivia con POO

class Pregunta:
    def __init__(self, enunciado, opciones, respuesta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta = respuesta

    def mostrar(self):
        print(self.enunciado)
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion}")

    def responder(self):
        try:
            numero = int(input("Ingrese el número de la opción correcta: "))
            if self.opciones[numero - 1].lower() == self.respuesta.lower():
                print("¡Respuesta correcta!")
            else:
                print("Respuesta incorrecta.")
        except (ValueError, IndexError):
            print("Opción inválida.")

if __name__ == "__main__":
    pregunta1 = Pregunta(
        "¿Cuál es la capital de Francia?",
        ["Madrid", "París", "Roma", "Berlín"],
        "París"
    )
    pregunta1.mostrar()
    pregunta1.responder()
