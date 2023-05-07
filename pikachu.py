from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient["pokemondb"]
pokemon_data = pokemonDB["pokemon_data"]

# Query to find all Pokemon named "Pikachu"
query_pikachu = {"name": "Pikachu"}
pikachus = pokemon_data.find(query_pikachu)
print("Pikachus:")
for pikachu in pikachus:
    print(pikachu)
