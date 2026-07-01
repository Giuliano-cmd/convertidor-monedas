#Importar librerias
import requests


url = "https://api.bcra.gob.ar/"

def precioUSD():
    r = requests.get(url + 'estadisticascambiarias/v1.0/Cotizaciones/USD')
    x = r.json()
    fecha = x['results'][0]['fecha']
    cotizacion = x['results'][0]['detalle'][0]['tipoCotizacion']
    
    #resultado = json.loads(x)
    #print(resultado)
    return fecha, cotizacion