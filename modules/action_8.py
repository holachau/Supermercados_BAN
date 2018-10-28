import sys
sys.path.append('./lib')
from productos import findByCodigo, updateProducto

#El usuario solicita poder hacer envios a domicilio. Pedir los datos de un cliente para hacer envío a domicilio.
def envio():
    prod = input("¿Qué producto desea? ")
    verif_compra = findByCodigo(prod)
    cant = int(input("¿Cuántos va a llevar? "))
    if verif_compra["stock"] > cant:
        print("Error, no hay tantos")
    else:
        precio_tot = cant * verif_compra["precioUnitario"]
        print(precio_tot)
        continuar = input("¿Va a llevarlo? ")
        if continuar == "no" or continuar == "No":
            print("Ok.")
        elif continuar == "si" or continuar == "Si":
            print("Por favor, verífiquenos su información")
            ubicacion = input("Domicilio: ")
            tel = input("Teléfono: ")
            nombre = input("Nombre: ")
