# app/models/rating.py
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    worker_id = Column(Integer, ForeignKey("workers.id", ondelete="CASCADE"))
    stars = Column(Integer)
    review = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    job = relationship("Job", back_populates="ratings")
    user = relationship("User", back_populates="ratings_given")
    worker = relationship("Worker", back_populates="ratings")