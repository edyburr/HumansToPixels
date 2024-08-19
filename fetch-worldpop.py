import http.client
import json

conn = http.client.HTTPSConnection("get-population.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "RAPIDAPI_KEY",
    'x-rapidapi-host': "get-population.p.rapidapi.com"
}

conn.request("GET", "/population", headers=headers)

res = conn.getresponse()
data = res.read()

# Decode and print the JSON data
decoded_data = data.decode("utf-8")
print("Response Data:", decoded_data)

# Load the JSON data
population_data = json.loads(decoded_data)

# Prepare the JSON data to be saved
world_population = {
    "count": population_data["count"],
    "readable_format": population_data["readable_format"]
}

# Save the data to worldpop.json
with open("worldpop.json", "w") as outfile:
    json.dump(world_population, outfile, indent=4)
