import sys
sys.path.insert(0, './lib')
sys.path.insert(0, './modules')

from action_1 import agregarProducto
from action_2 import eliminarProducto
from action_3 import listarProductos



print()
print('~ ~ ~ B I E N V E N I D O ~ ~ ~')
print()

def takeDecision(value, operation):
    operation[value]()
    return None

decision = {
    "1": agregarProducto,
    "2": eliminarProducto,
    "3": listarProductos
}

while True:
    print('///////////////////////////////////////////////////////////////////////////')
    print('// (1)  Agregar un nuevo producto                                        //')
    print('// (2)  Eliminar un producto introduciendo su codigo                     //')
    print('// (3)  Listar los productos en stock                                    //')
    print('// (4)  Actualiar stock de un producto                                   //')
    print('// (5)  Actualizar el precio unitario de un producto porcentualmente     //')
    print('// (6)  Cantidad de stock de un producto                                 //')
    print('// (7)  Introducir stock minimo de un producto                           //')
    print('// (8)  Conseguir el producto mas vendido                                //')
    print('// (9)  Introducir datos de un cliente para un delivery                  //')
    print('// (10) Eliminar productos vencidos                                      //')
    print('// (11) Vender un producto e imprimir ticket                             //')
    print('// (12) Agregar informacion adicional a un producto                      //')
    print('// (13) Aplicar descuentos a productos que vencen en una semana          //')
    print('// (14) Conseguir el producto mas vendido de cada categoria              //')
    print('///////////////////////////////////////////////////////////////////////////')

    print()

    action = input("Ingrese numero de operacion que desea realizar: ")
    
    takeDecision(action, decision)

                                                                                



