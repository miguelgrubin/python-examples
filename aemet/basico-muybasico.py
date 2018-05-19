import json
import http.client
import ssl

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2, depth=6)

api_base = 'https://opendata.aemet.es'
api_key = ''


def feed_municipio_diaria(codmunicipio):
    headers = {
        'cache-control': "no-cache"
    }
    conn = http.client.HTTPSConnection("opendata.aemet.es")
    context = ssl._create_unverified_context()
    api_url = "".join([
        '/opendata/api/prediccion/especifica/municipio/diaria/',
        str(codmunicipio), '/?api_key=', api_key
    ])
    print(api_url)
    conn.request('GET', api_url, headers=headers, context=context)
    api_res = conn.getresponse()
    data = json.loads(api_res.read())
    response = False
    if data['estado'] == 200:
        response = True
        # response = requests.get(data['datos'], headers=headers)
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
