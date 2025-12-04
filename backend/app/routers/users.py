from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import CreateUser, UserResponse
from app.services import user_services


router=APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create_user(user : CreateUser,db:Session =Depends(get_db)):
    existing =user_services.get_user_by_email(db,user.email)
    if existing:
        raise HTTPException(status_code=400,detail="Email alresy registerd")
    return user_services.create_user(db,user)

@router.get("/{user_id}" ,response_model=UserResponse)
def get_user(user_id : int ,db:Session = Depends(get_db)):
    user =user_services.get_user(db,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user

@router.get("/{email}", response_model=UserResponse)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = user_services.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_data: dict, db: Session = Depends(get_db)):
    user = user_services.update_user(db, user_id, updated_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = user_services.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}