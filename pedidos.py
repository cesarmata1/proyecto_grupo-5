import json
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
        else:
            print("No es posible ese precio")
    with open("restaurante.json", "w", encoding="utf-8") as archivo:
        json.dump(restaurante, archivo, indent=4, ensure_ascii=False)

    return restaurante

