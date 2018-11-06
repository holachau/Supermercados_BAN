import sys
sys.path.append('./lib')
sys.path.append('./utils')
from productos import getProductos, findByCodigo, deleteProducto
from date import formatDate, newDate, now
from questions import qYesNo

# Simular una venta y emitir un ticket
def ticket():
    print('Introduzca el codigo del producto a vender (primeras tres letras del nombre)')
    print('Luego la cantidad de unidades')
    print('Presione ENTER para emitir el ticket')

    exit = False
    productos = []
    precioTotal = 0
    while exit == False:
        producto = findByCodigo(input('~~>'))
        if (producto != None):
            cantidad = int(input('~>'))
            productos.append({ 'prod': producto["nombre"], 'cant' : cantidad, 'precio' : producto["precioUnitario"]})
        r = qYesNo("Desea continuar")
        if r == False:
            exit = True
    print()
    print('            SUPERMERCADOS BAN')
    print('       Capital Federal Buenos Aires')
    print()
    print('SUPBAN S.A')
    print('CUIT Nro: 45-99233219-7')
    print('Av. Callao 2406')
    print('C.A.B.A')
    print('IVA RESPONSABLE INSCRIPTO')
    print('A CONSUMIDOR FINAL')
    print(formatDate(now()))
    print()
    
    for prod in productos:
        dot = '.' * (30 - (len(prod['prod']) + 3 + len(str(prod['cant']))))
        print(prod['prod'],' x ', str(prod['cant']), dot,  str(prod['cant'] * prod['precio']))
        precioTotal += prod['cant'] * prod['precio']

    print()
    print('TOTAL: ', precioTotal)
    print('Gracias por comprar en los Supermercados BAN !')

    return ''
