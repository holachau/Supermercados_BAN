from datetime import datetime, date, time, timedelta

formato_fecha = "%d-%m-%Y"
fecha_inicial = datetime.strptime("01-10-2013", 
                                  formato_fecha)
fecha_final = datetime.strptime("25-12-2013", 
                                formato_fecha)
diferencia = fecha_final - fecha_inicial

print(type(fecha_final) == datetime)

formato2 = "%d-%m-%Y"
cadena2 = fecha_inicial.strftime(formato2)  
print("Fecha inicial:", cadena2)
print("Fecha final:", fecha_final)
print("Diferencia:", diferencia.days, "días")

# Asigna formato de ejemplo1
formato1 = "%a %b %d %H:%M:%S %Y"

# Asigna formato de ejemplo2
formato2 = "%d-%m-%y %I:%m %p"

hoy = datetime.today()  # Asigna fecha-hora

# Muestra fecha-hora según ISO 8601
print("Fecha en formato ISO 8601:", hoy)

# Aplica formato ejemplo1
cadena1 = hoy.strftime(formato1)  

# Aplica formato ejemplo2
cadena2 = hoy.strftime(formato2)  

# Muestra fecha-hora según ejemplo1
print("Formato1:", cadena1)

# Muestra fecha-hora según ejemplo2
print("Formato2:", cadena2)