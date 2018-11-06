import sys
sys.path.append('./lib')
from productos import getProductos

#El usuario solicita determinar cuál es el artículo más vendido.
def masvendido():
    productos = getProductos()
    listavendidos = []
    for i in productos:
        listavendidos.append([productos[i]["nombre"], productos[i]["vendidos"]])
    
    mayor = 0
    cod = ""
    for i in listavendidos:
        if mayor <= i[1]:
            mayor = i[1]
            cod = i[0]
            
    return "El producto más vendido fue", cod, "con", mayor, "productos"
