# agent to determine a fuzzy order and transform it into a proper order
# for example an americano -> long black
# or a cortado -> strong latte etc

from pydantic_ai import Agent, RunContext, ModelRetry
from typing import List
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging
from db_access import DatabaseOperations
from typing import Optional, List
from uuid import UUID


# Create a coffee agent
def create_coffee_agent(model,coffees, modifiers) -> Agent:
    agent = Agent(
        model=model,
        # result_type= dict,
        system_prompt=f"""
        You are a coffee order assistant that maps customer orders to standard menu items.
        Given a customer order, check the coffee types and modifiers and provide the exact corresponding output.
        Available coffee types are {coffees}
        Available modifiers are {modifiers}

       
Given a customer order, return a JSON object with standardized order details.

        Input Order: [customer's natural language coffee order (NOTE: if there is no coffee order from the available
        coffee types use the most appropriate coffee type available using probability)]
        Output Format: JSON with the following structure:
        
            "size": string,  // small, regular, large
            "coffee_type": string,
            "modifiers": string[]  // extras, sugars, etc.
            "total_price": float
        

        Examples:
        Input: "I'd like a large flat white with 2 sugars"
        Output: 
            "size": "large",
            "menu_item": "flat white",
            "modifications": ["2 sugars"]
            "total_price": 
        

        Input: "Can I get a regular magic please?"
        Output: 
            "menu_number": 3,
            "size": "regular",
            "menu_item": "melbourne magic",
            "modifications": ["double ristretto"]
            "total_price":
        

        Rules:
        - melbourne magic is a double ristretto flat white
        - americano is a long black
        - use only standard sizes: small, regular, large
        - keep modifications list concise and standardized
        - always return valid JSON format
        - menu_number must be an integer
        - size must be one of: small, regular, large
        """)
    return agent