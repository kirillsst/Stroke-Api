from fastapi import APIRouter, HTTPException
from stroke_api import filters

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Stroke Prediction !"}

# # TODO décommenter et compléter
@router.get("/patients/")
def get_patients(gender: str = None, stroke: int = None, max_age: float = None):
    filtered_df = filters.filter_patient(gender=gender, stroke=stroke, max_age=max_age)
    return filtered_df

# TODO décommenter et compléter
@router.get("/patients/{patient_id}")
def get_patient_by_id(patient_id: int):
    patient = filters.get_id(patient_id)

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient
# TODO Ajout de la route stats

@router.get("/stats/")
def get_stats():
    df = filters.statistic()

    if df is None or df.empty:
        raise HTTPException(status_code=404, detail="No data")

    stats = {
        "total_patients": len(df),
        "stroke_count": int(df['stroke'].sum()),
        "stroke_rate": round((df['stroke'].sum() / len(df)) * 100, 2),
        "average_age": round(df['age'].mean(), 2),
        "gender_distribution": df['gender'].value_counts().to_dict()
    }

    return stats

#poetry run fastapi dev stroke_api/main.py