import os

from mesas import cargar_restaurante, cargar_grupos, sentar_grupos, mostrar_mesas
from pedidos import tomar_pedido, ampliar_menu
from cobros import (buscar_mesa, elegir_mesa_a_cobrar, cobrar_mesa,
                    consultar_estado, registrar_ventas, mostrar_resumen_ventas)


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


def elegir_archivo_json(carpeta):
    if not os.path.isdir(carpeta):
        print("No existe la carpeta", carpeta)
        return None
    archivos = []
    for nombre in sorted(os.listdir(carpeta)):
        if nombre.endswith(".json"):
            archivos.append(nombre)
    if len(archivos) == 0:
        print("No hay archivos .json en", carpeta)
        return None

    print("\nArchivos disponibles en", carpeta + ":")
    for i, nombre in enumerate(archivos, 1):
        print(" ", i, "-", nombre)
    texto = input("Elige un archivo: ")
    try:
        eleccion = int(texto)
    except ValueError:
        print("Error: escribe un número.")
        return None
    if eleccion < 1 or eleccion > len(archivos):
        print("Error: opción fuera de rango.")
        return None
    return os.path.join(carpeta, archivos[eleccion - 1])


def cargar_datos_restaurante():
    ruta_restaurante = elegir_archivo_json(".")
    if ruta_restaurante is None:
        return None, None
    try:
        restaurante = cargar_restaurante(ruta_restaurante)
    except (OSError, ValueError, KeyError):
        print("Error: no se ha podido leer el restaurante.")
        return None, None
    if restaurante is None:
        return None, None
    for clave in ["nombre", "capacidad", "mesas_max", "menu"]:
        if clave not in restaurante:
            print("Error: este archivo no es un restaurante (falta", clave + ").")
            return None, None
    return restaurante, ruta_restaurante


def siguiente_numero_mesa(mesas):
    mayor = 0
    for mesa in mesas:
        if mesa["numero"] > mayor:
            mayor = mesa["numero"]
    return mayor + 1


def cargar_y_sentar_grupos(restaurante, mesas):
    carpeta = "mesas"
    if not os.path.isdir(carpeta):
        carpeta = "."
    ruta_grupos = elegir_archivo_json(carpeta)
    if ruta_grupos is None:
        return mesas
    try:
        grupos = cargar_grupos(ruta_grupos)
        numero_mesa = siguiente_numero_mesa(mesas)
        resultado = sentar_grupos(grupos, restaurante, mesas, numero_mesa)
    except (OSError, ValueError, KeyError, TypeError):
        print("Error: el archivo de grupos no tiene el formato correcto.")
        return mesas
    if isinstance(resultado, tuple):
        mesas = resultado[0]
    else:
        mesas = resultado
    mostrar_mesas(mesas)
    return mesas


def elegir_mesa_ocupada(mesas):
    ocupadas = []
    for mesa in mesas:
        if mesa["estado"] == "ocupada":
            ocupadas.append(mesa)
    if len(ocupadas) == 0:
        print("No hay mesas pendientes de pedido.")
        return None

    print("\nMesas pendientes de pedido:")
    for mesa in ocupadas:
        print("  Mesa", mesa["numero"], "-", mesa["clientes"], "clientes")
    texto = input("Número de mesa (Enter para volver): ")
    if texto == "":
        return None
    try:
        numero_mesa = int(texto)
    except ValueError:
        print("Error: escribe un número.")
        return None
    if buscar_mesa(ocupadas, numero_mesa) is None:
        print("Esa mesa no está pendiente de pedido.")
        return None
    return numero_mesa


def gestionar_pedidos(restaurante, mesas):
    seguir = True
    while seguir:
        numero_mesa = elegir_mesa_ocupada(mesas)
        if numero_mesa is None:
            seguir = False
        else:
            mesa = buscar_mesa(mesas, numero_mesa)
            posicion = mesas.index(mesa)
            mesas[posicion] = tomar_pedido(restaurante, mesa)
    return mesas


def pedir_precio():
    texto = input("Precio (€): ")
    try:
        precio = float(texto.replace(",", "."))
    except ValueError:
        print("Error: el precio debe ser un número.")
        return None
    if precio <= 0:
        print("Error: el precio debe ser mayor que 0.")
        return None
    return precio


def ampliar_menu_cli(restaurante, ruta_restaurante):
    nombre_plato = input("Nombre del plato: ").strip()
    if nombre_plato == "":
        print("Error: el nombre no puede estar vacío.")
        return restaurante
    if nombre_plato in restaurante["menu"]:
        print("Aviso: ese plato ya existe; se actualizará su precio.")
    precio = pedir_precio()
    if precio is None:
        return restaurante
    restaurante = ampliar_menu(restaurante, nombre_plato, precio, ruta_restaurante)
    print("Menú actualizado:", nombre_plato, "-", precio, "€")
    return restaurante


def main():
    restaurante = None
    ruta_restaurante = None
    mesas = []
    recaudacion = 0
    ventas_platos = {}
    salir = False

    while not salir:
        mostrar_menu()
        opcion = pedir_opcion()
        if opcion is None:
            continue

        if opcion == 7:
            if restaurante is not None:
                mostrar_resumen_ventas(ventas_platos, recaudacion)
            print("Hasta luego")
            salir = True
        elif opcion == 1:
            nuevo, nueva_ruta = cargar_datos_restaurante()
            if nuevo is not None:
                restaurante = nuevo
                ruta_restaurante = nueva_ruta
                mesas = []
                recaudacion = 0
                ventas_platos = {}
                print("Restaurante cargado:", restaurante["nombre"])
        elif restaurante is None:
            print("Primero tienes que cargar un restaurante (opción 1).")
        elif opcion == 2:
            mesas = cargar_y_sentar_grupos(restaurante, mesas)
        elif opcion == 3:
            mesas = gestionar_pedidos(restaurante, mesas)
        elif opcion == 4:
            numero_mesa = elegir_mesa_a_cobrar(mesas)
            if numero_mesa is not None:
                mesa = buscar_mesa(mesas, numero_mesa)
                ventas_platos = registrar_ventas(ventas_platos, mesa["pedido"])
                mesas, recaudacion = cobrar_mesa(mesas, numero_mesa, recaudacion)
        elif opcion == 5:
            restaurante = ampliar_menu_cli(restaurante, ruta_restaurante)
        elif opcion == 6:
            consultar_estado(restaurante, mesas, recaudacion)
            mostrar_resumen_ventas(ventas_platos, recaudacion)


if __name__ == "__main__":
    main()