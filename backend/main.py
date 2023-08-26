from typing import Union
from fastapi import FastAPI, APIRouter

import uvicorn

app = FastAPI()
api_router = APIRouter()
app.include_router(api_router)



@app.get("/")
async def root():
    return {"msg": "Hello world!"}

@app.get("/items/{item_id}")
def update_item(item_id: int):
    return {"item_id": item_id}


