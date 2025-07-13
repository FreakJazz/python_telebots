def es_primo(numero):
    
    if numero <= 1:
        return False  
        return True   
    elif numero % 2 == 0:
        return False
    else:
        
        i = 3
        while i * i <= numero:
            if numero % i == 0:
                return False  
            i += 2  
        return True  

def mostrar_primos_hasta_n():
    
    while True:
        try:
            n_str = input("Por favor, ingresa un número entero positivo (n): ")
            n = int(n_str)
            if n <= 0:
                print("Por favor, ingresa un número entero positivo mayor que cero. Inténtalo de nuevo.")
            else:
                break 
        except ValueError:
            print("Entrada inválida. Por favor, ingresa solo números enteros. Inténtalo de nuevo.")

    print(f"\nNúmeros primos del 1 al {n}:")
    primos_encontrados = False
    for i in range(1, n + 1):
        if es_primo(i):
            print(i)
            primos_encontrados = True

    if not primos_encontrados and n > 1:
        print(f"No se encontraron números primos en el rango de 1 a {n}. (El 2 es el primer primo, si n es menor que 2)")
    elif not primos_encontrados and n <= 1:
         print(f"No se encontraron números primos en el rango de 1 a {n}.")


if __name__ == "__main__":
    mostrar_primos_hasta_n()