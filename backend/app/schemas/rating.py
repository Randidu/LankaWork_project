from typing import Optional
from pydantic import BaseModel, ConfigDict


class RatingBase(BaseModel):
    stars: int
    review: Optional[str] = None

class RatingCreate(RatingBase):
    job_id: int
    user_id: int
    worker_id: int

class RatingResponse(RatingBase): 
    id: int

    model_config = ConfigDict(from_attributes=True)