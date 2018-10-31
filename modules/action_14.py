
import sys
sys.path.append('./lib')
from productos import getProductos
sys.path.append('./lib')
from categorias import getCategorias

#El usuario solicita poder determinar el producto más vendido dependiendo del tipo de producto.

def masvendido_segunclase ():
    efe = getCategorias()
    jota = getProductos()
    pedir_sigla_cat = input("¿Dentro de qué categoría? ")
    mayus = pedir_sigla_cat.upper()
    if mayus not in efe:
        print("no existe")
    else:
        listavendidosporprod = []
        mayor = 0
        nombre = ""
        for prod in jota:
            if mayus == jota[prod]["categoria"]["sigla"]:
                listavendidosporprod.append([jota[prod]["nombre"], jota[prod]["vendidos"]])
                for i in listavendidosporprod:
                    if mayor <= i[1]:
                        mayor = i[1]
                        nombre = i[0]
        print("El producto más vendido dentro de la categoria", mayus, "es", nombre, "con", mayor, "artículos vendidos")