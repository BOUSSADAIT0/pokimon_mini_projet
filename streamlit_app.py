# import streamlit as st
# from poke_api import get_pokemon_stats , get_type_stats
# from battle import battle

# st.title("Comparaison et Combat de Pokémon")

# # Entrer les noms des Pokémon
# pokemon1 = st.text_input("Entrez le premier Pokémon:")
# pokemon2 = st.text_input("Entrez le second Pokémon:")

# # Vérifier que les deux Pokémon sont saisis
# if pokemon1 and pokemon2:
#     # Récupérer les statistiques des Pokémon
#     stats1 = get_pokemon_stats(pokemon1)
#     stats2 = get_pokemon_stats(pokemon2)

#     # Vérifier si les données existent
#     if stats1 and stats2:
#         # Afficher les statistiques des deux Pokémon
#         col1, col2 = st.columns(2)

#         with col1:
#             st.subheader(f"{pokemon1.capitalize()} 🟦")
#             st.write(stats1)

#         with col2:
#             st.subheader(f"{pokemon2.capitalize()} 🟥")
#             st.write(stats2)

#         # Comparaison des statistiques
#         winner_hp = pokemon1 if stats1["hp"] > stats2["hp"] else pokemon2
#         winner_attack = pokemon1 if stats1["attack"] > stats2["attack"] else pokemon2

#         st.write("### Résultats de la comparaison :")
#         st.success(f"🥇 **{winner_hp.capitalize()}** a plus de PV.")
#         st.success(f"⚔ **{winner_attack.capitalize()}** a une meilleure attaque.")

#         # Bouton pour simuler un combat
#         if st.button("⚔ Simuler un combat de 5 rounds ⚔"):
#             winner = battle(pokemon1, pokemon2)
#             st.write("### 🏆 Résultat du Combat 🏆")
#             st.success(f"🎉 **{winner.capitalize()} remporte le combat après 5 rounds !** 🎉")

#     else:
#         st.error("Impossible de récupérer les statistiques. Vérifiez les noms des Pokémon.")

import streamlit as st
from poke_api import get_pokemon_stats, get_type_stats
from battle import battle

st.title("Comparaison et Combat de Pokémon")

# Entrer les noms des Pokémon
pokemon1 = st.text_input("Entrez le premier Pokémon:")
pokemon2 = st.text_input("Entrez le second Pokémon:")

# Vérifier que les deux Pokémon sont saisis
if pokemon1 and pokemon2:
    # Récupérer les statistiques des Pokémon
    stats1 = get_pokemon_stats(pokemon1)
    stats2 = get_pokemon_stats(pokemon2)

    # Vérifier si les données existent
    if stats1 and stats2:
        # Afficher les statistiques des deux Pokémon
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"{pokemon1.capitalize()} 🟦")
            st.write(stats1)

        with col2:
            st.subheader(f"{pokemon2.capitalize()} 🟥")
            st.write(stats2)

        # Comparaison des statistiques
        winner_hp = pokemon1 if stats1["hp"] > stats2["hp"] else pokemon2
        winner_attack = pokemon1 if stats1["attack"] > stats2["attack"] else pokemon2

        st.write("### Résultats de la comparaison :")
        st.success(f"🥇 **{winner_hp.capitalize()}** a plus de PV.")
        st.success(f"⚔ **{winner_attack.capitalize()}** a une meilleure attaque.")

        # Bouton pour simuler un combat
        if st.button("⚔ Simuler un combat de 5 rounds ⚔"):
            winner = battle(pokemon1, pokemon2)
            st.write("### 🏆 Résultat du Combat 🏆")
            st.success(f"🎉 **{winner.capitalize()} remporte le combat après 5 rounds !** 🎉")

    else:
        st.error("Impossible de récupérer les statistiques. Vérifiez les noms des Pokémon.")

# Menu déroulant pour choisir un type de Pokémon
type_options = [
    "normal", "fire", "water", "grass", "electric", "psychic", "ice", "dragon", 
    "dark", "fairy", "bug", "fighting", "ghost", "rock", "ground", "steel", "poison", "flying"
]

selected_type = st.selectbox("Choisissez un type de Pokémon:", type_options)

if selected_type:
    # Affichage du message avant de récupérer les statistiques du type
    st.write(f"Affichage des statistiques pour le type **{selected_type.capitalize()}**...")
    
    # Appel de la fonction get_type_stats pour obtenir les informations sur le type
    
    st.success(f" **{get_type_stats(selected_type)} cest la moyenne des HP !** ")
