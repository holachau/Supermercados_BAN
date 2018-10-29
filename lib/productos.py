import sys
sys.path.append('./utils')
import json
from rw import read, write

def getProductos():
    results = read('productos')
    return results

def findByCodigo(codigo):
    results = read('productos')
    data = None
    if results.__contains__(codigo):
        data = results[codigo]
    return data

def addProducto(obj):
    data = findByCodigo(obj['codigo'])
    if (data == None):
        results = read('productos')
        results[obj['codigo']] = obj
        write('productos', results)    
        return {'status': True, 'msj': 'La Producto se ha agregado correctamente'}
    else:
        return {'status': False, 'msj': 'La Producto ya existe'}

def updateProducto(obj):
    data = findByCodigo(obj['codigo'])
    if (data != None):
        results = read('productos')
        results[obj['codigo']] = obj
        write('productos', results)
        return {'status': True, 'msj': 'La Producto se ha modificado correctamente'}
    else:
        return {'status': False, 'msj': 'La Producto no se encuentra'}

def deleteProducto(key):
    data = findByCodigo(key)
    if (data != None):
        results = read('productos')
        results.pop(key)
        write('productos', results)
        return {'status': True, 'msj': 'La Producto se ha eliminado correctamente'}
    else:
        return {'status': False, 'msj': 'La Producto no se encuentra'}

#TEST
# print(getProductos()) #Obtengo todos los elementos
# print(findByCodigo('V')) #Busco elemento por su codigo
# print(addProducto({'nombre': 'Cocina', 'codigo': 'CO'})) #Agrego un nuevo elemento
# print(updateProducto({'nombre': 'Cochera', 'codigo': 'CO'})) #Modifico un elemento
# print(updateProducto('CO')) #Elimino un elemento