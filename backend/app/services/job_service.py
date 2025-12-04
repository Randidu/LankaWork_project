from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate

def create_job(db:Session,job :JobCreate) -> Job:
    new_job =Job(
        user_id = job.user_id,
        category = job.category,
        title = job.title,
        description = job.description,
        budget_min = job.budget_min,
        budget_max = job.budget_max,
        location = job.location,
        lat = job.lat,
        lng = job.lng
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job
     
def get_job(db:Session,job_id:int) -> Job | None:
    return db.query(Job).filter(Job.id == job_id).first()

def list_jobs(db:Session,skip:int=0,limit:int=100) -> list[Job]:
    return db.query(Job).offset(skip).limit(limit).all()

def update_job(db:Session,job_id:int,updated_data:dict) -> Job | None:
    job = db.query(Job).filter(Job.id == job_id).first()
    if job:
        for key, value in updated_data.items():
            setattr(job, key, value)
        db.commit()
        db.refresh(job)
    return job

def delete_job(db:Session,job_id:int) -> bool:
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return False
    db.delete(job)
    db.commit()
    return True