import requests


def test_api():
    url = 'https://www.kpc.by/'
    response = requests.get(url)

    print(response.status_code, 'status_code')
    print(response.headers, 'headers')
    print(response.cookies, 'cookies')
    print(response.request, 'request')


def test_api_get():
    url = 'https://www.kpc.by/search'
    query = {'search_query': 'принтер'}
    response = requests.get(url, params=query)

    print(response.headers, 'headers')
    print(response.status_code, 'status_code')
    print(response.url, 'url')

    print(response.json(), 'json')
