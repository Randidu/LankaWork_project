from sqlalchemy.orm import Session
from app.models.quote import Quote
from app.schemas.quote import QuoteCreate

def create_quote(db: Session, quote: QuoteCreate) -> Quote:
    new_quote = Quote(
        job_id=quote.job_id,
        worker_id=quote.worker_id,
        price=quote.price,
        note=quote.note,
        status=quote.status
    )
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    return new_quote

def get_quote(db: Session, quote_id: int) -> Quote | None:
    return db.query(Quote).filter(Quote.id == quote_id).first()

def list_quotes_for_job(db: Session, job_id: int):
    return db.query(Quote).filter(Quote.job_id == job_id).all()

def list_quotes_for_worker(db: Session, worker_id: int):
    return db.query(Quote).filter(Quote.worker_id == worker_id).all()