def agregarProducto(prod):
    print("pone muchos datos")
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    stock = int(input("Cantidad stock: "))
    precioUnitario = float(input("Precio unitario: "))
    fechaVencimiento = input("Fecha vencimiento: ")
    tipoProducto = input("Tipo de producto: ")
    prod[codigo] = {
        "código": codigo,
        "nombre":nombre,
        "stock": stock,
        "precioUnitario": precioUnitario,
        "fechaVencimiento": fechaVencimiento,
        "tipoProducto": tipoProducto
    }
    return prod