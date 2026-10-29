def mostrar_menu():
    print("\n=== GESTOR DEL RESTAURANTE ===")
    print("1. Cargar restaurante")
    print("2. Cargar nuevas peticiones de grupos")
    print("3. Tomar un pedido")
    print("4. Cobrar y liberar una mesa")
    print("5. Ampliar el menú")
    print("6. Consultar estado")
    print("7. Salir")


def pedir_opcion():
    texto = input("Elige una opción (1-7): ")
    try:
        opcion = int(texto)
    except ValueError:
        print("Error: escribe un número.")
        return None
    if opcion < 1 or opcion > 7:
        print("Error: elige un número entre 1 y 7.")
        return None
    return opcion


def main():
    restaurante = None
    salir = False
    while not salir:
        mostrar_menu()
        opcion = pedir_opcion()
        if opcion is None:
            continue
        if opcion == 7:
            print("Hasta luego")
            salir = True
        elif opcion == 1:
            print("(pendiente) Cargar restaurante")
        elif restaurante is None:
            print("Primero tienes que cargar un restaurante (opción 1).")
        else:
            print("(pendiente) opción", opcion)


if __name__ == "__main__":
    main()