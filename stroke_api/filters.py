from typing import Optional
import pandas as pd


# Chargement des données (une fois)
stroke_data_df = pd.read_parquet("~/stroke-api/fichier_parquet.parquet")
# Tester l'app avec :
# poetry run fastapi dev stroke_api/main.py
# http://127.0.0.1:8000/docs : utiliser la fonctionnalité Try it out pour tester les routes

# Ajout des fonctions de filtrage des données cf notebook 1
# Ensuite faire appel à ces fonctions dans le fichier api.py où sont définies les routes.
# Ajouter les fonctions de filtrage pour les autres routes.
# fonction avec ajout de paramètres par défault et de type

def filter_patient(stroke: Optional[int] = None,  max_age: Optional[int] = None, gender: Optional[str] = None) -> list[dict]:
    
    df = stroke_data_df.copy()
    
    if stroke is not None:
        df = df[df["stroke"] == stroke]
    
    if max_age is not None:
        df = df[df["age"] <= max_age]
    

    df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    if gender is not None:
        df = df[df["gender"] == gender.lower()]
    
    return df.to_dict('records')

def get_id(patient_id: int):

    df = stroke_data_df.copy()

    result = df[df["id"] == patient_id]

    if result.empty:
        return None
    else:
        return result.to_dict(orient="records")[0]  # retourne un seul patient
    
def statistic():
    return stroke_data_df.copy()
#Renvoie une copie du DataFrame pour les statistiques.