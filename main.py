def get_pokemon_stats(pokemon_name):
    data = fetch_pokemon_data(pokemon_name)
    if data:
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
        print(f"Stats de {pokemon_name}: {stats}")
        return stats
    return None

def compare_pokemons(pokemon1, pokemon2):
    stats1 = get_pokemon_stats(pokemon1)
    stats2 = get_pokemon_stats(pokemon2)

    if stats1 and stats2:
        winner_hp = pokemon1 if stats1["hp"] > stats2["hp"] else pokemon2
        winner_attack = pokemon1 if stats1["attack"] > stats2["attack"] else pokemon2
        print(f"{winner_hp} a plus de PV.")
        print(f"{winner_attack} a une meilleure attaque.")


def get_type_stats(type_name):
    url = f"https://pokeapi.co/api/v2/type/{type_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemons = data["pokemon"]
        total_hp = 0
        count = len(pokemons)

        for p in pokemons:
            stats = get_pokemon_stats(p["pokemon"]["name"])
            if stats:
                total_hp += stats["hp"]

        avg_hp = total_hp / count if count else 0
        print(f"Nombre de Pokémon de type {type_name}: {count}")
        print(f"Moyenne des HP: {avg_hp}")


