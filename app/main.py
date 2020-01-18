from fastapi import FastAPI
from random import choice

app = FastAPI()

GENDERS = ['male', 'female', 'nonbinary']
NAMES = {
    'male': ['Bob', 'Joe', 'Sam'],
    'female': ['Mary', 'Suzy', 'Abigail'],
    'nonbinary': ['Skylar', 'Robin'],
}
ANY = [element for gender in GENDERS for element in NAMES[gender]]


async def generate_name(gender: str):
    if gender == 'any':
        return choice(ANY)
    return choice(NAMES[gender])

@app.get("/")
async def root():
    return {"root": 0}

@app.get("/ping")
async def ping():
    return {'success': 1}

@app.get("/names")
async def generate_names(gender: str = 'any', count: int = 1):
    names = []
    for i in range(count):
        names.append(await generate_name(gender=gender))
    return {'names': names}
