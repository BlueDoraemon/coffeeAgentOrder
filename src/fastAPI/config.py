
# make sure to set up these variables beforehand
# gemini
# supabase
import os

def get_key(env_key: str): 
    MY_KEY = os.getenv(env_key)
    if not MY_KEY:
        raise ValueError(f"{env_key} environment variable not found")
    return MY_KEY
