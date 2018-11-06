import sys
sys.path.append('./lib')
sys.path.append('./utils')
from productos import findByCodigo, updateProducto
from questions import qYesNo

def reponer_Stock ():
    n = input("¿Qué producto busca? ")
    analizar_stock = findByCodigo(n)
    if analizar_stock == None:
        return "El producto no existe."
    else:
        print("Cantidad total de stock: ", analizar_stock["stock"])
        preg = qYesNo("Desea reponer el stock")
        if preg:
            reponer = int(input("¿Cuántos quiere agregar?"))
            analizar_stock["stock"] = analizar_stock["stock"] + reponer
            result = updateProducto(analizar_stock)
            return result["msj"]
        else:
            return "Ok."
