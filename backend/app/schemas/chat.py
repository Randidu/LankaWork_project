from pydantic import BaseModel
from typing import Optional

class ChatBase(BaseModel):
    job_id: int
    sender_id: int
    receiver_id: int
    message: str
class ChatCreate(ChatBase):
    pass
class ChatResponse(ChatBase):
    id: int

    class Config:
        orm_mode = True