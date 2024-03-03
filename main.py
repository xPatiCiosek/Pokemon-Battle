import requests
import random
import json

# Define the URL of the API endpoint you want to access
url = 'https://api.pokemontcg.io/v2/cards/{}-{}'


sword_shield = 'swsh4'
page = random.randint(1,12)
id = random.randint(1,215)
pokemon = url.format(sword_shield,id)
# print(url)
# cards where set series equals to sword and shield (ability to sort by series)
series_url = 'https://api.pokemontcg.io/v2/cards?q=set.series:sword & shield'

pokedex_url = 'https://api.pokemontcg.io/v2/cards?q=nationalPokedexNumbers:{}'
pokedex_num = random.randint(1,1008)
random_by_pokedex_url = pokedex_url.format(pokedex_num)
# Define your API key
api_key = '2021ebc1-08a8-4d78-8c7a-647e50a6b77e'

# Define the headers with the X-Api-Key header
headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json'  # You can add other headers if necessary
}

# Send a GET request with the defined headers
response = requests.get(random_by_pokedex_url, headers=headers)

# Process the response
# if response.status_code == 200:
#     # If the request was successful (status code 200)
#     print('Response:', response.json())
# else:
#     # If there was an error with the request
#     print('Error:', response.status_code)


print(response[0])    



  
