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
