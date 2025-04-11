# Task Service

This is a FastAPI-based Simple to-do task management service designed for managing tasks with functionalities to create, update, list, retrieve, and delete tasks. It interacts with a PostgreSQL database for task storage and uses SQLAlchemy for ORM-based data management.

## Features
Via API 
- Create Task: Add a new task with title, description, and status.
- Update Task: Modify Status of an existing task.
- List Tasks: Retrieve a list of tasks, ordered by status and creation date, with a limit of 10 tasks.
- Get Task: Fetch a specific task by its ID.
- Delete Task: Remove a task by its ID.

Via UI
- Crate Task
- Update Task Status

## Architecture
The project is structured using the Ports and Adapters (Hexagonal) Architecture, where:
Backend :
- Adapters: Handle the communication with external systems (e.g., database).
- Interfaces: Define the interfaces for interacting with the domain model.
- Domain: Contains the core business logic, including the models and their behaviors.
- Schemas: Pydantic models for data validation.
Frontend:
- SPA with HTML, CSS, vanilla JS

## Requirements
Python 3.9 or later
PostgreSQL database
Docker (for containerized environments)


## Docker Setup
For a containerized setup using Docker, you can build and run the application and database with the following commands.
```
docker-compose up --build
```

#### with the default configuration (.env) 
- FE  url : http://localhost:8080/
- BE url(Swagger UI doc) : http://localhost:8000/docs  





