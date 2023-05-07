from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient["pokemondb"]
pokemon_data = pokemonDB["pokemon_data"]

# Query to find all Pokemon with attack greater than 150
query_high_attack = {"attack": {"$gt": 150}}
high_attack_pokemon = pokemon_data.find(query_high_attack)
print("High attack Pokemon:")
for pokemon in high_attack_pokemon:
    print(pokemon)
