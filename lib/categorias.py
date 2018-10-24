import json

def getCategorias():
    with open('./db/categorias.json') as json_file:
        results = json.load(json_file)
    return results

def categoriasFindBySigla(sigla):
    with open('./db/categorias.json') as json_file:
        results = json.load(json_file)
        data = None
        if results.__contains__(sigla):
            data = results[sigla]
        return data

def addCategoria(obj):
    with open('./db/categorias.json') as json_file:
        results = json.load(json_file)
        results[obj["sigla"]] = obj
        with open('./db/categorias.json', 'w') as outfile:  
            json.dump(results, outfile)            

def updateCategoria(obj):
    with open('./db/categorias.json') as json_file:
        results = json.load(json_file)
        results[obj["sigla"]] = obj
        with open('./db/categorias.json', 'w') as outfile:  
            json.dump(results, outfile)
        
def deleteCategoria(key):
    try:
        with open('./db/categorias.json') as json_file:
            results = json.load(json_file)
            results.pop(key)
            with open('./db/categorias.json', 'w') as outfile:  
                json.dump(results, outfile)            
                return True
    except Exception:
        return False        

