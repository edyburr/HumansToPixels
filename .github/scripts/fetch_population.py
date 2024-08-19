import requests
import json
import os

url = "https://get-population.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": "https://get-population.p.rapidapi.com/"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    population = data['body']['world_population']
    
    with open('population-data.json', 'w') as f:
        json.dump({"population": population}, f)
    print("Population data updated successfully.")
else:
    print(f"Error fetching data: {response.status_code}")
    print(response.text)
