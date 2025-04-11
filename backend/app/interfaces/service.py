from abc import ABC, abstractmethod
from app.domain.models import TaskDB
from app.schemas.task import TaskCreate, TaskUpdate

class TaskServiceInterface(ABC):
    @abstractmethod
    def create_task(self, task_data: TaskCreate) -> TaskDB:
        pass
    
    @abstractmethod
    def update_task(self, task_id: int, task_data: TaskUpdate) -> TaskDB:
        pass
    
    @abstractmethod
    def list_tasks(self) -> list[TaskDB]:
        pass
    
    @abstractmethod
    def get_task(self, task_id: int) -> TaskDB:
        pass
    
    @abstractmethod
    def delete_task(self, task_id: int):
        pass
