import uuid
from pydantic import BaseModel
from datetime import datetime
from .models import ProjectStatus, DeploymentStatus


# --- User Schemas ---
class UserBase(BaseModel):
    telegram_id: int
    first_name: str
    username: str | None = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True


# --- Project Schemas ---
class ProjectBase(BaseModel):
    name: str
    git_url: str | None = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: uuid.UUID
    user_id: uuid.UUID
    subdomain: str
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# --- Deployment Schemas ---
class DeploymentBase(BaseModel):
    project_id: uuid.UUID
    git_sha: str | None = None

class DeploymentCreate(DeploymentBase):
    pass

class Deployment(DeploymentBase):
    id: uuid.UUID
    status: DeploymentStatus
    build_logs: str | None = None
    created_at: datetime

    class Config:
        orm_mode = True


# --- Token Schemas for JWT ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    telegram_id: int | None = None
