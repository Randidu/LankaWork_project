from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import user_services, job_service, quote_service, rating_service, chat_service ,worker_service

router = APIRouter(prefix="/admin", tags=["Admin"])


#user management endpoints
@router.get("/users")
def list_all_users(db: Session = Depends(get_db)):
    return db.query(user_services.User).all()

@router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_services.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_services.delete_user(db, user_id)
    return {"detail": "User deleted successfully"}
@router.put("/user/{user_id}")
def update_user(user_id: int, updated_data: dict, db: Session = Depends(get_db)):
    user = user_services.update_user(db, user_id, updated_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/user/{user_id}")
def patch_user(user_id: int, updated_data: dict, db: Session = Depends(get_db)):
    user = user_services.update_user(db, user_id, updated_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#worker management endpoints
@router.get("/workers")
def list_all_workers(db: Session = Depends(get_db)):
    return db.query(worker_service.Worker).all()
@router.delete("/worker/{worker_id}")
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    worker = worker_service.get_worker(db, worker_id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    worker_service.delete_worker(db, worker_id)
    return {"detail": "Worker deleted successfully"}



#job management endpoints
@router.get("/jobs")
def list_all_jobs(db: Session = Depends(get_db)):
    return db.query(job_service.Job).all()

@router.delete("/job/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = job_service.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    job_service.delete_job(db, job_id)
    return {"detail": "Job deleted successfully"}

#quote management endpoints
@router.get("/quotes")
def list_all_quotes(db: Session = Depends(get_db)):
    return db.query(quote_service.Quote).all()

@router.delete("/quote/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = quote_service.get_quote(db, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    quote_service.delete_quote(db, quote_id)
    return {"detail": "Quote deleted successfully"}

#rating management endpoints
@router.get("/ratings")
def list_all_ratings(db: Session = Depends(get_db)):
    return db.query(rating_service.Rating).all()

@router.delete("/rating/{rating_id}")
def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    rating = rating_service.get_rating(db, rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    rating_service.delete_rating(db, rating_id)
    return {"detail": "Rating deleted successfully"}

#chat management endpoints
@router.get("/chats")
def list_all_chats(db: Session = Depends(get_db)):
    return db.query(chat_service.Chat).all()

@router.delete("/chat/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    chat = chat_service.get_chat(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    chat_service.delete_chat(db, chat_id)
    return {"detail": "Chat deleted successfully"}

#platform statistics endpoint
@router.get("/stats")
def get_platform_stats(db: Session = Depends(get_db)):
    total_users = db.query(user_services.User).count()
    total_jobs = db.query(job_service.Job).count()
    total_quotes = db.query(quote_service.Quote).count()
    total_ratings = db.query(rating_service.Rating).count()
    total_chats = db.query(chat_service.Chat).count()
    
    return {
        "total_users": total_users,
        "total_jobs": total_jobs,
        "total_quotes": total_quotes,
        "total_ratings": total_ratings,
        "total_chats": total_chats
    }

@router.get("/health")
def health_check():
    return {"status": "OK"}

@router.get("/get_all_data")
def get_all_data(db: Session = Depends(get_db)):
    users = db.query(user_services.User).all()
    jobs = db.query(job_service.Job).all()
    quotes = db.query(quote_service.Quote).all()
    ratings = db.query(rating_service.Rating).all()
    chats = db.query(chat_service.Chat).all()
    
    return {
        "users": users,
        "jobs": jobs,
        "quotes": quotes,
        "ratings": ratings,
        "chats": chats
    }

@router.delete("/delete_all_data")
def delete_all_data(db: Session = Depends(get_db)):
    db.query(chat_service.Chat).delete()
    db.query(rating_service.Rating).delete()
    db.query(quote_service.Quote).delete()
    db.query(job_service.Job).delete()
    db.query(user_services.User).delete()
    db.commit()
    return {"detail": "All data deleted successfully"}

@router.get("/ping")
def ping():
    return {"message": "Pong!"}

@router.get("/version")
def get_version():
    return {"version": "1.0.0"}

