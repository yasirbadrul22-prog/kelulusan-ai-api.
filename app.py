from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Prediksi Kelulusan")

class DataSiswa(BaseModel):
    nilai: float

@app.get("/")
def home():
    return {"status": "API aktif", "hari": 40}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: DataSiswa):
    if not 0 <= data.nilai <= 100:
        from fastapi import HTTPException
        raise HTTPException(
            status_code=422,
            detail="Nilai harus 0 sampai 100"
        )

    return {
        "nilai": data.nilai,
        "prediksi": "Lulus" if data.nilai >= 75 else "Belum Lulus"
    }