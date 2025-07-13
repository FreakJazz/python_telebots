import requests

def obtener_chiste():
    try:
        respuesta = requests.get("https://official-joke-api.appspot.com/jokes/random")
        respuesta.raise_for_status()
        chiste = respuesta.json()
        return chiste
    except Exception as e:
        print(f"Error al obtener chiste: {e}")
        return None

def main():
    print("Presiona Enter para obtener un chiste o escribe 'salir' para terminar.")
    while True:
        entrada = input("> ").strip().lower()
        if entrada == "salir":
            print("¡Hasta luego!")
            break
        chiste = obtener_chiste()
        if chiste:
            print(f"\nSetup: {chiste['setup']}")
            print(f"Punchline: {chiste['punchline']}\n")
        else:
            print("No se pudo obtener un chiste, intenta de nuevo.")

if __name__ == "__main__":
    main()
