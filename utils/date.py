from datetime import datetime

formato = {
    "date": {
        "format": "%d-%m-%Y",
        "label": "dd-mm-YYYY"
    },
    "datetime": {
        "format": "%d-%m-%Y %H:%M:%S",
        "label": "dd-mm-YYYY HH:mm:ss"
    }
}

def newDate(fecha):
    try:
        return datetime.strptime(fecha, formato["date"]["format"])
    except ValueError:
        return False 

def formatDate(fecha):
    try:
        return fecha.strftime(formato["date"]["format"])  
    except AttributeError:
        return False 

def fieldDate(label):
    valido = False
    while valido == False:
        fecha = newDate(input("Ingresar " + label + " (" + formato["date"]["label"] +"): "))
        if (fecha):
            valido = True
        else:
            print("Error de formato...")
    return fecha

def newDateTime(fecha):
    try:
        return datetime.strptime(fecha, formato["datetime"]["format"])
    except ValueError:
        return False 

def formatDateTime(fecha):
    try:
        return fecha.strftime(formato["datetime"]["format"])  
    except AttributeError:
        return False 

def fieldDateTime(label):
    valido = False
    while valido == False:
        fecha = newDateTime(input("Ingresar " + label + " (" + formato["datetime"]["label"] +"): "))
        if (fecha):
            valido = True
        else:
            print("Error de formato...")
    return fecha

def now():
    return datetime.now()

#TEST
#DATE
# fecha = newDate('01-01-2008')
# print(fecha)
# print(type(fecha))
# print(formatDate(fecha))
# print(type(formatDate(fecha)))
#DATE TIME
# fecha = newDateTime('01-01-2008 22:10:1')
# print(fecha)
# print(type(fecha))
# print(formatDateTime(fecha))
# print(type(formatDateTime(fecha)))