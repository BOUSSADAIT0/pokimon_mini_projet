from poke_api import get_pokemon_stats

def battle(pokemon1, pokemon2):
    stats1 = get_pokemon_stats(pokemon1)
    stats2 = get_pokemon_stats(pokemon2)

    if stats1 and stats2:
        dmg1 = stats1["attack"] * 5
        dmg2 = stats2["attack"] * 5

        winner = pokemon1 if dmg1 > dmg2 else pokemon2
        print(f"Combat terminé ! {winner} gagne après 5 tours.")
        return winner
