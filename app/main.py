from fastapi import FastAPI
from random import choice

app = FastAPI()

NAMES = {
    'male': ['Bob', 'Joe', 'Sam'],
    'female': ['Mary', 'Suzy', 'Abigail'],
    'nonbinary': ['Skylar', 'Robin'],
}

async def generate_name(gender: str):
    return choice(NAMES[gender])

@app.get("/")
async def root():
    return {"root": 0}

@app.get("/ping")
async def ping():
    return {'success': 1}

@app.get("/names")
async def generate_names(gender: str, count: int):
    names = []
    for i in range(count):
        names.append(await generate_name(gender=gender))
    return {'names': names}
