def ampliar_menu(pedido,precio):
    plato=restaurante["menu"]
    if pedido in plato:
        print("el plato ya existe, se modificara el precio")
        plato[pedido]=precio
        return
    else:
    plato[pedido] = precio
    print("Plato añadido")
    
    return restaurante

