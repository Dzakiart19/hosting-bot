from fastapi import FastAPI
from .database import engine
from . import models

# This creates the database tables if they don't exist.
# In a production setup, this would be handled by Alembic migrations.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Panel Hosting Bot API",
    description="The backend API for the Panel Hosting Bot service.",
    version="0.1.0",
)

# In a real app, you would import your routers here
# from .routers import users, projects
# app.include_router(users.router)
# app.include_router(projects.router)

@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {"status": "ok"}
