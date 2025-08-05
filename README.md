Stroke data project
===================

Ce projet contient les fichiers nécessaires au brief Stroke data - Développement d'une API REST et visualisation.

============================================================================

🧹 Étapes de prétraitement des données
📥 1. Chargement des données
Les données sont chargées à partir d’un fichier CSV à l’aide de pandas.read_csv().

🧾 2. Analyse de la structure du dataset
Utilisation de :

df.info() pour visualiser le nombre de lignes, de colonnes, et les valeurs nulles.

df.dtypes pour vérifier les types de données de chaque colonne.

🧩 3. Traitement des valeurs manquantes
Identification des colonnes contenant des valeurs NaN, puis :

remplissage avec des valeurs appropriées (fillna()),

remplacement (replace()),

ou suppression des lignes ou colonnes concernées (dropna()), selon le contexte.

🔁 4. Conversion des types de données
Si certaines colonnes ont un type incorrect (ex. : nombres au format texte), elles sont converties avec astype().

🧹 5. Vérification et suppression des doublons
Détection des doublons avec df.duplicated().

Suppression si nécessaire via df.drop_duplicates().

📊 6. Analyse statistique descriptive
Exploration des données numériques avec df.describe() pour obtenir :

Moyenne, médiane, minimum, maximum, écart type, etc.

Cela permet de repérer des anomalies éventuelles.

🚨 7. Détection des valeurs aberrantes
Identification et traitement des outliers à l’aide de :

Règles logiques (valeurs incohérentes),

Méthodes statistiques (ex. : IQR, score-z).