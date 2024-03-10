import requests

base_url = 'https://pokeapi.co/api/v2/{}'

class Request:
    def __init__(self, endpoint):
        self.url = base_url.format(endpoint)
 
    def get_content(self):
        return requests.get(self.url).json()