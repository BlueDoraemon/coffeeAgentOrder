import os
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

class MyCoffee(BaseModel): 
    itemID: int
    size: str
    itemName: str
    modifiers:str

app = FastAPI()
MY_KEY = os.getenv('GEMINI_API_KEY')
if not MY_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not found")

model = GeminiModel("gemini-2.0-flash-exp",api_key = MY_KEY )
coffeeAgent = Agent(model=model,result_type=MyCoffee)
judgeAgent = Agent(model=model)

result = coffeeAgent.run_sync("What is an americano?")

print(result.data)
judgeResult = judgeAgent.run_sync("Test waht is the capital of Mexico?")
print("Judge agent:" + judgeResult.data)
# @app.post("/api/chat")
# async def chat_endpoint(message: str):
#     result = await agent.run(message)
#     return result.data
