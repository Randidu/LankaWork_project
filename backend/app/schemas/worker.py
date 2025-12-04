from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class WorkerBase(BaseModel):
    category: Optional[str] = None
    skills: Optional[str] = None
    experience_years: Optional[int] = 0
    price_min: Optional[int] = None
    price_max: Optional[int] = None
    is_verified: Optional[bool] = False

class WorkerCreate(WorkerBase):
    user_id: int

class WorkerResponse(WorkerBase):
    id: int
    rating_avg: float = 0.0

    model_config = ConfigDict(from_attributes=True)