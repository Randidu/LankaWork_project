from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import CreateUser


def create_user(db: Session, user: CreateUser) -> User:
    db_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password_hash=user.password_hash,
        role=user.role,
        location=user.location
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def update_user(db:Session ,user_id:int, updated_data:dict) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in updated_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


