from sqlalchemy import Column, String, DateTime, Enum as SqlEnum,Integer
from datetime import datetime
import enum
from app.adapters.db import Base

# Enum for task status
class TaskStatus(str, enum.Enum):
    pending = "Pending"
    done = "Done"

# Task database model
class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(SqlEnum(TaskStatus), default=TaskStatus.pending)
    user = Column(String, nullable=False)