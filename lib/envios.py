import sys
sys.path.append('./utils')
import json
from rw import read, write
from validation import validateSchema
from date import newDateTime, formatDateTime

def getEnvios():
    results = read('envios')
    results = beforeGet(results)
    return results

def addEnvio(obj):
    valid = validateSchema(obj, 'envio')
    if (valid):
        results = read('envios')
        obj = afterSave(obj)
        results.append(obj) 
        write('envios', results)
        return {'status': True, 'msj': 'La Envio se ha agregado correctamente'}
    else:
        return {'status': False, 'msj': 'Los datos ingresados son incorrentos'}

def beforeGet(objs):
    for o in objs:
        objs[o] = beforeFindBy(objs[o])
    return objs

def beforeFindBy(obj):
    obj["fecha"] = newDateTime(obj["fecha"])
    return obj

def afterSave(obj):
    obj["fecha"] = formatDateTime(obj["fecha"])
    return obj

#TEST
# print(getEnvios()) #Obtengo todos los elementos
# print(addEnvio({  "producto": "obj",
#   "nombre": "str",
#   "telefono": "str",
#   "direccion": "str"
# }
# )) #Agrego un nuevo elemento
