import sys
sys.path.insert(0, '../lib')
from productos import deleteProducto

def eliminarProducto() :
    codigoAEliminar = input('Ingrese codigo del producto que desea eliminar: ')
    print()

    print(deleteProducto(codigoAEliminar))
    
    return None