import json
import requests

headers = { 'Content-Type': 'application/json'}

def get_cocktail():
    api_url_base = 'https://www.thecocktaildb.com/api/json/v2/9973553/popular.php'
    api_token = '9973553'
    response = requests.get(api_url, headers=headers)

    if response.status.code == 200:
            return json.loads(response.cotent.decode('utf-8'))
        else:
            return None

cocktail_info = get_recipe()

if cocktail_info is not None:
    print("Found the recipe for popular drink")
    for cocktail in cocktail_info.items():
        print(cocktail)

else:
    print('Request failure')
    
        
