import requests
import json
#endpoint = 'https://httpbin.org/anything'

auth_endpoint = 'http://127.0.0.1:8000/api/accounts/auth/'

username = 'kaan'
password = '123'

get_token = requests.post(auth_endpoint, json={'username':username, 'password': password})

if get_token.status_code == 200:
    token = get_token.json()['token']
    headers = {
        'Authorization' : f'Token {token}'
    }
    endpoint = 'http://127.0.0.1:8000/api/tasks/b7263c35-29ed-43ae-b7ec-09a02ceb5197/'
    #endpoint = 'http://127.0.0.1:8000/api/tasks/'
    get_response = requests.get(endpoint, headers=headers)

    data = get_response.json()
    for item in data:
        print(item)
    print(get_response.status_code)