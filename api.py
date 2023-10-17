import bs4
import requests

query = '192.168.1.138'
response = requests.get(f"http://ip-api.com/json/{query}")
data = response.json()

if data["status"] == "fail":
    print("Такого IP не существует")
else:
    print(data["country"])