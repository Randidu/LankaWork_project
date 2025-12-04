from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
import enum

class UserRole(str, enum.Enum):
    USER = "user"
    WORKER = "worker"
    ADMIN = "admin"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    role: UserRole = UserRole.USER
    location: Optional[str] = None

class CreateUser(UserBase):
    password_hash: str

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)