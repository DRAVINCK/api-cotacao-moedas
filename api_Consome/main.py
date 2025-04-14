from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/cotacao/{moeda}")
def consumir_api_moedas(moeda: str):
    response = requests.get(f"http://api_b:8001/moeda/{moeda}")
    return response.json()
