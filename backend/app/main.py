from fastapi import FastAPI
from app.config import settings
from app.database import engine, Base

# Import routers
from app.routers import (
    users,
    workers,
    jobs,
    quotes,
    ratings,
    chat,
    auth,
    admin,
)

# Create tables if not using Alembic migrations
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

# Register routers
app.include_router(users.router)
app.include_router(workers.router)
app.include_router(jobs.router)
app.include_router(quotes.router)
app.include_router(ratings.router)
app.include_router(chat.router)
app.include_router(auth.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Welcome to LankaWork API"}