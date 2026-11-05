import json

def cargar_grupos(ruta):
    archivo = open(ruta, "r", encoding="utf-8")
    grupos = json.load(archivo)
    archivo.close()
    return grupos


def sentar_grupos(grupos, restaurante, mesas, numero_mesa):
    ocupacion = contar_clientes(mesas)

    for grupo in grupos:
        clientes = grupo["clientes"]

        if clientes <= 0:
            print("Numero de clientes invalido.")
            continue

        if len(mesas) >= restaurante["mesas_max"]:
            print("No quedan mesas disponibles.")
            break

        if ocupacion + clientes > restaurante["capacidad"]:
            print("No hay capacidad suficiente para este grupo.")
            continue

        mesa = {
            "numero": numero_mesa,
            "clientes": clientes,
            "estado": "ocupada",
            "pedido": {}
        }

        mesas.append(mesa)
        ocupacion += clientes
        numero_mesa += 1

        print("Grupo sentado en la mesa", mesa["numero"])

    return mesas, numero_mesa



def contar_clientes(mesas):
    total = 0

    for mesa in mesas:
        total += mesa["clientes"]

    return total

def mostrar_mesas(mesas):
    if len(mesas) == 0:
        print("No hay mesas ocupadas.")
    else:
        for mesa in mesas:
            print("Mesa:", mesa["numero"])
            print("Clientes:", mesa["clientes"])
            print("Estado:", mesa["estado"])
            print("--------------------")

