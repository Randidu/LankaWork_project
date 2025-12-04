import enum
from typing import Optional
from pydantic import BaseModel


class QuoteStatus(str , enum.Enum):
    PENDING = "pending"
    REJECTED = "rejected"
    ACCEPTED = "accepted"

class QuoteBase(BaseModel):
    price : Optional[str] = None
    note : Optional[str] = None
    status : QuoteStatus = QuoteStatus.PENDING

class CreateQuote(QuoteBase):
    job_id : int
    worker_id : int

class QuoteResponse(QuoteBase):
    id : int

    class Config:
        orm_mode = True