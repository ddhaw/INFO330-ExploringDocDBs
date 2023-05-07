from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient["pokemondb"]
pokemon_data = pokemonDB["pokemon_data"]

# Query to find all Pokemon with ability of "Overgrow"
query_ability = "Overgrow"
query_overgrow = {"abilities": {"$regex": f".*{query_ability}.*"}}
overgrow_pokemon = pokemon_data.find(query_overgrow)
print("Overgrow ability:")
for pokemon in overgrow_pokemon:
    print(pokemon)
