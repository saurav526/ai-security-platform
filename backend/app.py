from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_anomaly
from vector_store import semantic_search
from llm_summary import summarize_alert

app = FastAPI(
    title="AI Security Intelligence Platform"
)


class SecurityLog(BaseModel):
    duration: float
    src_bytes: float
    dst_bytes: float
    count: float
    srv_count: float


class SearchRequest(BaseModel):
    query: str


class SummaryRequest(BaseModel):
    alert: str


@app.get("/")
def home():
    return {
        "message": "AI Security Platform Running"
    }


@app.post("/predict")
def predict(log: SecurityLog):
    result = predict_anomaly(log.dict())

    return {
        "prediction": result
    }


@app.post("/search")
def search_logs(req: SearchRequest):
    results = semantic_search(req.query)

    return {
        "results": results
    }


@app.post("/summarize")
def summarize(req: SummaryRequest):
    summary = summarize_alert(req.alert)

    return {
        "summary": summary
    }