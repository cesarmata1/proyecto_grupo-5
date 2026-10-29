restaurante = {
    "nombre": "Casa Pepe",
    "capacidad": 50,
    "mesas_max": 5,
    "menu": {
        "Callos a la madrileña": 12,
        "Bocata de calamares": 5,
        "Cocido madrileño": 20
    }
}


def ampliar_menu(restaurante,pedido,precio):
    plato=restaurante["menu"]
    if pedido in plato:
        print("El plato ya existe, se modificara el precio")
        if precio > 0:
         plato[pedido]=precio
        
        else:
            print("No es posible ese precio")
    
    else:
        if precio > 0:

            plato[pedido] = precio
            print("Plato añadido")
    print(restaurante)
