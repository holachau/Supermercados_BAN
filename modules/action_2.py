import sys
sys.path.append('./lib')
from productos import deleteProducto


def eliminarProducto() :
    codigoAEliminar = input('Ingrese codigo del producto que desea eliminar: ')
    print()

    print(deleteProducto(codigoAEliminar))
    
    return None