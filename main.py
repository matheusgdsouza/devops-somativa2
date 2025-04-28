from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "Hello World": "num_aleatorio", "num_aleatorio": random.randint(1, 100)}

@app.get("/saudar/{nome}")
async def saudar_nome(nome: str):
    return {"mensagem": f"Olá, {nome}! Bem-vindo(a) à nossa API."}