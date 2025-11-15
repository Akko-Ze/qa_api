from fastapi import FastAPI
from pydantic import BaseModel
from llm_deepseek import get_deepseek_answer

app = FastAPI(title="DeepSeek QA API")

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "API 已启动"}

@app.post("/ask")
def ask(req: QuestionRequest):
    answer = get_deepseek_answer(req.question)
    return {"question": req.question, "answer": answer}
