from sqlalchemy.orm import Session
from app.models.rating import Rating
from app.schemas.rating import RatingCreate

def create_rating(db: Session, rating: RatingCreate) -> Rating:
    new_rating = Rating(
        job_id=rating.job_id,
        user_id=rating.user_id,
        worker_id=rating.worker_id,
        stars=rating.stars,
        review=rating.review
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating

def get_rating(db: Session, rating_id: int) -> Rating | None:
    return db.query(Rating).filter(Rating.id == rating_id).first()

def list_ratings_for_worker(db: Session, worker_id: int):
    return db.query(Rating).filter(Rating.worker_id == worker_id).all()

def list_ratings_for_job(db: Session, job_id: int):
    return db.query(Rating).filter(Rating.job_id == job_id).all()

def delete_rating(db: Session, rating_id: int) -> bool:
    rating = db.query(Rating).filter(Rating.id == rating_id).first()
    if not rating:
        return False
    db.delete(rating)
    db.commit()
    return True