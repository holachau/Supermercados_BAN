import sys
sys.path.append('./lib')
sys.path.append('./utils')
from productos import findByCodig, updateProducto

# Actualizar el precio unitario de un producto porcentualmente 

def updatePrecio():
    print('Introduzca el codigo del producto que desea modificar el precio: ')
    
    producto = findByCodigo(input('~~>'))
    print('Precio de ',producto['nombre'],' $',producto['precioUnitario'])
    print("Desea cambiar el precio de manera porcentual o por un numero [p/n]: ")
    print('Ej. Porcentual[ $10 por %50 = $15 ] ')
    print('Ej. Numerico[ $10 mas $5 = $15 ] ')
    action = str(input("~~> "))

    if action == 'p':
        incremento = float(input('Ingrese el porcentaje de incremento: %'))
        producto['precioUnitario'] = producto['precioUnitario'] * (1 + (incremento/100))
        producto['ultimoIncremento%'] = incremento
    
    if action == 'n':
        incremento = float(input('Ingrese el valor de incremento: $'))
        producto['precioUnitario'] = producto['precioUnitario'] + incremento
        producto['ultimoIncremento#'] = incremento
    
    result = updateProducto(producto)

    return result["msj"]
    
