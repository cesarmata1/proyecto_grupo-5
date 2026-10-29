import json

def cargar_grupos(ruta):
    archivo = open(ruta, "r", encoding="utf-8")
    grupos = json.load(archivo)
    archivo.close()
    return grupos

def sentar_grupos(grupos, restaurante):
    mesas = []
    ocupacion = 0
    numero_mesa = 1

    for grupo in grupos:
        clientes = grupo["clientes"]

        if numero_mesa > restaurante["mesas_max"]:
            print("No quedan mesas disponibles.")
            break

        if ocupacion + clientes > restaurante["capacidad"]:
            print("No hay capacidad suficiente para este grupo.")
            continue

        mesa = {
            "numero": numero_mesa,
            "clientes": clientes
        }

        mesas.append(mesa)
        ocupacion += clientes
        numero_mesa += 1

    return mesas


def contar_clientes(mesas):
    total = 0

    for mesa in mesas:
        total += mesa["clientes"]

    return total
