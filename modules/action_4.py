import sys
sys.path.append('./lib')
from productos import findByCodigo, updateProducto


def newStock():
    n = input("¿Qué producto busca? ")
    analizar_stock = findByCodigo(n)
    if analizar_stock == None:
        return "El producto no existe."
    else:
        m = int(input("¿Cuántos se vendieron? "))
        
        if m > analizar_stock["stock"]:
            return "No hay tantos."
        else:
            analizar_stock["stock"] -= m
            result = updateProducto(analizar_stock)
            return result["msg"]
