from pydantic import BaseModel
from typing import Optional
import enum

class JobStatus(str, enum.Enum):
    POSTED = "posted"
    QUOTED = "quoted"
    ACCEPTED = "accepted"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class JobBase(BaseModel):
    category: Optional[str] = None
    title: str
    description: Optional[str] = None
    budget_min: Optional[int] = None
    budget_max: Optional[int] = None
    location: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None

class JobCreate(JobBase):
    user_id: int

class JobResponse(JobBase):
    id: int
    status: JobStatus = JobStatus.POSTED

    class Config:
        orm_mode = True