# database module for agents
# Uses Supabase postgres API connection because opensource etc
# Two sql tables coffee_types and modifiers at the moment

# Contributor: Lixang Li lli32@myune.edu.au

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from supabase import create_client, Client
from supabase.client import ClientOptions
from config import get_key
import logging
import os

def create_supabase_client() -> Optional[Client]:
    """Create and return a Supabase client instance."""
    try:
        return create_client(
            supabase_url=get_key("SUPABASE_URL"),
            supabase_key=get_key("SUPABASE_KEY"),
            options=ClientOptions(
                postgrest_client_timeout=10,
                storage_client_timeout=10,
                schema="public"
            )
        )
    except ValueError as e:
        logging.error(f"Supabase client initialization failed: {e}")
        return None

class DatabaseOperations:
    """Database operations for coffee shop management."""
    
    def __init__(self, supabase_client: Optional[Client] = None):
        self.client = supabase_client or create_supabase_client()
        if not self.client:
            raise ValueError("Supabase client not initialized")

    def get_coffees(self) -> Optional[List[Dict]]:
        """Retrieve all coffee types."""
        try:
            api_response = self.client.table("coffee_types").select("*").execute()
            return api_response.data
        except Exception as e:
            logging.error(f"Error fetching coffees: {e}")
            return None

    def get_modifiers(self) -> Optional[List[Dict]]:
        """Retrieve all modifiers."""
        try:
            response = self.client.table("modifiers").select("*").execute()
            return response.data
        except Exception as e:
            logging.error(f"Error fetching modifiers: {e}")
            return None

        def add_coffee(self):
            """Add a new coffee type."""
            return NotImplemented

        def add_order(self):
            """Add a new order."""
            return NotImplemented

        def get_orders(self):
            """Retrieve all orders."""
            return NotImplemented
