from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(100))
    skills = Column(Text)
    experience_years = Column(Integer, default=0)
    price_min = Column(Integer)
    price_max = Column(Integer)
    rating_avg = Column(Float, default=0.0)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="worker_profile")
    quotes = relationship("Quote", back_populates="worker", cascade="all, delete-orphan")
    ratings = relationship("Rating", back_populates="worker", cascade="all, delete-orphan")
