from sqlalchemy.orm import Session
from app.models.worker import Worker
from app.schemas.worker import WorkerCreate, WorkerResponse, WorkerBase



def create_worker(db: Session, worker: WorkerCreate) -> Worker:
    new_worker = Worker(
        user_id=worker.user_id,
        category=worker.category,
        skills=worker.skills,
        experience_years=worker.experience_years,
        price_min=worker.price_min,
        price_max=worker.price_max,
        is_verified=worker.is_verified,
        rating_avg=0.0,  # default
    )
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker



def get_worker(db: Session, worker_id: int) -> Worker | None:
    return db.query(Worker).filter(Worker.id == worker_id).first()


def list_workers(db: Session, skip: int = 0, limit: int = 10) -> list[Worker]:
    return db.query(Worker).offset(skip).limit(limit).all()



def update_worker(db: Session, worker_id: int, worker_update: WorkerBase) -> Worker | None:
    worker = db.query(Worker).filter(Worker.id == worker_id).first()
    if not worker:
        return None

    
    for key, value in worker_update.dict(exclude_unset=True).items():
        setattr(worker, key, value)

    db.commit()
    db.refresh(worker)
    return worker



def delete_worker(db: Session, worker_id: int) -> Worker | None:
    worker = db.query(Worker).filter(Worker.id == worker_id).first()
    if not worker:
        return None

    db.delete(worker)
    db.commit()
    return worker