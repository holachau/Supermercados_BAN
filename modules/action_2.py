import sys
sys.path.append('./lib')
from productos import deleteProducto

def eliminarProducto() :
    codigo = input('Ingrese codigo del producto que desea eliminar: ')
    result = deleteProducto(codigo)

    return result["msj"]