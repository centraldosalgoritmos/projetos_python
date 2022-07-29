import requests


class PokeAPIClient:

    _BASE_URL = r'https://pokeapi.co/api/v2/pokemon/'

    @staticmethod
    def get_pokemon_data(search):
        response = requests.get(f'{PokeAPIClient._BASE_URL}{search}')
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Pokemon not found!')
