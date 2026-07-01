from funciones_api.BCRA_API import precioUSD
from base_de_datos.BDD import crearBDD
import os


def main():
    salida = ""
    while salida != "0":
        limpiar_pantalla()
        print("Convertidor de moneda (USD->ARS o ARS->USD)")
        print("1- Ver cotizacion de USD")
        print("2- Convertir ARS a USD")
        print("3- Convertir USD a ARS")
        salida = input("Ingrese opcion (0 salida): ")
        if salida == '1':
            limpiar_pantalla()
            fecha, cotizacion = precioUSD()
            print(f"Fecha: {fecha}")
            print(f"Cotizacion: {cotizacion}")
            input("Presione enter para volver")
        elif salida == '2':
            limpiar_pantalla()
            fecha, cotizacion = precioUSD()
            monto = int(input("Ingrese monto en ARS: "))
            total = str(convertirARS(monto, cotizacion))
            print(f"Fecha cotizacion USD: {fecha}")
            print(f"Cotizacion USD: {cotizacion}")
            print(f"Cantidad de ARS: {monto}")
            print(f"Cantidad de USD: {total}")
            input("Presione enter para volver")
        elif salida == '3':
            limpiar_pantalla()
            fecha, cotizacion = precioUSD()
            monto = int(input("Ingrese monto en USD: "))
            total = str(convertirUSD(monto, cotizacion))
            print(f"Fecha cotizacion USD: {fecha}")
            print(f"Cotizacion USD: {cotizacion}")
            print(f"Cantidad de USD: {monto}")
            print(f"Cantidad de ARS: {total}")
            input("Presione enter para volver")
        elif salida == "0":
            exit()

def convertirARS(m, c) -> float:
    cantUSD = m/c
    return cantUSD

def convertirUSD(m, c) -> float:
    cantARS = m*c
    return cantARS

def limpiar_pantalla():
    # 'cls' para Windows, 'clear' para macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    crearBDD()
    main()