"""Inference API entrypoint.
Fill code only between marker lines.
"""

#start code here
# TODO: import FastAPI/Flask and any schema validation tools
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.model_loader import load_model, predict

MODEL_PATH = "artifacts/model.bin"
MANIFEST_PATH = "artifacts/manifest.json"



# TODO: create app object
app = FastAPI(title = "Deployment Learning API", version = "0.1.0")

# TODO: define request and response schema/classes
class PredictRequest(BaseModel):
    feature_1 : float = Field(..., description = "First feature value")
    feature_2 : float = Field(..., description = "Second feature value")

class PredictResponse(BaseModel):
    model_name : str
    model_version: str
    score : float

try: 
    MODEL = load_model(MODEL_PATH, MANIFEST_PATH)
except FileNotFoundError:
    MODEL = load_model(MODEL_PATH, None)

@app.get("/health")
def health():
    return{
        "status": "ok",
        "model_version": MODEL["version"],
    }



# TODO: create POST /predict endpoint

@app.post("/predict", response_model = PredictResponse)
def predict_endpoint(payload: PredictRequest):
    try:
        result = predict(MODEL, payload.model_dump())
        return PredictResponse(**result)
    except Exception as exc:
        raise HTTPException(status_code = 500, detail = str(exc))
    

# TODO: load model once (startup or module init)
# TODO: include GET /health endpoint returning status and version
#send code here
