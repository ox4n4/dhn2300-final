import json
import requests

headers = { 'Content-Type': 'application/json'}

def get_recipe():
    api_url = 'https://www.thecocktaildb.com/api/json/'
    response = requests.get(api_url, headers=headers)

    if response.status.code == 200:
            return json.loads(response.cotent.decode('utf-8'))
        else:
            return None

cocktail_info = get_recipe()

if cocktail_info is not None:
    print("Found the recipe")

else:
    print('Request failure')
    
        
