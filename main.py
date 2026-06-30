import requests
import os


def main():
    salida = ""
    while salida != "0":
        limpiar_pantalla()
        print("Convertidor de moneda (USD->ARS)")
        print("1- Ver cotizacion de USD")
        salida = input("Ingrese opcion: ")
        if salida == '1':
            limpiar_pantalla()
            r = requests.get('https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Cotizaciones/USD')
            x = r.json()
            print(x['results'][0]['detalle'][0]['tipoCotizacion'])
            
            #resultado = json.loads(x)
            #print(resultado)

            input("Presione enter para volver")


def limpiar_pantalla():
    # 'cls' para Windows, 'clear' para macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')





if __name__ == "__main__":
    main()