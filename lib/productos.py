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
            results.pop("apellidos")
            with open('./db/productos.json', 'w') as outfile:  
                json.dump(results, outfile)            
                return True
    except Exception:
        return False
