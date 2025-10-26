import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()  
        return(pokemon_data)
    else:
        print(f"Error: Could not retrieve data {response.status_code}")

pokemon_name = "eevee"
get_pokemon_info(pokemon_name)
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f'Name: {pokemon_info["name"]}')
    print(f'Id: {pokemon_info["height"]}')
    print(f'Weight: {pokemon_info["weight"]}')
    print(f'Weight:{pokemon_info["id"]}')