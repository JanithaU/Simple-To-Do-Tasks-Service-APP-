from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

# Task creation schema
class TaskCreate(BaseModel):
    title: str = Field(..., example="Complete report")
    description: str = Field(..., example="Finish the Q1 report")

# Task update schema
class TaskUpdate(BaseModel):
    # title: str | None = None
    # description: str | None = None
    status: str | None = None

# Task output schema
class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    status: str
    user: str
