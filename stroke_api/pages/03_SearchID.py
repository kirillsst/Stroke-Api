import streamlit as st
import pandas as pd
import requests

st.title("Recherche par ID patient")

# Champ pour entrer l'ID
patient_id = st.text_input("Entrez l'ID du patient")

if st.button("Rechercher"):
    if not patient_id.isdigit():
        st.warning("Veuillez entrer un ID valide")
    else:
        # Requête à l'API pour récupérer le patient par ID
        response = requests.get(f"http://127.0.0.1:8000/patients/{patient_id}")
        
        if response.status_code == 404:
            st.info("Patient non trouvé")
        elif response.status_code != 200:
            st.error("Erreur lors de la récupération des données")
        else:
            patient_data = response.json()
            # Convertir en DataFrame pour l'affichage
            df = pd.DataFrame([patient_data])
            st.subheader(f"Informations pour le patient ID {patient_id}")
            st.dataframe(df)
            
            if "stroke" in df.columns:
                st.subheader("Statut AVC")
                st.write(df["stroke"].value_counts())
