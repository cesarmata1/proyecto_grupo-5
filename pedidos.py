import json

#Funcion para ampliar menu Punto 8
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

# Funcion de mostrar la carta del restaurnate
 
def mostrar_carta(restaurante):
    for plato, precio in restaurante["menu"].items():
        print(plato, ":", precio,"€")

# Funcion de tomar pedido a los clientes de una mesa

def tomar_pedido(restaurante,mesa):
    
    menu= restaurante["menu"]
    pedidos={}
    if mesa["estado"] == "ocupada":
        mostrar_carta(restaurante)
        for cliente in range(mesa["clientes"]):
            pedido=input("Que desean para comer?: ")
            while pedido != "Eso es todo":
                if pedido in menu.keys():
                     if pedido in pedidos:
                         pedidos[pedido]+=1
                     else:
                         pedidos[pedido]=1
                else:
                    print("Tu pedido no esta en el menu")
                pedido=input("Que otro plato deseas?: ")
        if pedidos:        
            mesa["pedido"]=pedidos
            mesa["estado"]="con_pedido"
    return mesa




    

