from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/cotacao/{moeda}")
def consumir_api_moedas(moeda: str):
    response = requests.get(f"http://api_b:8001/moeda/{moeda}")
    return response.json()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)