
# make sure to set up these variables beforehand
# gemini
# supabase
from dotenv import load_dotenv
import os

load_dotenv()

def get_key(key_name: str) -> str:
    """Get environment variable value."""
    value = os.getenv(key_name)
    if not value:
        raise ValueError(f"Missing environment variable: {key_name}")
    return value
