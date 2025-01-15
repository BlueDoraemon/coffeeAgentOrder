
# Core squential program 
#
# This program aims to use three agents to determine the order of a person's coffee 
# when the coffee order may be of a fuzzy nature and not within the store database 
# e.g. long black or americano  
# 
# Authors: Lixang Li lli32@myune.edu.au

import os
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from db_access import create_supabase_client
from dataclasses import dataclass, field
from config import get_key
from db_agent import create_db_agent
from pydantic_ai.models.openai import OpenAIModel



# Get required api keys
app = FastAPI()

model = GeminiModel("gemini-2.0-flash-exp",api_key = get_key('GEMINI_API_KEY'))
function_calling_model = OpenAIModel(
    "microsoft/phi-3-medium-128k-instruct:free",  # use phi 3 beccause gemini sucks for tool use
    base_url="https://openrouter.ai/api/v1",
    api_key=get_key('OPEN_ROUTER_API_KEY'),
)
dbAgent = create_db_agent(function_calling_model)
# from db_access import DatabaseOperations
# db = DatabaseOperations()
# print(db.get_coffees())


result = dbAgent.run_sync("get coffee types")

print(result.data)

# coffeeAgent = create_coffee_agent(model)

# judgeAgent = create_judge_agent(model)

# # 
# @dataclass
# class MyCoffee(BaseModel): 
#     itemID: int
#     size: str
#     itemName: str
#     modifiers:str



# result = coffeeAgent.run_sync("Can I order an americano?")

# coffeeAgent = Agent(model=model, result_type=MyCoffee)
# dbAgent = Agent(model = model)
# judgeAgent = Agent(model=model)


# print(result.data)
# judgeResult = judgeAgent.run_sync("Test: waht is the capital of Mexico?")
# print("Judge agent:" + judgeResult.data)

# # @app.post("/api/chat")
# # async def chat_endpoint(message: str):
# #     result = await agent.run(message)
# #     return result.data
