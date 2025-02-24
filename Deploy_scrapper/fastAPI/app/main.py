from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

@app.get("/")
def home():
    return {"health_check":"ok", "model_version":model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload:TextIn):
    language = predict_pipeline(payload.text)
    return{'language': language}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

#uvicorn app.main:app --host 127.0.0.1 --port 8000
