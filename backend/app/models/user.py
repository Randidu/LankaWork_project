import datetime
import enum
from sqlalchemy import Integer,Column,String,DateTime,Enum
from sqlalchemy.orm import relationship
from ..database import Base

class UserRole(str,enum.Enum):
    USER = "user"
    WORKER ="worker"
    ADMIN = "admin"
class User(Base):
    __tablename__ = "users"

    id =Column(Integer,primaty_key=True,index=True)
    name =Column(String(255),nullable=False)
    email = Column(String(255),nullable=False,unique=True,index=True)
    phone =Column(String(50))
    password_hash =Column(String(255),nullable=False)
    relo = Column(Enum(UserRole),default=UserRole.USER)
    location = Column(String(255))
    create_at = Column(DateTime , default=datetime.UTC)
    update_at =Column(DateTime,default=datetime.UTC)

    worker_profile = relationship("Worker",back_populates="user")
    jobs = relationship("Jobs",back_populates="user")
    rating_given = relationship("Rating",back_populates="user")