from fastapi import FastAPI, HTTPException
from api_Moeda.db import get_currency_from_db
from api_Moeda.apiexterna import consultar_api_externa
import redis

app = FastAPI()
cache = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.get("/moeda/{nome}")
def get_moeda(nome: str):

    # Verifica o cache
    cached = cache.get(nome)
    if cached:
        return {"moeda": nome, "valor em BRL": cached, "fonte": "redis"}

    valor = consultar_api_externa(nome)
    if valor:
        valor_float = valor
        cache.set(nome, valor_float, ex=60)
        return {"moeda": nome, "valor em BRL": valor_float, "fonte": "api externa"}
    
    valor = get_currency_from_db(nome)
    if valor:
        valor_float = float(valor)  # Converte para float
        cache.set(nome, valor_float, ex=60)
        return {"moeda": nome, "valor em BRL": valor_float, "fonte": "mysql"}

    

    
    raise HTTPException(status_code=404, detail="Moeda não encontrada")
