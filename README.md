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


## Using Google Gemini API

Get an api key:
https://ai.google.dev/gemini-api/docs/api-key

Store your API key as an environment variable:
For Linux/macOS (Bash):
```bash
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

** For Windows: **
Windows
```bash
    setx GEMINI_API_KEY "your_key_here"
```
or 
Search for "Environment Variables" in the system settings
Edit either "User variables" (for current user) or "System variables" (for all users - use with caution).
Create the variable and add export GEMINI_API_KEY=your_key_here
Apply the changes

After applying changes to environment variables please restart your IDE
