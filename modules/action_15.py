import sys
sys.path.append('./lib')
sys.path.append('./utils')
from categorias import addCategoria

# Crear una nueva categoria
def newCategoria(): 
    print()
    nombre = str(input('Ingrese el nombre'))
    sigla = str(input('Ingrese la sigla de la categoria: '))

    categoria = {
        "sigla": sigla,
    "nombre": nombre
    }

    result = addCategoria(categoria)

    print()
    print(result["msj"])

    return ''