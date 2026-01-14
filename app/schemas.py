from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    response: str
    model_used: str
    cost_usd: float
