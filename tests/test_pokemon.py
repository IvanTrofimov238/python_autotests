import requests
import json

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'content-type': 'application/json',
           'trainer_token': 'youre_token'}
TOKEN = 'youre_token'
TRAINER_ID = '149'



def test_staus_code():
    response = requests.get(
        url=f'{URL}/trainers', params={'trainers': TRAINER_ID})
    assert response.status_code == 200



def test_of_response():
    response = requests.get(
        url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.json()['data'][0]['trainer_name'] == 'Ваня'