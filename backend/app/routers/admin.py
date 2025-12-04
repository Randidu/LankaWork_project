from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import user_services

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users")
def list_all_users(db: Session = Depends(get_db)):
    return db.query(user_services.User).all()

# You can later add admin-only endpoints here