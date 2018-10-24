import json

def getProductos():
    with open('./db/productos.json') as json_file:
        results = json.load(json_file)
    return results

def productosFindByCodigo(codigo):
    with open('./db/productos.json') as json_file:
        results = json.load(json_file)
        data = None
        if results.__contains__(codigo):
            data = results[codigo]
        return data

def addProducto(obj):
    with open('./db/productos.json') as json_file:
        results = json.load(json_file)
        results[obj["codigo"]] = obj
        with open('./db/productos.json', 'w') as outfile:  
            json.dump(results, outfile)        

def updateProducto(obj):
    with open('./db/productos.json') as json_file:
        results = json.load(json_file)
        results[obj["codigo"]] = obj
        with open('./db/productos.json', 'w') as outfile:  
            json.dump(results, outfile)  

def deleteProducto(key):
    try:
        with open('./db/productos.json') as json_file:
            results = json.load(json_file)
            nombre = results[key]['nombre']
            results.pop(key)
            with open('./db/productos.json', 'w') as outfile:  
                json.dump(results, outfile)            
                return 'El producto '+ nombre + ' ha sido eliminado'
    except Exception:
        return 'Ha ocurrido un error borrando el producto, no existe ese producto'
