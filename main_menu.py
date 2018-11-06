import sys
sys.path.append('./modules')

from action_1 import agregarProducto
from action_2 import eliminarProducto
from action_3 import listarProductos
from action_4 import newStock
from action_5 import updatePrecio
from action_6 import stock
from action_7 import reponer_Stock
from action_8 import envio
from action_9 import masvendido
from action_10 import elimProdVencidos
from action_11 import ticket
from action_12 import agregarDesc
from action_13 import DescVenc
from action_14 import masvendido_segunclase
from action_15 import agregarCategoria



print()
print('~ ~ ~ B I E N V E N I D O ~ ~ ~')
print()

def takeDecision(value, operation):
    return operation[value]()

decision = {
    "1": agregarProducto,
    "2": eliminarProducto,
    "3": listarProductos,
    "4": newStock,
    "5": updatePrecio,
    "6": stock,
    "7": reponer_Stock,
    "8": envio,
    "9": masvendido,
    "10": elimProdVencidos,
    "11": ticket,
    "12": agregarDesc,
    "13": DescVenc,
    "14": masvendido_segunclase,
    "15": agregarCategoria
}

while True:
    print('///////////////////////////////////////////////////////////////////////////')
    print('// (1)  Agregar un nuevo producto                                        //')
    print('// (2)  Eliminar un producto introduciendo su codigo                     //')
    print('// (3)  Listar los productos en stock                                    //')
    print('// (4)  Actualizar stock de un producto tras una venta                   //')
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
    print('// (15) Crear una nueva categoria                                        //')
    print('///////////////////////////////////////////////////////////////////////////')
    print()
    action = input("Ingrese numero de operacion que desea realizar: ")
    print()

    print(takeDecision(action, decision))

                                                                                



