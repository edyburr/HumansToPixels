import http.client
import json

conn = http.client.HTTPSConnection("get-population.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "RAPIDAPI-KEY",
    'x-rapidapi-host': "get-population.p.rapidapi.com"
}

conn.request("GET", "/population", headers=headers)

res = conn.getresponse()
data = res.read()

# Decode and load the JSON data
decoded_data = data.decode("utf-8")
population_data = json.loads(decoded_data)

# Prepare the JSON data to be saved
world_population = {
    "count": population_data["body"]["world_population"],
    "readable_format": f"{population_data['body']['world_population']:,}"
}

# Save the data to worldpop.json
with open("worldpop.json", "w") as outfile:
    json.dump(world_population, outfile, indent=4)
