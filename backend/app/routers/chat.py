from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.chat import ChatCreate, ChatResponse
from app.services import chat_service

router = APIRouter(prefix="/chats", tags=["Chats"])

@router.post("/", response_model=ChatResponse)
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    return chat_service.create_chat(db, chat)

@router.get("/user/{user_id}", response_model=list[ChatResponse])
def list_chats_for_user(user_id: int, db: Session = Depends(get_db)):
    chat = chat_service.get_chat(db, user_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat_service.list_chats_for_user(db, user_id)


@router.get("/conversation/{sender_id}/{receiver_id}", response_model=list[ChatResponse])
def list_chats_between_users(sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    list_chat = chat_service.list_chats_between_users(db, sender_id, receiver_id)
    if not list_chat:
        raise HTTPException(status_code=404, detail="No chats found between the users")
    return list_chat

@router.get("/", response_model=list[ChatResponse])
def list_all_chats(job_id:int,db: Session = Depends(get_db)):
    return chat_service.list_chats_for_job(db, job_id)

@router.delete("/{chat_id}", response_model=ChatResponse)
def delete_chat(chat_id: int, db: Session = Depends(get_db)):   
    chat = chat_service.delete_chat(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat