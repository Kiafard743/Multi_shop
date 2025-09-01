import requests

url = "https://api.tetherland.com/v1/tether/rate"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)
data = response.json()

print(data)
