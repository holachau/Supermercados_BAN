import sys
sys.path.append('./lib')
sys.path.append('./utils')
from productos import findByCodigo, updateProducto
from envios import addEnvio
from date import now

#El usuario solicita poder hacer envios a domicilio. Pedir los datos de un cliente para hacer envío a domicilio.
def envio():
    prod = input("Ingresar código del producto: ")
    producto = findByCodigo(prod)
    if producto == None:
        return "El producto no existe."
    else:
        cantidad = int(input("¿Cuántos va a llevar? "))
        if producto["stock"] < cantidad:
            return "Error, no hay tantos."
        else:
            precio_tot = cantidad * producto["precioUnitario"]
            print("El precio total es:", precio_tot)
            producto["stock"] -= cantidad
            producto["vendidos"] += cantidad
            result = updateProducto(producto)
            if (result["status"]):
                continuar = input("¿Va a llevarlo online? si/no")
                if continuar == "n" or continuar == "no" or continuar == "No":
                    print("Ok.")
                elif continuar == "s" or continuar == "si" or continuar == "Si":

                    print("Por favor, verífiquenos su información.")
                    direccion = input("Domicilio: ")
                    telefono = input("Teléfono: ")
                    nombre = input("Nombre: ")
                    envio = addEnvio({
                        "producto": {"codigo": producto["codigo"]},
                        "nombre": nombre,
                        "telefono": telefono,
                        "direccion": direccion,
                        "fecha": now()
                    })
                    return envio["msj"]
            else:
                return result["msj"]
