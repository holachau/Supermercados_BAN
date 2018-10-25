import sys
sys.path.insert(0, './utils')
import json
from rw import read, write

def getCategorias():
    results = read('categorias')
    return results

def findBySigla(sigla):
    results = read('categorias')
    data = None
    if results.__contains__(sigla):
        data = results[sigla]
    return data

def addCategoria(obj):
    data = findBySigla(obj['sigla'])
    if (data == None):
        results = read('categorias')
        results[obj['sigla']] = obj
        write('categorias', results)
        return {'status': True, 'msj': 'La Categoria se ha agregado correctamente'}
    else:
        return {'status': False, 'msj': 'La Categoria ya existe'}

def updateCategoria(obj):
    data = findBySigla(obj['sigla'])
    if (data != None):
        results = read('categorias')
        results[obj['sigla']] = obj
        write('categorias', results)
        return {'status': True, 'msj': 'La Categoria se ha modificado correctamente'} 
    else:
        return {'status': False, 'msj': 'La Categoria no se encuentra'}

def deleteCategoria(key):
    data = findBySigla(key)
    if (data != None):
        results = read('categorias')
        results.pop(key)
        write('categorias', results)
        return {'status': True, 'msj': 'La Categoria se ha eliminado correctamente'}
    else:
        return {'status': False, 'msj': 'La Categoria no se encuentra'}

#TEST
# print(getCategorias()) #Obtengo todos los elementos
# print(findBySigla('V')) #Busco elemento por su sigla
# print(addCategoria({'nombre': 'Cocina', 'sigla': 'CO'})) #Agrego un nuevo elemento
# print(updateCategoria({'nombre': 'Cochera', 'sigla': 'CO'})) #Modifico un elemento
# print(updateCategoria('CO')) #Elimino un elemento