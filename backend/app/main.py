from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.adapters.repository import SQLAlchemyTaskRepository
from app.domain.services import TaskService
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.adapters.db import SessionLocal
from contextlib import asynccontextmanager
from typing import List
from fastapi.middleware.cors import CORSMiddleware



# Application setup
@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.adapters.db import engine
    from app.domain.models import Base
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks", response_model=List[TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    task_service = TaskService(SQLAlchemyTaskRepository(db))
    return task_service.list_tasks()

@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return TaskService(SQLAlchemyTaskRepository(db)).get_task(task_id)

@app.post("/tasks", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return TaskService(SQLAlchemyTaskRepository(db)).create_task(task)

@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return TaskService(SQLAlchemyTaskRepository(db)).update_task(task_id, task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    TaskService(SQLAlchemyTaskRepository(db)).delete_task(task_id)
    return {"detail": "Task deleted successfully"}
