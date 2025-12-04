from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.job import JobCreate, JobResponse
from app.services import job_service

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return job_service.create_job(db, job)

@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = job_service.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.get("/", response_model=list[JobResponse])
def list_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return job_service.list_jobs(db, skip, limit)


@router.put("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job_update: JobCreate, db: Session = Depends(get_db)):
    job = job_service.update_job(db, job_id, job_update)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

