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

@router.get("/{quote_id}", response_model=QuoteResponse)
def get_quote(quote_id: int, db: Session = Depends(get_db)):    
    quote = quote_service.get_quote(db, quote_id)
    return quote

@router.put("/{quote_id}", response_model=QuoteResponse)
def update_quote(quote_id: int, quote_update: QuoteCreate, db: Session = Depends(get_db)):
    quote = quote_service.update_quote(db, quote_id, quote_update)
    return quote

@router.delete("/{quote_id}", response_model=QuoteResponse)
def delete_quote(quote_id: int, db: Session = Depends(get_db)):   
    quote = quote_service.delete_quote(db, quote_id)
    return quote