"""
Ejercicio1
Clase: cuenta bancaria
Atributos: titular, numero_cuenta, saldo
Metodos: depositar, retirar, consultar_saldo
"""

class CuentaBancaria:

    def __init__(self, titular, numero_cuenta, saldo= 0.0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = float(saldo)

    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser mayor que cero.")
        self.saldo += monto
        print(f"Depósito exitoso: +{monto:.2f}. Saldo actual: {self.saldo:.2f}")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser mayor que cero.")
        elif monto > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
        else: 
            self.saldo -= monto
            print(f"Retiro exitoso: -{monto:.2f}. Saldo actual: {self.saldo:.2f}")

    def consultar_saldo(self) -> float:
        return self.saldo
"""Ejercicio 2
Listas y diccionarios
"""
lista_pelis = ["Pokemon", "Shrek", "Los Pitufos"]

#impresion de los elementos de la lista
print("Listado de peliculas")
for elemento in lista_pelis:
    print(f"- {elemento}")

#Diccionario de datos
misDatos = {
    "nombre" : "Ronald",
    "edad" : 30,
    "genero" : "Masculino"
}
#Impresion de los datos del diccionario
print("Mis datos:")
print(f"Nombre: {misDatos["nombre"]}  Edad: {misDatos["edad"]} Genero: {misDatos["genero"]}")

"""
Ejercicio 3 Trivia con POO
1. Crea una clase `Pregunta` con `enunciado`, `opciones` y `respuesta`.
2. Muestra la pregunta y permite al usuario responder.
3. Indica si la respuesta fue correcta o no.
"""
class Pregunta:
    def __init__(self, enunciado, opciones, respuesta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta = respuesta

    def mostrar(self) -> None:
        print(self.enunciado)
        numeros = range(1, len(self.opciones)+1)
        for numero, opcion in zip(numeros, self.opciones):
            print(f"  {numero}. {opcion}")

    def preguntar(self) -> bool:
        self.mostrar()
        respuesta_usuario = int(input("Tu respuesta (1,2,3....): "))
        if respuesta_usuario == self.respuesta:
            print("¡Correcto!")
            return True
        else:
            print(f"Incorrecto. La respuesta correcta era {self.respuesta}.")
            return False
        
if __name__ == "__main__":
    #Ejercicio 1
    cuenta = CuentaBancaria("Armando Lopez", "1700098563", 100.0)
    cuenta.depositar(150.0)
    cuenta.retirar(75.0)
    print(f"Saldo actual: {cuenta.consultar_saldo()}")
    #El ejericicio 2 ya se ejecuta sin llamarlo
    # Ejercicio 3
    q = Pregunta(
        "¿Cuál es la capital de Ecuador?",
        ["Madrid", "Berlín", "Quito", "Roma"],
        3
    )
    q.preguntar()