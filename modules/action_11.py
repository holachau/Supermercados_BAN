from productos import getProductos, findByCodigo, deleteProducto
from action_3 import listarProductos
from date import formatDate, newDate, now

# Simular una venta y emitir un ticket

def ticket():
    producto = ' '
    fecha = newDate(str(input('Ingrese la fecha de hoy [dd-mm-aaaa]:  ')))

    print('Introduzca el codigo del producto a vender (primeras tres letras del nombre)')
    print('Luego la cantidad de unidades')
    print('Presione ENTER para emitir el ticket')

    while producto != '':
        producto = findByCodigo(input('~~>'))
        cantidad = int(input('~~~>'))  
        precioTotal = precioTotal + ( producto["precio"] * cantidad )

    print('        SUPERMERCADOS BAN')
    print('   Capital Federal Buenos Aires')
    print()
    print('SUPBAN S.A')
    print('CUIT Nro: 45-99233219-7')
    print('Av. Callao 2406')
    print('C.A.B.A')
    print('IVA RESPONSABLE INSCRIPTO')
    print('A CONSUMIDOR FINAL')
    print(fecha)

    return()