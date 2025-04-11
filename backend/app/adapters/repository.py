from sqlalchemy.orm import Session
from app.domain.models import TaskDB
from app.schemas.task import TaskCreate, TaskUpdate
from app.interfaces.repository import TaskRepository
from fastapi import HTTPException
from sqlalchemy import case, desc


class SQLAlchemyTaskRepository(TaskRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, task_data: TaskCreate, default_user: str = "default_user" ) -> TaskDB:
        existing_task = self.db.query(TaskDB).filter(
                    TaskDB.title == task_data.title,
                    TaskDB.description == task_data.description,
                    TaskDB.status == "Pending"
                ).first()

        if existing_task:
            raise HTTPException(
                status_code=400,
                detail="Task with the same title and description already exists"
            )

        task_data_dict = task_data.model_dump(exclude_unset=True)
        task_data_dict['user'] = default_user      
        task = TaskDB(**task_data_dict)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task
    
    def update(self, task_id: int, task_data: TaskUpdate) -> TaskDB:
        task = self.db.query(TaskDB).filter(TaskDB.id == task_id).first()
        if not task:
            raise Exception("Task not found")
        for key, value in task_data.dict(exclude_unset=True).items():
            setattr(task, key, value)
        self.db.commit()
        return task
    
    def list_all(self) -> list[TaskDB]:
        return self.db.query(TaskDB).order_by( case((TaskDB.status == "Done", 1), else_=0),desc(TaskDB.created_at)).limit(10).all()
    
    def get(self, task_id: int) -> TaskDB:
        return self.db.query(TaskDB).filter(TaskDB.id == task_id).first()
    
    def delete(self, task_id: int):
        task = self.db.query(TaskDB).filter(TaskDB.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()
