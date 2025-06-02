from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from app.openai_utils import generate_sql_from_question
from app.query_executor import run_sql_query
import os





app = FastAPI()
load_dotenv(dotenv_path=os.path.join("data", ".env"))

class Question(BaseModel):
    message: str

@app.get("/ping")
def ping():
    return {"status": "alive"}

@app.post("/chat")
def chat_with_bot(q: Question):
    question = q.message
    sql = generate_sql_from_question(question)
    answer = run_sql_query(sql)
    return {"sql": sql, "answer": answer}
