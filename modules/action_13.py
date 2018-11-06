import sys
sys.path.append('./lib')
sys.path.append('./utils')
from productos import getProductos, updateProducto
from date import now, addDays, formatDate
import datetime

def DescVenc():
    prods = getProductos()
    fecha = now()
    end_date = addDays(fecha, 7)
    for i in prods:
        if prods[i]["fechaVencimiento"] < fecha:
            print(prods[i]["nombre"],"ha expirado.")
        else:
            if prods[i]["fechaVencimiento"] >= fecha and prods[i]["fechaVencimiento"] <= end_date and prods[i]["descuento"] == 0.0:
                prods[i]["descuento"] = 0.10
                updateProducto(prods[i])
                print(prods[i]["nombre"],"se actualizó")
            else:
                print(prods[i]["nombre"],"no necesita descuento")
    print("La lista ha sido actualizada")
