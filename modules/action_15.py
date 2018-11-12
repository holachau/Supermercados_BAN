import sys
sys.path.append('./lib')
sys.path.append('./utils')
from categorias import addCategoria

# Crear una nueva categoria
def agregarCategoria(): 
    print()
    nombre = str(input('Ingrese el nombre de la categoria: '))
    nombre.upper()
    sigla = str(input('Ingrese la sigla de la categoria: '))
    categoria = {
        "sigla": sigla,
        "nombre": nombre
    }
    result = addCategoria(categoria)
    print()
    return result["msj"]