import sys
sys.path.append('./lib')
from productos import addProducto


def agregarProducto():
    codigo = input("Código del producto: ")

    nombre = input("Nombre del producto: ")

    stock = int(input("Cantidad stock: "))

    precioUnitario = float(input("Precio unitario: "))

    fechaVencimiento = input("Fecha vencimiento: ")

    tipoProducto = input("Tipo de producto: ")

    prod = {
        "codigo": codigo,
        "nombre": nombre,
        "stock": stock,
        "precioUnitario": precioUnitario,
        "fechaVencimiento": fechaVencimiento,
        "tipoProducto": tipoProducto
    }

    return addProducto(prod)
