from pedidos import calcular_subtotal, mostrar_carta


def buscar_mesa(mesas, numero_mesa):
    for mesa in mesas:
        if mesa["numero"] == numero_mesa:
            return mesa
    return None


def mesas_con_pedido(mesas):
    resultado = []
    for mesa in mesas:
        if mesa["estado"] == "con_pedido":
            resultado.append(mesa)
    return resultado


def elegir_mesa_a_cobrar(mesas):
    servidas = mesas_con_pedido(mesas)
    if len(servidas) == 0:
        print("No hay mesas con pedido para cobrar.")
        return None

    print("\nMesas con pedido:")
    for mesa in servidas:
        subtotal = calcular_subtotal(mesa["pedido"])
        print("  Mesa", mesa["numero"], "-", mesa["clientes"],
              "clientes -", subtotal, "€")

    texto = input("Número de mesa a cobrar: ")
    try:
        numero_mesa = int(texto)
    except ValueError:
        print("Error: escribe un número.")
        return None

    if buscar_mesa(servidas, numero_mesa) is None:
        print("Esa mesa no está disponible para cobrar.")
        return None
    return numero_mesa


def cobrar_mesa(mesas, numero_mesa, recaudacion):
    mesa = buscar_mesa(mesas, numero_mesa)
    if mesa is None or mesa["estado"] != "con_pedido":
        print("Esa mesa no se puede cobrar.")
        return mesas, recaudacion

    subtotal = calcular_subtotal(mesa["pedido"])
    recaudacion = recaudacion + subtotal
    mesas.remove(mesa)
    print("Mesa", numero_mesa, "cobrada:", subtotal, "€")
    print("Recaudación de la noche:", recaudacion, "€")
    return mesas, recaudacion


def consultar_estado(restaurante, mesas, recaudacion):
    ocupacion = 0
    for mesa in mesas:
        ocupacion = ocupacion + mesa["clientes"]

    print("\n=== ESTADO DEL RESTAURANTE ===")
    print("Restaurante:", restaurante["nombre"])
    print("Capacidad:", restaurante["capacidad"])
    print("Ocupación actual:", ocupacion, "/", restaurante["capacidad"])
    print("Mesas activas:", len(mesas), "/", restaurante["mesas_max"])
    if len(mesas) == 0:
        print("  (no hay mesas activas)")
    for mesa in mesas:
        linea = ("  Mesa " + str(mesa["numero"]) + " - "
                 + str(mesa["clientes"]) + " clientes - " + mesa["estado"])
        if mesa["estado"] == "con_pedido":
            linea = linea + " - " + str(calcular_subtotal(mesa["pedido"])) + " €"
        print(linea)
    mostrar_carta(restaurante)
    print("Recaudación de la noche:", recaudacion, "€")


def registrar_ventas(ventas_platos, pedido):
    for plato, datos in pedido.items():
        ventas_platos[plato] = ventas_platos.get(plato, 0) + datos["cantidad"]
    return ventas_platos


def plato_mas_vendido(ventas_platos):
    mejor_plato = None
    mejor_cantidad = 0
    for plato, cantidad in ventas_platos.items():
        if cantidad > mejor_cantidad:
            mejor_plato = plato
            mejor_cantidad = cantidad
    return mejor_plato, mejor_cantidad


def mostrar_resumen_ventas(ventas_platos, recaudacion):
    print("\n=== RESUMEN DE VENTAS ===")
    if len(ventas_platos) == 0:
        print("Todavía no se ha vendido ningún plato.")
        return
    for plato, cantidad in ventas_platos.items():
        print("  ", plato, ":", cantidad, "unidades")
    plato, cantidad = plato_mas_vendido(ventas_platos)
    print("Plato más vendido:", plato, "(", cantidad, "unidades )")
    print("Recaudación total:", recaudacion, "€")