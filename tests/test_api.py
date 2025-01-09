import requests
import pytest_check as check


def test_api1():
    url = 'https://www.kpc.by/'
    headers = {}
    response = requests.request('GET', url, headers=headers)

    print(response.status_code)

    assert response.status_code == 200
    check.equal(response.status_code, 200)



payload = {
    
}
requests.post('https://www.kpc.by/assets/components/minishop2/action.php', data='')









