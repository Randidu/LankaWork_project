from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base
import enum

class JobStatus(str, enum.Enum):
    POSTED = "posted"
    QUOTED = "quoted"
    ACCEPTED = "accepted"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(100))
    title = Column(String(255))
    description = Column(Text)
    budget_min = Column(Integer)
    budget_max = Column(Integer)
    location = Column(String(255))
    lat = Column(Float)
    lng = Column(Float)
    status = Column(Enum(JobStatus), default=JobStatus.POSTED)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="jobs")
    quotes = relationship("Quote", back_populates="job", cascade="all, delete-orphan")
    ratings = relationship("Rating", back_populates="job", cascade="all, delete-orphan")
    chats = relationship("Chat", back_populates="job", cascade="all, delete-orphan")
