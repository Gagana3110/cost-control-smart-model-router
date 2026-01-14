from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.sql import func
from app.db import Base

class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True)
    prompt = Column(Text)
    difficulty = Column(String(20))
    model_used = Column(String(50))
    cost_usd = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
