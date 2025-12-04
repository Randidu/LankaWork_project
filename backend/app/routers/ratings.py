from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.rating import RatingCreate, RatingResponse
from app.services import rating_service

router = APIRouter(prefix="/ratings", tags=["Ratings"])

@router.post("/", response_model=RatingResponse)
def create_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    return rating_service.create_rating(db, rating)

@router.get("/worker/{worker_id}", response_model=list[RatingResponse])
def list_ratings_for_worker(worker_id: int, db: Session = Depends(get_db)):
    return rating_service.list_ratings_for_worker(db, worker_id)

@router.get("/job/{job_id}", response_model=list[RatingResponse])
def list_ratings_for_job(job_id: int, db: Session = Depends(get_db)):
    return rating_service.list_ratings_for_job(db, job_id)

@router.get("/{rating_id}", response_model=RatingResponse)
def get_rating(rating_id: int, db: Session = Depends(get_db)):
    rating = rating_service.get_rating(db, rating_id)
    return rating