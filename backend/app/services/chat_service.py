from sqlalchemy.orm import Session
from app.models.chat import Chat
from app.schemas.chat import ChatCreate

def create_chat(db: Session, chat: ChatCreate) -> Chat:
    new_chat = Chat(
        sender_id=chat.sender_id,
        receiver_id=chat.receiver_id,
        job_id=chat.job_id,
        message=chat.message
    )
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat

def get_chat(db: Session, chat_id: int) -> Chat | None:
    return db.query(Chat).filter(Chat.id == chat_id).first()

def list_chats_between_users(db: Session, sender_id: int, receiver_id: int):
    return (
        db.query(Chat)
        .filter(
            ((Chat.sender_id == sender_id) & (Chat.receiver_id == receiver_id)) |
            ((Chat.sender_id == receiver_id) & (Chat.receiver_id == sender_id))
        )
        .order_by(Chat.timestamp.asc())
        .all()
    )

def list_chats_for_job(db: Session, job_id: int):
    return db.query(Chat).filter(Chat.job_id == job_id).order_by(Chat.timestamp.asc()).all()

def delete_chat(db: Session, chat_id: int) -> bool:
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        return False
    db.delete(chat)
    db.commit()
    return True