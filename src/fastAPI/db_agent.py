# agent to retrieve and create database operations
# chooses to use tools to look up database from DatabaseOperations class

from pydantic_ai import Agent, RunContext, ModelRetry
from typing import List
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging
from db_access import DatabaseOperations
from typing import Optional, List
from uuid import UUID

class Modifier(BaseModel):
    id: UUID
    name: str
    type: str
    options: dict | None
    additional_cost: float | None

class CoffeeType(BaseModel):
    id: UUID
    item_id: str
    name: str
    description: Optional[str]
    base_price: float
    available: bool
    allowed_modifiers: Optional[List[dict]] = Field(default_factory=list)

@dataclass
class SupportDependencies:
    db: DatabaseOperations = DatabaseOperations()

def create_db_agent(model) -> Agent:
    """Initialize agent for coffee shop database operations."""
    db = DatabaseOperations
    db_agent = Agent(
        model=model,
        # deps_type=SupportDependencies,
        # result_type=List[CoffeeType | Modifier],
        # result_type= str,
        system_prompt="""
        Database agent for coffee shop inventory management.
        
        Available Functions:
        - get_coffees(): Retrieves coffee menu items with:
          * Type details (id, item_id, name)
          * Pricing and availability
          * Allowed modifications
          
        - get_modifiers(): Retrieves modification options with:
          * Modifier details (id, name, type)
          * Available options
          * Additional costs
        """,
        retries=3
    )
    # @db_agent.result_validator
    # def validate_response(_ctx: RunContext[DatabaseOperations], value: Dict[str, List[Dict]]) -> Dict[str, List[Dict]]:
    #     """Validate database operation results."""
    #     if not value:
    #         raise ModelRetry("Empty database response")
    #     return value

    # async def report_tool_usage(ctx: RunContext[DatabaseOperations], tool_name: str):
    #     """Reports tool usage."""
    #     logging.info(f"Database operation: {tool_name}")

    @db_agent.tool
    async def get_coffees():
        """Get all coffee types."""
        print("Running")
        return await db.get_coffees

    # @db_agent.tool(prepare=report_tool_usage)
    # async def get_all_modifiers(ctx: RunContext[DatabaseOperations]) -> Optional[List[Dict]]:
    #     """Get all modifiers."""
    #     return ctx.deps.get_modifiers()

    return db_agent

