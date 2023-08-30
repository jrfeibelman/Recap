from typing import Union
# from fastapi import FastAPI, APIRouter
# import uvicorn
from slack import fetch_slack_messages, post_slack_messages
from summarize_openai import openaiCall
import os
import yaml

# app = FastAPI()
# api_router = APIRouter()
# app.include_router(api_router)



# @app.get("/")
# async def root():
#     return {"msg": "Hello world!"}

# @app.get("/items/{item_id}")
# def update_item(item_id: int):
#     return {"item_id": item_id}

def connecting(): 
    convo_history = fetch_slack_messages("%s/config/slack.yaml"% os.getcwd()) #putting in root directory
    getAIRepsonse = openaiCall(convo_history)
    print(getAIRepsonse)

connecting()



