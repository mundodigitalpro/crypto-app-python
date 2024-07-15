import requests
from datetime import datetime

BASE_URL = "https://api.coincap.io/v2"

def obtener_info_criptomoneda(id_cripto):
    """
    Obtiene información detallada sobre una criptomoneda.
    
    :param id_cripto: ID de la criptomoneda en CoinCap (ej. 'bitcoin', 'ethereum')
    :return: Diccionario con información de la criptomoneda o None si hay un error
    """
    url = f"{BASE_URL}/assets/{id_cripto}"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()['data']
    except requests.RequestException as e:
        print(f"Error al obtener información: {e}")
        return None

def mostrar_info_criptomoneda(info):
    """
    Muestra información detallada sobre una criptomoneda.
    
    :param info: Diccionario con información de la criptomoneda
    """
    if info is None:
        print("No se pudo obtener la información.")
        return
    
    precio = float(info['priceUsd'])
    cap_mercado = float(info['marketCapUsd'])
    volumen_24h = float(info['volumeUsd24Hr'])
    cambio_24h = float(info['changePercent24Hr'])
    
    print(f"\nInformación de {info['name']} ({info['symbol']}):")
    print(f"Ranking: #{info['rank']}")
    print(f"Precio actual: ${precio:.2f}")
    print(f"Capitalización de mercado: ${cap_mercado:,.0f}")
    print(f"Volumen en 24h: ${volumen_24h:,.0f}")
    print(f"Cambio de precio en 24h: {cambio_24h:.2f}%")
    print(f"Oferta circulante: {float(info['supply']):,.0f} {info['symbol']}")
    print(f"Oferta máxima: {float(info['maxSupply']):,.0f} {info['symbol']}" if info['maxSupply'] else "Oferta máxima: No especificada")

def obtener_top_criptomonedas(limite=10):
    """
    Obtiene las principales criptomonedas por capitalización de mercado.
    
    :param limite: Número de criptomonedas a obtener (por defecto 10)
    :return: Lista de diccionarios con información de las criptomonedas o None si hay un error
    """
    url = f"{BASE_URL}/assets"
    parametros = {'limit': limite}
    
    try:
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()
        return respuesta.json()['data']
    except requests.RequestException as e:
        print(f"Error al obtener las principales criptomonedas: {e}")
        return None

def mostrar_top_criptomonedas(top_criptos):
    """
    Muestra una lista de las principales criptomonedas.
    
    :param top_criptos: Lista de diccionarios con información de las criptomonedas
    """
    if top_criptos is None:
        print("No se pudo obtener la lista de criptomonedas.")
        return
    
    print("\nTop Criptomonedas por Capitalización de Mercado:")
    for cripto in top_criptos:
        precio = float(cripto['priceUsd'])
        cap_mercado = float(cripto['marketCapUsd'])
        print(f"{cripto['rank']}. {cripto['name']} ({cripto['symbol']}): ${precio:.2f} - Cap. Mercado: ${cap_mercado:,.0f}")

def main():
    print("Bienvenido a la aplicación de información de criptomonedas")
    
    while True:
        print("\nOpciones:")
        print("1. Ver información detallada de una criptomoneda")
        print("2. Ver top 10 criptomonedas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            id_cripto = input("Ingrese el ID de una criptomoneda (ej. 'bitcoin', 'ethereum'): ").lower()
            info = obtener_info_criptomoneda(id_cripto)
            mostrar_info_criptomoneda(info)
        elif opcion == '2':
            top_criptos = obtener_top_criptomonedas()
            mostrar_top_criptomonedas(top_criptos)
        elif opcion == '3':
            print("¡Gracias por usar la aplicación!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()