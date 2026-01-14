from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.schemas import PromptRequest, PromptResponse
from app.router import classify_prompt
from app.model_selector import route_to_model
from app.db import SessionLocal, engine
from app.models import Base, RequestLog

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cost-Control Smart Model Router")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate", response_model=PromptResponse)
def generate(request: PromptRequest, db: Session = Depends(get_db)):
    difficulty = classify_prompt(request.prompt)

    (response, cost), model_name = route_to_model(request.prompt, difficulty)

    log = RequestLog(
        prompt=request.prompt,
        difficulty=difficulty,
        model_used=model_name,
        cost_usd=cost
    )

    db.add(log)
    db.commit()

    return PromptResponse(
        response=response,
        model_used=model_name,
        cost_usd=cost
    )
