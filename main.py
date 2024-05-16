from fastapi import FastAPI
from asyncio import sleep

app = FastAPI()

@app.get('/')
async def info_dump():
    await sleep(2)
    return {'message': 'Hello PyCon US 2024!'}
