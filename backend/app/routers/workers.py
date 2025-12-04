from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.worker import WorkerCreate, WorkerResponse
from app.services import worker_service

router = APIRouter(prefix="/workers", tags=["Workers"])

@router.post("/", response_model=WorkerResponse)
def create_worker(worker: WorkerCreate, db: Session = Depends(get_db)):
    return worker_service.create_worker(db, worker)

@router.get("/{worker_id}", response_model=WorkerResponse)
def get_worker(worker_id: int, db: Session = Depends(get_db)):
    worker = worker_service.get_worker(db, worker_id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker

@router.get("/", response_model=list[WorkerResponse])
def list_workers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return worker_service.list_workers(db, skip, limit)
@router.put("/{worker_id}", response_model=WorkerResponse)
def update_worker(worker_id: int, worker_update: WorkerCreate, db: Session = Depends(get_db)):
    worker = worker_service.update_worker(db, worker_id, worker_update)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker

@router.delete("/{worker_id}", response_model=WorkerResponse)
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    worker = worker_service.delete_worker(db, worker_id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker