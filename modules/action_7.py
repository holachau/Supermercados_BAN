import sys
sys.path.append('./lib')
from productos import findByCodigo, updateProducto



#El usuario solicita poder reponer un producto cuando el stock este por debajo de un mínimo requerido.

def reponer_Stock ():
    n = input("¿Qué producto busca? ")
    analizar_stock = findByCodigo(n)
    if analizar_stock == None:
        return "El producto no existe."
    else:
        print("Cantidad total de stock: ", analizar_stock["stock"])
        preg = input("¿Desea reponer el stock? ")
        if preg == "si" or preg == "Si":
            reponer = int(input("¿Cuántos quiere agregar?"))
            analizar_stock["stock"] = analizar_stock["stock"] + reponer
            result = updateProducto(analizar_stock)
            return result["msj"]
        elif preg == "no" or preg == "No":
            return "Ok."