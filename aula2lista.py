import requests
import json

lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)
print(lista)
