# cache temporaire pour stocker les résultats des requêtes de l'API PokéAPi
#pour améliorer les performances et de réduire la charge réseau
from cachetools import TTLCache, cached

# cachetools est une bibliothèque qui permet de gérer efficacement le caching en mémoire.
# TTLCache est un cache où chaque entrée expire après un certain temps (Time-To-Live).
# cached est un décorateur qui permet de mettre en cache les résultats d'une fonctio

cache = TTLCache(maxsize=100, ttl=3600)  # 100 entrées max, expiration 1h

# Ajout du cache à fetch_pokemon_data

@cached(cache)
def fetch_pokemon_data_cached(pokemon_name):
    return fetch_pokemon_data(pokemon_name)   #requête HTTP à l'API
