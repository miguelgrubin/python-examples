import requests
import urllib3

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2, depth=6)

urllib3.disable_warnings()
api_base = 'https://opendata.aemet.es/opendata/api'
api_key = ''


def feed_municipio_diaria(codmunicipio):
    headers = {
        'cache-control': "no-cache"
    }
    query = {
        'api_key': api_key
    }
    api_url = "".join([
        api_base, '/prediccion/especifica/municipio/diaria/',
        str(codmunicipio), '/'
    ])
    api_res = requests.request(
        'GET', api_url, headers=headers, params=query, verify=False
    )
    response = False
    if api_res.json()['estado'] == 200:
        api_res = requests.get(
            api_res.json()['datos'], headers=headers, verify=False
        )
        response = api_res.json()
        # save_municipio_diaria(codmunicipio, response)
    return response


def main():
    # Madrid - Madrid
    mad = feed_municipio_diaria(28079)
    pp.pprint(mad)
    # Galapagar - Madrid
    gal = feed_municipio_diaria(28061)
    pp.pprint(gal)


if __name__ == '__main__':
    main()
