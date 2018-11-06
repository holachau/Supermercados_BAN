import sys
sys.path.append('./modules')
sys.path.append('./lib')

from productos import getProductos, findByCodigo, deleteProducto
from date import formatDate, newDate, now, fieldDate

# Eliminar productos vencidos

def elimProdVencidos() :
    #fecha = newDate(str(input('Ingrese la fecha de hoy [dd-mm-aaaa]:  ')))
    fecha = now()
    productos = getProductos()
    productosEliminados = []
    for k in productos:
        if productos[k]['fechaVencimiento'] < fecha :
            productosEliminados.append(productos[k]["nombre"])
            deleteProducto(productos[k]['codigo'])
    
    print('Se han eliminado')
    print(', '.join(productosEliminados))

    return ''

    

