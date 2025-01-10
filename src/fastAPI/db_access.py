# database module for agents
# Uses Supabase postgres API connection because opensource etc
# Two sql tables coffee_types and modifiers at the moment

# Contributor: Lixang Li lli32@myune.edu.au


import os
from supabase import create_client, Client
from pydantic import BaseModel
from supabase.client import ClientOptions

# initialise Supabase client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key,  
        options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public"
    ))



def get_coffees():

    response = supabase.table("coffee_types").select("*").execute()
    return response

def get_modifiers():

    return NotImplemented

def add_coffee():

    return NotImplemented
def add_order():
    return NotImplemented

def get_orders():
    return NotImplemented
