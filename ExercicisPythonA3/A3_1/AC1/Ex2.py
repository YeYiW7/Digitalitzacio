import requests


# URL amb el paràmetre integrat
url = "https://api.chucknorris.io/jokes/random?category=food"


response = requests.get(url)


if response.status_code == 200:
    print("✅ Èxit!")
    print(response.text)
else:
    print(f"❌ Error {response.status_code}")

#METODE B
import requests


url = "https://api.chucknorris.io/jokes/random"
# Els paràmetres (Query params) es passen com un diccionari
params = {"category": "food"}


response = requests.get(url, params=params)


# La propietat response.url mostra la URL final generada
print(response.url)
print("✅ Resposta JSON:")
# response.json() converteix el cos de la resposta (Body) en un diccionari Python
print(response.json())

