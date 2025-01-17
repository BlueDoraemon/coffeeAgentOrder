# Coffee Agent Order
An intelligent system using LLM agents and function calling to transform ambiguous coffee orders into precise, standardized outputs.
System Architecture
Core Components
- LLM Agent for natural language understanding
- Function calling interface
- PostgreSQL database for order validation
- JSON response generator



``` mermaid 
graph TD
    A[Ambiguous Order Input] --> B[LLM Agent]
    B --> C[Function Calls]
    C --> D[Database Validation]
    D --> E[Standardized JSON Output]
```
## Database (Supabase Postgres)
``` mermaid
erDiagram
    coffee_types {
        uuid id PK
        text item_id
        text name
        text description
        numeric base_price
        bool available
        jsonb allowed_modifiers
    }

    modifiers {
        uuid id PK
        text name
        text type
        jsonb options
        numeric additional_cost
    }

    coffee_types ||--o{ modifiers : has
```

# Coffee Order System Usage Guide

## Command Line Interface (FOR NOW)
```bash
# View available menu
python main.py --list-menu

# Place a coffee order
python main.py --order "your coffee order"
```

## Supported Order Examples
- Long Black/Americano conversions are automatically handled:
```bash
# These orders are equivalent:
python main.py --order "large long black with 2 sugars"
python main.py --order "large americano with 2 sugars"
```

## Order Format Guidelines
- Size options: small, regular, large
- Base drinks: long black, americano, flat white, cappuccino, latte
- Modifiers:
  - Sugars (e.g., "2 sugars", "no sugar")
  - Temperature (e.g., "extra hot")
  - Milk options (e.g., "oat milk", "soy")

## Project Structure
```
src/
├── fastAPI/           # Backend services
│   ├── agents.py      # AI agent definitions
│   ├── config.py      # Configuration settings
│   ├── db_access.py   # Database operations
│   └── main.py        # Main application
└── front_end/         # Frontend interface
    └── app.py         # Streamlit application
```

## Environment Setup
1. Create `.env` file with required API keys:
```env
GEMINI_API_KEY=your_key
OPEN_ROUTER_API_KEY=your_key
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Notes
- The system automatically maps similar drink types (long black ↔ americano)
- Natural language processing handles variations in order phrasing
- Database automatically updates with order history


API Configuration
Create a .env file in the project root directory with the following variables:
```bash
# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key

# Google Gemini API
GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```


## Using Google Gemini API

Get an api key:
https://ai.google.dev/gemini-api/docs/api-key


## Using Supabase API

You can obtain these values from your Supabase project settings:
SUPABASE_URL: Your project URL found in Project Settings > API
SUPABASE_KEY: Your project API key found in Project Settings > API


After applying changes to environment variables please restart your IDE
