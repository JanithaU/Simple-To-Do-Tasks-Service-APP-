from abc import ABC, abstractmethod
from app.domain.models import TaskDB
from app.schemas.task import TaskCreate, TaskUpdate

class TaskRepository(ABC):
    @abstractmethod
    def create(self, task_data: TaskCreate) -> TaskDB:
        pass
    
    @abstractmethod
    def update(self, task_id: int, task_data: TaskUpdate) -> TaskDB:
        pass
    
    @abstractmethod
    def list_all(self) -> list[TaskDB]:
        pass
    
    @abstractmethod
    def get(self, task_id: int) -> TaskDB:
        pass
    
    @abstractmethod
    def delete(self, task_id: int):
        pass