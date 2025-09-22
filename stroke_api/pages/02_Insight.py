import streamlit as st
import pandas as pd
import requests

st.title("Informations intéressantes sur les données AVC")

# Récupération des données depuis l'API
response = requests.get("http://127.0.0.1:8000/patients/")
data = pd.DataFrame(response.json())

if data.empty:
    st.write("Aucune donnée trouvée")
else:
    #  Statistiques générales
    st.subheader("Statistiques générales des patients")
    st.write(f"Nombre total de patients : {len(data)}")
    st.write(f"Nombre de patients avec AVC : {data['stroke'].sum()}")
    st.write(f"Pourcentage de patients avec AVC : {data['stroke'].mean()*100:.2f}%")

    #  Âge moyen des patients avec AVC
    st.subheader("Âge moyen des patients avec AVC")
    st.write(f"Âge moyen : {data[data['stroke']==1]['age'].mean():.1f} ans")

    #Facteurs de risque les plus fréquents
    st.subheader("Facteurs de risque associés à l'AVC")
    facteurs_risque = ["hypertension", "heart_disease", "ever_married", "smoking_status"]
    for facteur in facteurs_risque:
        if facteur in data.columns:
            counts = data[data['stroke']==1][facteur].value_counts()
            st.write(f"**{facteur}** :")
            st.write(counts)

    #  Combinaisons de facteurs de risque les plus fréquentes
    st.subheader("Combinaisons fréquentes de facteurs de risque chez les patients avec AVC")
    colonnes_a_verifier = ["hypertension", "heart_disease", "smoking_status"]
    if all(col in data.columns for col in colonnes_a_verifier):
        top_combinations = data[data['stroke']==1].groupby(
            colonnes_a_verifier
        ).size().sort_values(ascending=False).head(5)
        st.write(top_combinations)

    # Visualisation graphique des facteurs de risque
    st.subheader("Graphiques des facteurs de risque")
    if "hypertension" in data.columns:
        st.bar_chart(data[data['stroke']==1]["hypertension"].value_counts())
