from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from .base import TimestampMixin
import uuid

class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = None
    status: str = Field(default="pending", index=True)  # Changed from completed to status to match Supabase

class Task(TimestampMixin, TaskBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)  # Changed from Optional[int] to str to match uuid
    user_id: str = Field(index=True, foreign_key="user.id")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None  # Changed from completed to status
