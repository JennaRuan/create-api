from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: StatusEnum
