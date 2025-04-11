import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.domain.models import TaskDB
from app.schemas.task import TaskCreate, TaskUpdate
from app.adapters.repository import SQLAlchemyTaskRepository

@pytest.fixture
def mock_db():
    return MagicMock(Session)

@pytest.fixture
def task_repo(mock_db):
    return SQLAlchemyTaskRepository(db=mock_db)

# Test create method
def test_create_task(task_repo, mock_db):
    task_data = TaskCreate(title="Test Task", description="Test Description", status="Pending")
    
    # Mock the query to return None (task doesn't exist)
    mock_db.query().filter().first.return_value = None
    
    # Mock the db.commit() and db.refresh() methods
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    # Call the create method
    result = task_repo.create(task_data, default_user="test_user")

    # Assertions
    assert result.title == task_data.title
    assert result.description == task_data.description
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

# Test create method (task already exists)
def test_create_task_already_exists(task_repo, mock_db):
    task_data = TaskCreate(title="Test Task", description="Test Description", status="Pending")
    
    # Mock the query to return an existing task
    mock_db.query().filter().first.return_value = TaskDB(id=1, title="Test Task", description="Test Description", status="Pending")
    
    with pytest.raises(HTTPException):
        task_repo.create(task_data, default_user="test_user")

# Test update method
def test_update_task(task_repo, mock_db):
    task_data = TaskUpdate( status="Done")
    
    # Mock the query to return an existing task
    mock_task = TaskDB(id=1, title="Old Task", description="Old Description", status="Pending")
    mock_db.query().filter().first.return_value = mock_task
    
    # Call the update method
    result = task_repo.update(1, task_data)

    # Assertions
    assert result.status == task_data.status
    mock_db.commit.assert_called_once()

# Test update method (task not found)
def test_update_task_not_found(task_repo, mock_db):
    task_data = TaskUpdate(status="Done")
    
    # Mock the query to return None (task not found)
    mock_db.query().filter().first.return_value = None
    
    with pytest.raises(Exception):
        task_repo.update(1, task_data)

# Test list_all method
def test_list_all_tasks(task_repo, mock_db):
    # Mock the query to return a list of tasks
    mock_db.query().order_by().limit().all.return_value = [TaskDB(id=1, title="Task 1", description="Test Task 1", status="Done"),
                                                           TaskDB(id=2, title="Task 2", description="Test Task 2", status="Pending")]
    
    result = task_repo.list_all()

    # Assertions
    assert len(result) == 2
    assert result[0].status == "Done"
    assert result[1].status == "Pending"

# Test get method
def test_get_task(task_repo, mock_db):
    # Mock the query to return an existing task
    mock_db.query().filter().first.return_value = TaskDB(id=1, title="Test Task", description="Test Description", status="Pending")
    
    result = task_repo.get(1)

    # Assertions
    assert result.id == 1
    assert result.title == "Test Task"

# Test get method (task not found)
def test_get_task_not_found(task_repo, mock_db):
    # Mock the query to return None (task not found)
    mock_db.query().filter().first.return_value = None
    
    result = task_repo.get(1)

    # Assertions
    assert result is None

# Test delete method
def test_delete_task(task_repo, mock_db):
    # Mock the query to return an existing task
    mock_task = TaskDB(id=1, title="Test Task", description="Test Description", status="Pending")
    mock_db.query().filter().first.return_value = mock_task
    mock_db.delete = MagicMock()
    mock_db.commit = MagicMock()
    
    task_repo.delete(1)
    
    # Assertions
    mock_db.delete.assert_called_once()
    mock_db.commit.assert_called_once()

# Test delete method (task not found)
def test_delete_task_not_found(task_repo, mock_db):
    # Mock the query to return None (task not found)
    mock_db.query().filter().first.return_value = None
    
    task_repo.delete(1)
    
    # Assertions
    mock_db.delete.assert_not_called()
    mock_db.commit.assert_not_called()
