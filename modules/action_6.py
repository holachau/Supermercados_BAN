import sys
sys.path.append('./lib')
sys.path.append('./utils')
from productos import findByCodigo

# Cantidad de stock de un producto
def stock():
    print('Introduzca el codigo del producto que desea ver el stock: ')
    
    producto = findByCodigo(input('~~>'))
    
    print()
    print(producto["nombre"])
    print()
    print('STOCK ', producto['stock'])
    print()

    return ''