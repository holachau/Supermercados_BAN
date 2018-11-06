import sys
sys.path.append('./lib')
from productos import findByCodigo, updateProducto
sys.path.append('./utils')
from questions import qYesNo


def agregarDesc ():
    julio = input("¿Qué producto busca? ")
    prod = findByCodigo(julio)
    if prod == None:
        return "No existe el producto"
    preg = qYesNo("¿Tiene Descuento?")
    if preg == False:
        prod["descuento"] = 0
        return "El producto no tiene descuento"
    else: 
        descuento1 = int(input("¿De cuánto es el descuento? "))
        prod["descuento"] = descuento1 / 100
        result = updateProducto(prod)
        return result["msj"]