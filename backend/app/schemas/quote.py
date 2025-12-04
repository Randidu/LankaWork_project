import enum
from typing import Optional
from pydantic import BaseModel, ConfigDict


class QuoteStatus(str, enum.Enum):
    PENDING = "pending"
    REJECTED = "rejected"
    ACCEPTED = "accepted"

class QuoteBase(BaseModel):
    price: Optional[float] = None
    note: Optional[str] = None
    status: QuoteStatus = QuoteStatus.PENDING

class QuoteCreate(QuoteBase):
    job_id: int
    worker_id: int

class QuoteResponse(QuoteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)