import requests


def fetch_data(endpoint):
    response = requests.get(
        f"https://rickandmortyapi.com/api/{endpoint}")

    if response.status_code == 200:
        return response.json()
    else:
        return None


characters = fetch_data("character")

if characters:
    print(characters)
else:
    print('Failed to fetch data')
