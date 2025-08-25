# 🩺 Stroke Dataset API

API pour travailler avec les données des patients.
Implémenté avec **FastAPI**, il permet le filtrage des données, la consultation des statistiques et des informations sur des patients individuels.

---

## 🚀 Installation et lancement

### 1. Cloner le repository

```bash
git clone -b Kirill https://github.com/nabil-ghazali/stroke-api.git
cd stroke-api
cd stroke_api
```

### 2. Installer les dépendances (Poetry)

```bash
poetry install
```

### 3. Lancer le serveur FastAPI

```bash
poetry run fastapi dev stroke_api/main.py
```

Le serveur sera accessible à l'adresse :

```
http://127.0.0.1:8000/docs
```

### 4. Lancer l'application Streamlit
```bash
poetry run streamlit run stroke_api/streamlit_API.py
```

Le serveur sera accessible à l'adresse :

```
http://localhost:8501/
```

---

## 📂 Structure du projet

```
stroke-api/
│
├── stroke_api/
│   ├──__init__.py               
│   ├── API_tuto.ipynb            
│   ├── main.py                  # Point d'entrée, lancement de l'application
│   ├── api.py                   # Routes API
│   ├── filters.py               # Logique de filtrage des données
│   └── streamlit_API.py         # Application Streamlit pour visualisation et filtrage
│
├── fichier_parquet.parquet      # Données
├── pyproject.toml               # Dépendances Poetry
├── poetry.lock                  # Lock file des dépendances
└── README.md                    # Documentation
```

## 🔗 Endpoints disponibles

| Méthode | Route                    | Description                     | Paramètres                    |
| ------- | ------------------------ | ------------------------------- | ----------------------------- |
| GET     | `/patients/`             | Liste des patients avec filtres | `gender`, `stroke`, `max_age` |
| GET     | `/patients/{patient_id}` | Détails d'un patient spécifique | `patient_id`                  |
| GET     | `/stats/`                | Statistiques globales           | —                             |
| GET     | `/docs`                  | Swagger UI pour tester l'API    | —                             |

## 🛠️ Technologies

* [FastAPI](https://fastapi.tiangolo.com/)
* [Pandas](https://pandas.pydata.org/)
* [Poetry](https://python-poetry.org/)
* [Streamlit](https://streamlit.io/)
