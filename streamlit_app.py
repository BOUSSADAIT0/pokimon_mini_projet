import streamlit as st
from poke_api import get_pokemon_stats
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
