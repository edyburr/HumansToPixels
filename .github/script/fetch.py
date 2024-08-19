import http.client
import json

conn = http.client.HTTPSConnection("get-population.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "66464791admshd4a0601e505d5cep1a16a9jsn031bf6389364",
    'x-rapidapi-host': "get-population.p.rapidapi.com"
}

conn.request("GET", "/population", headers=headers)

res = conn.getresponse()
data = res.read()

# Decode and parse the JSON response
parsed_data = json.loads(data.decode("utf-8"))

# Write the parsed JSON data to a file
with open('data/population.json', 'w') as f:
    json.dump(parsed_data, f, indent=2)

print("API data fetched and saved.")
