class Celular:
   

    def __init__(self, marca, modelo, año, color):
       
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        print(f"¡Nuevo celular {self.marca} {self.modelo} ({self.color}) del año {self.año} creado!")

    def llamar(self, numero_destino):
       
        print(f"Realizando llamada desde el {self.modelo} ({self.color}) a {numero_destino}...")
        return f"Llamada a {numero_destino} en curso."

    def enviar_mensaje(self, numero_destino, mensaje):
        
        print(f"Enviando mensaje desde el {self.modelo} ({self.color}) a {numero_destino}: '{mensaje}'")
        return f"Mensaje enviado a {numero_destino}."

    def obtener_info(self):
        
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Color: {self.color}"

# --- Operaciones con el Objeto Celular ---

if __name__ == "__main__":
    print("--- Creando objetos Celular ---")

    # Crear una instancia (objeto) de la clase Celular
    mi_celular = Celular("Samsung", "Galaxy S23", 2023, "Negro")
    celular_amigo = Celular("Apple", "iPhone 14 Pro", 2022, "Gris Espacial")

    print("\n--- Accediendo a atributos ---")
    print(f"Mi celular es un {mi_celular.marca} {mi_celular.modelo}.")
    print(f"El celular de mi amigo es de color {celular_amigo.color}.")

    print("\n--- Realizando operaciones (llamando a métodos) ---")

    # Realizar una llamada con mi_celular
    resultado_llamada = mi_celular.llamar("0991234567")
    print(f"Estado: {resultado_llamada}")

    # Enviar un mensaje con celular_amigo
    resultado_mensaje = celular_amigo.enviar_mensaje("0987654321", "Hola, ¿cómo estás?")
    print(f"Estado: {resultado_mensaje}")

    # Obtener información completa de mi_celular
    info_mi_celular = mi_celular.obtener_info()
    print(f"\nInformación de mi celular: {info_mi_celular}")

    # Obtener información completa de celular_amigo
    info_celular_amigo = celular_amigo.obtener_info()
    print(f"Información del celular de mi amigo: {info_celular_amigo}")

    print("\n--- Modificando un atributo ---")
    mi_celular.color = "Verde Oscuro"
    print(f"He cambiado el color de mi celular a {mi_celular.color}.")
    print(f"Nueva información de mi celular: {mi_celular.obtener_info()}")








    # Ejercicio 2: Listas y Diccionarios

# --- Parte 1: Crear una lista con tus 3 películas favoritas ---
# Una lista es una colección ordenada y mutable de elementos.
# Los elementos pueden ser de diferentes tipos de datos.
peliculas_favoritas = [
    "Interstellar",
    "El Señor de los Anillos: La Comunidad del Anillo",
    "Origen"
]

print("--- Mis 3 películas favoritas ---")
print(f"Lista de películas: {peliculas_favoritas}")


print("\n--- Operaciones con la lista de películas ---")


print(f"Mi primera película favorita es: {peliculas_favoritas[0]}") 
print(f"Mi tercera película favorita es: {peliculas_favoritas[2]}") 


peliculas_favoritas.append("Pulp Fiction")
print(f"Lista después de añadir 'Pulp Fiction': {peliculas_favoritas}")


peliculas_favoritas.remove("Origen")
print(f"Lista después de eliminar 'Origen': {peliculas_favoritas}")


print(f"Número total de películas en la lista: {len(peliculas_favoritas)}")


print("Recorriendo mis películas favoritas:")
for pelicula in peliculas_favoritas:
    print(f"- {pelicula}")


# --- Parte 2: Crear un diccionario con tu nombre, género y año ---

informacion_personal = {
    "nombre": "Milton",
    "genero": "Masculino",
    "año_nacimiento": 1990 
}

print("\n--- Mi información personal ---")
print(f"Diccionario de información: {informacion_personal}")


print("\n--- Operaciones con el diccionario de información ---")


print(f"Mi nombre es: {informacion_personal['nombre']}")
print(f"Mi género es: {informacion_personal['genero']}")


informacion_personal["año_nacimiento"] = 1992 
print(f"Año de nacimiento actualizado: {informacion_personal['año_nacimiento']}")
print(f"Diccionario después de actualizar el año: {informacion_personal}")

informacion_personal["ciudad"] = "Quito"
print(f"Diccionario después de añadir la ciudad: {informacion_personal}")


del informacion_personal["genero"]
print(f"Diccionario después de eliminar el género: {informacion_personal}")


print(f"Claves del diccionario: {informacion_personal.keys()}")


print(f"Valores del diccionario: {informacion_personal.values()}")


print("Recorriendo las claves de mi información:")
for clave in informacion_personal:
    print(f"- {clave}: {informacion_personal[clave]}")


print("Recorriendo pares clave-valor de mi información:")
for clave, valor in informacion_personal.items():
    print(f"- {clave}: {valor}")


    