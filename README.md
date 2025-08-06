Stroke data project
===================

Ce projet contient les fichiers nécessaires au brief Stroke data - Développement d'une API REST et visualisation.

============================================================================

Je commence par charger le fichier CSV, puis je regarde head() et info().
Ensuite, je vérifie les valeurs manquantes.
Je change les types si besoin avec astype().
Je vérifie s’il y a des doublons et je les supprime si nécessaire.
Je remplis, supprime ou remplace les valeurs NaN.
Enfin, j’utilise describe() pour voir les détails.

============================================================================

Différence principale avec CSV :
Parquet est binaire et compressé, alors que CSV est texte brut. Parquet est donc plus rapide à lire/écrire et prend moins de place.

Quand l’utiliser ?
Idéal quand on travaille avec beaucoup de données, surtout en data science ou big data.

Pourquoi adapté aux gros volumes ?
Parce qu’il est colonnes par colonnes, compressé, et permet de lire seulement ce qu’on a besoin (pas tout le fichier comme CSV).