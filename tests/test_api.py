import requests

def test_api():
    url = 'https://auto.ru/'
    response = requests.get(url)

    print(response.status_code, 'status_code')
    print(response.headers, 'headers')
    print(response.cookies, 'cookies')


def test_api_get():
    url = 'https://auto.ru/'
    query = {'search_query': 'Haval'}
    response = requests.get(url, params=query)

    print(response.headers, 'headers')
    print(response.status_code, 'status_code')
    print(response.url, 'url')

    print(response.json(), 'json')

