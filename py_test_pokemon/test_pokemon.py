import requests
import json

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'content-type': 'application/json',
           'trainer_token': 'youre_token'}
TOKEN = 'youre_token'
TRAINER_ID = '149'
body_create = {
    "name": "generate",
    "photo": "generate"
}


response_create = requests.post(
    url=f'{URL}/pokemons', headers=HEADERS, json=body_create)

print(response_create.text)

response_dict = response_create.json()
pokemon_id = response_dict["id"]

body_update = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response_update = requests.post(
    url=f'{URL}/pokemons', headers=HEADERS, json=body_update)

print(response_update.text)


body_add_pokeball = {

    "pokemon_id": pokemon_id

}
response_add_pokeball = requests.post(
    url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=body_add_pokeball)

print(response_add_pokeball.text)