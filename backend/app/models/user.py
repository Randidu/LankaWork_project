import datetime
import enum
from sqlalchemy import Integer, Column, String, DateTime, Enum
from sqlalchemy.orm import relationship
from ..database import Base

class UserRole(str, enum.Enum):
    USER = "user"
    WORKER = "worker"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    phone = Column(String(50))
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER)  # Fixed typo: relo -> role
    location = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)  # Fixed: create_at -> created_at, and datetime.UTC -> datetime.datetime.utcnow
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)  # Fixed: update_at -> updated_at

    worker_profile = relationship("Worker", back_populates="user")
    jobs = relationship("Job", back_populates="user")  # Fixed: "Jobs" -> "Job"
    ratings_given = relationship("Rating", back_populates="user")