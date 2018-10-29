import sys
sys.path.insert(0, './lib')
from productos import findByCodigo, updateProducto


def newStock():
    n = input("¿Qué producto busca? ")
    m = int(input("¿Cuántos se vendieron? "))
    analizar_stock = findByCodigo(n)
    if analizar_stock == False:
        return "El objeto no existe"
    analizar_stock["stock"] -= m
    updateProducto(analizar_stock)
    print("Lista actualizada.")
