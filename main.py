import json
from mesas import cargar_grupos, sentar_grupos, contar_clientes, mostrar_mesas


def main():
    archivo = open("restaurante.json", "r", encoding="utf-8")
    restaurante = json.load(archivo)
    archivo.close()

    grupos = cargar_grupos("grupos.json")

    mesas = []
    numero_mesa = 1

    mesas, numero_mesa = sentar_grupos(
        grupos, restaurante, mesas, numero_mesa
    )

    print("\nRestaurante:", restaurante["nombre"])
    print("Mesas ocupadas:", len(mesas))
    print("Clientes sentados:", contar_clientes(mesas))

    print("\nEstado de las mesas:")
    mostrar_mesas(mesas)


if __name__ == "__main__":
    main()