#Importar librerias
import requests


def precioUSD():
    r = requests.get('https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Cotizaciones/USD')
    x = r.json()
    fecha = x['results'][0]['fecha']
    cotizacion = x['results'][0]['detalle'][0]['tipoCotizacion']
    
    #resultado = json.loads(x)
    #print(resultado)
    return fecha, cotizacion