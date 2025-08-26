import streamlit as st
import pandas as pd
import requests

st.title("Tableau de bord des données AVC")

# Filtres principaux
gender = st.selectbox("Sexe", ["tous", "Male", "Female"])
min_age = st.number_input("Âge minimum", 0, 120, 0)
max_age = st.number_input("Âge maximum", 0, 120, 120)
stroke = st.selectbox("AVC", ["tous", 0, 1])
hypertension = st.selectbox("Hypertension", ["tous", 0, 1])
heart_disease = st.selectbox("Maladie cardiaque", ["tous", 0, 1])
smoking_status = st.selectbox("Statut tabagique", ["tous", "never smoked", "formerly smoked", "smokes"])
ever_married = st.selectbox("Marié(e)", ["tous", 0, 1])

# Création des paramètres pour la requête
params = {}
if gender != "tous":
    params["gender"] = gender
if min_age > 0:
    params["min_age"] = min_age
if max_age < 120:
    params["max_age"] = max_age
if stroke != "tous":
    params["stroke"] = int(stroke)
if hypertension != "tous":
    params["hypertension"] = int(hypertension)
if heart_disease != "tous":
    params["heart_disease"] = int(heart_disease)
if smoking_status != "tous":
    params["smoking_status"] = smoking_status
if ever_married != "tous":
    params["ever_married"] = int(ever_married)

# Requête à l'API FastAPI
response = requests.get("http://127.0.0.1:8000/patients/", params=params)
data = pd.DataFrame(response.json())

st.subheader("Résultats filtrés")
st.write(f"{len(data)} patients trouvés")

if not data.empty:
    st.dataframe(data)

    # Visualisation de la distribution des âges
    st.subheader("Distribution des âges")
    st.bar_chart(data["age"])

    # Distribution par sexe
    if "gender" in data.columns:
        st.subheader("Distribution par sexe")
        st.bar_chart(data["gender"].value_counts())

    # Distribution AVC
    if "stroke" in data.columns:
        st.subheader("Nombre de patients avec AVC")
        st.bar_chart(data["stroke"].value_counts())
else:
    st.write("Aucun patient trouvé pour ce filtre.")

