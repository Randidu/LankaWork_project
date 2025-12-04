from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.chat import ChatCreate, ChatResponse
from app.services import chat_service

router = APIRouter(prefix="/chats", tags=["Chats"])

@router.post("/", response_model=ChatResponse)
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    return chat_service.create_chat(db, chat)

@router.get("/conversation/{sender_id}/{receiver_id}", response_model=list[ChatResponse])
def list_chats_between_users(sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    return chat_service.list_chats_between_users(db, sender_id, receiver_id)