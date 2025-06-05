import requests

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    "http://localhost:8080/engine-rest/process-definition/key/order-process/start",
    headers=headers,
    json={}  # Tu peux aussi ajouter des variables ici si besoin
)

print(response.json())
