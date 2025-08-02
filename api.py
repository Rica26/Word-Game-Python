import requests

def buscar_palavra():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    palavra = response.json()[0].lower()
    return palavra