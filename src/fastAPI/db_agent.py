# agent to retrieve and create database operations
# chooses to use tools to look up database from DatabaseOperations class

from pydantic_ai import Agent, RunContext, ModelRetry
from typing import List, Dict, Optional
import logging
from db_access import DatabaseOperations

def create_db_agent(model) -> Agent:
    """Create database operations agent."""
    db_agent = Agent(
        model=model,
        deps_type=DatabaseOperations,
        result_type=Dict[str, List[Dict]],
        system_prompt="""
        You are a coffee shop database agent.
        Handle database operations for:
        - Coffee types with properties and availability
        - Modifiers with options and costs
        """,
        retries=3
    )

    @db_agent.result_validator
    def validate_response(_ctx: RunContext[DatabaseOperations], value: Dict[str, List[Dict]]) -> Dict[str, List[Dict]]:
        """Validate database operation results."""
        if not value:
            raise ModelRetry("Empty database response")
        return value

    async def report_tool_usage(ctx: RunContext[DatabaseOperations], tool_name: str):
        """Reports tool usage."""
        logging.info(f"Database operation: {tool_name}")

    @db_agent.tool(prepare=report_tool_usage)
    async def get_all_coffees(ctx: RunContext[DatabaseOperations]) -> Optional[List[Dict]]:
        """Get all coffee types."""
        return ctx.deps.get_coffees()

    @db_agent.tool(prepare=report_tool_usage)
    async def get_all_modifiers(ctx: RunContext[DatabaseOperations]) -> Optional[List[Dict]]:
        """Get all modifiers."""
        return ctx.deps.get_modifiers()

    return db_agent
