def calcular_cuenta(pedido, carta):
    total = 0
    for plato, cantidad in pedido.items():
        total = total + carta[plato] * cantidad
    return total