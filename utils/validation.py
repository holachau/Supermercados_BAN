import sys
sys.path.append('./schemas')
from rw import schema
from datetime import date, datetime

typesMatch = {
    "str": str,
    "int": int,
    "float": float,
    "date": date,
    "datetime": datetime,
    "object": dict,
    "list": list
}

def validateSchema(obj, sch):
    valid = True
    structure = schema(sch)
    for o in obj:
        if (valid == True):
            if (structure.__contains__(o) == False): 
                valid = False
            if (type(obj[o]) != typesMatch[structure[o]]):
                print(o, structure[o])
                valid = False

    return valid
