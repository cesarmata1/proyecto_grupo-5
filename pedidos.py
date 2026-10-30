import json
def ampliar_menu(restaurante,nombre_plato,precio):
    plato=restaurante["menu"]
    if nombre_plato in plato:
        print("El plato ya existe, se modificara el precio")
        if precio > 0:
         plato[nombre_plato]=precio
        
        else:
            print("No es posible ese precio")
    
    else:
        if precio > 0:

            plato[nombre_plato] = precio
            print("Plato añadido")
        else:
            print("No es posible ese precio")
    with open("restaurante.json", "w", encoding="utf-8") as archivo:
        json.dump(restaurante, archivo, indent=4, ensure_ascii=False)

    return restaurante

