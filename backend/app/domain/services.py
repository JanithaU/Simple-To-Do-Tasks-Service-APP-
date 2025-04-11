from app.domain.models import TaskDB
from app.interfaces.repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository
    
    def create_task(self, task_data: TaskCreate) -> TaskDB:
        return self.repository.create(task_data, default_user="default_user")
    
    def update_task(self, task_id: int, task_data: TaskUpdate) -> TaskDB:
        return self.repository.update(task_id, task_data)
    
    def list_tasks(self) -> list[TaskDB]:
        return self.repository.list_all()
    
    def get_task(self, task_id: int) -> TaskDB:
        return self.repository.get(task_id)
    
    def delete_task(self, task_id: int):
        self.repository.delete(task_id)
