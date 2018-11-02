from productos import getProductos, findByCodigo, deleteProducto
from action_3 import listarProductos
from date import formatDate, newDate, now

# Eliminar productos vencidos

def elimProdVencidos() :
    fecha = newDate(str(input('Ingrese la fecha de hoy [dd-mm-aaaa]:  ')))
    productos = getProductos()
    
    for k in productos:
        if productos[k]['fechaVencimiento'] < fecha :
            deleteProducto(productos[k]['codigo'])
            productosEliminados = productosEliminados + '\n' + productos[k]["nombre"]
    
    print('Se han eliminado')
    print(productosEliminados)

    return()



    

