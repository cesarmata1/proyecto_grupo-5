import json
from mesas import cargar_grupos, sentar_grupos, contar_clientes


def main():
    archivo = open("restaurante.json", "r", encoding="utf-8")
    restaurante = json.load(archivo)
    archivo.close()

    grupos = cargar_grupos("grupos.json")

    mesas = []
    mesas = sentar_grupos(grupos, restaurante, mesas)

    print("Restaurante:", restaurante["nombre"])
    print("Mesas ocupadas:", len(mesas))
    print("Clientes sentados:", contar_clientes(mesas))


if __name__ == "__main__":
    main()
