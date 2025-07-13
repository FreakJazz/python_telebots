import requests

def obtener_chiste():
    url = "https://official-joke-api.appspot.com/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        chiste_data = response.json()
        
        setup = chiste_data.get('setup')
        punchline = chiste_data.get('punchline')
        
        return setup, punchline
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión o de la API: {e}")
        return None, None
    except ValueError:
        print("Error: La respuesta de la API no es un JSON válido.")
        return None, None

def main():
    print("¡Bienvenido al generador de chistes!")
    print("Presiona ENTER para obtener un chiste nuevo, o escribe 'salir' para terminar.")

    while True:
        entrada = input("\n> ").strip().lower()

        if entrada == "salir":
            print("¡Hasta la próxima! Espero que te hayas reído.")
            break
        elif entrada == "":
            setup, punchline = obtener_chiste()
            if setup and punchline:
                print("\n--- ¡Chiste! ---")
                print(f"Setup: {setup}")
                print(f"Punchline: {punchline}")
                print("----------------")
            else:
                print("No se pudo obtener un chiste. Intenta de nuevo.")
        else:
            print("Comando no reconocido. Presiona ENTER para un chiste o 'salir' para terminar.")

if __name__ == "__main__":
    main()