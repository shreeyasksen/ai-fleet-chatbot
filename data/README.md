# ai-fleet-chatbot
"MVP AI Chatbot Assistant for Datakrew Fleet Analytics Platform"
An AI-powered assistant that converts natural language queries into secure, optimized SQL queries and fetches actionable insights from high-frequency electric vehicle raw telemetry data.

Higlights:
Converts user-friendly questions into accurate SQL queries
Executes queries securely on a PostgreSQL database
Applies row-level security to ensure users only see data from their own fleet
Designed for operations managers.
Helps users get fast insights without needing to write any code

Questions:
1. { "message": "What is the SOC of vehicle GBM6296G right now?" }
2. { "message": "How many SRM T3 EVs are in my fleet?" }
3. { "message": "Did any SRM T3 exceed 33 °C battery temperature in the last 24 hours?" }
4. { "message": "What is the fleet-wide average SOC comfort zone?" }
5. { "message": "Which vehicles spent more than 20% of the past week in the 90–100% SOC band?" }
6. { "message": "How many vehicles are currently driving with SOC less than 30%?" }
7. { "message": "What is the total kilometers and driving hours by my fleet over the past 7 days, and which vehicles are the most-used and least-used?" }


Technologies Used
FastAPI: A modern Python web framework that powers the backend of this chatbot. It handles all incoming queries and routes them securely to the right logic.
PostgreSQL: The primary database storing real-time electric vehicle raw telemetry data, including SOC levels, vehicle models, battery temperatures, and driving metrics. All queries are executed against this structured data source.
OpenAI API: This is the intelligence behind the chatbot. It converts natural language questions (like “Which SRM T3 vehicles crossed 33°C yesterday?”) into SQL queries that match your fleet’s  raw telemetry schema.
SQLAlchemy: An ORM (Object Relational Mapper) used to communicate between the FastAPI backend and your PostgreSQL database. It helps write clean, secure, and flexible SQL logic while keeping your database interactions.

Setup Virtual environment: 
python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
To run Fast API server: 
uvicorn app.main:app --reload--port8005
To show the server in web:
http://127.0.0.1:8005/docs#/default/chat%20with%20bot%20chat%20post

Last steps: 
Clone to github.