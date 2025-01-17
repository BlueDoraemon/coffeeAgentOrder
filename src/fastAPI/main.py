
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
    "google/gemini-2.0-flash-exp:free",  # use phi 3 beccause gemini sucks for tool use
    base_url="https://openrouter.ai/api/v1",
    api_key=get_key('OPEN_ROUTER_API_KEY')
)
import os
import argparse
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.models.openai import OpenAIModel
from db_access import DatabaseOperations
from coffee_input_agent import create_coffee_agent
from config import get_key

def initialise_agents():
    """Initialise the AI models and database"""
    model = GeminiModel("gemini-2.0-flash-exp", api_key=get_key('GEMINI_API_KEY'))
    function_calling_model = OpenAIModel(
        "google/gemini-2.0-flash-exp:free",
        base_url="https://openrouter.ai/api/v1",
        api_key=get_key('OPEN_ROUTER_API_KEY')
    )
    
# use this instead of agent for now
    db = DatabaseOperations()
    coffees = db.get_coffees()
    modifiers = db.get_modifiers()
    
    return model, db, coffees, modifiers
# sometimes errors out and openrouter's known issue https://github.com/pydantic/pydantic-ai/issues/527
def process_order(coffee_agent, order_text): 
    """Process a coffee order"""
    try:
        result = coffee_agent.run_sync(order_text)
        return result.data
    except Exception as e:
        print(f"Error processing order: {str(e)}")
        return None

def main(): 
    parser = argparse.ArgumentParser(description="Coffee Order Processing System")
    parser.add_argument("--list-menu", action="store_true", help="Show available coffees")
    parser.add_argument("--order", type=str, help="Place a coffee order")
    
    args = parser.parse_args()
    
    # Initialise components
    model, db, coffees, modifiers = initialise_agents()
    coffee_agent = create_coffee_agent(model, coffees, modifiers)
    
    if args.list_menu:
        result = coffee_agent.run_sync("what coffees are there")
        print("\nAvailable Coffees:")
        print(result.data)
        return
        
    if args.order:
        result = process_order(coffee_agent, args.order)
        if result:
            print("\nOrder Details:")
            print(result)
    
    if not (args.list_menu or args.order):
        parser.print_help()

if __name__ == "__main__":
    main()
