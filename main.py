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

@app.get("/info/{nome}/{idade}")
async def info_pessoa(nome: str, idade: int):
    if idade < 18:
        mensagem = f"{nome}, você é menor de idade."
    else:
        mensagem = f"{nome}, você é maior de idade."
    return {"info": mensagem}