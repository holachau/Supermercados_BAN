import sys
sys.path.append('./lib')
sys.path.append('./utils')
from productos import addProducto
from categorias import getCategoriaOpt
from date import fieldDate

def agregarProducto():
    nombre = input("Nombre del producto: ")
    codigo = input("Código del producto: ")
    stock = int(input("Cantidad stock: "))
    precioUnitario = float(input("Precio unitario: "))
    fechaVencimiento = fieldDate("fecha de vencimiento")
    categoria = None
    optCategorias = getCategoriaOpt()
    labelsCategoria = getCategoriaOpt(join=True)
    while categoria not in optCategorias:
        categoria = input("Categoría (" + labelsCategoria + "): ")
        if categoria not in optCategorias:
            print("Error, la categoria no existe")

    prod = {
        "codigo": codigo,
        "nombre": nombre,
        "stock": stock,
        "precioUnitario": precioUnitario,
        "fechaVencimiento": fechaVencimiento,
        "vendidos": 0,
        "categoria": {"sigla": categoria}
    }
    result = addProducto(prod)
    return result['msj']
