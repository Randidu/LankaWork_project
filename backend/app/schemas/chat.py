from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)