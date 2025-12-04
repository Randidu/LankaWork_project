from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.quote import QuoteCreate, QuoteResponse
from app.services import quote_service

router = APIRouter(prefix="/quotes", tags=["Quotes"])

@router.post("/", response_model=QuoteResponse)
def create_quote(quote: QuoteCreate, db: Session = Depends(get_db)):
    return quote_service.create_quote(db, quote)

@router.get("/job/{job_id}", response_model=list[QuoteResponse])
def list_quotes_for_job(job_id: int, db: Session = Depends(get_db)):
    return quote_service.list_quotes_for_job(db, job_id)