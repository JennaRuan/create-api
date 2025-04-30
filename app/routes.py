from uuid import UUID

from fastapi import APIRouter, HTTPException

from .models import StatusEnum, Task
from .services import TaskService

router = APIRouter()
task_service = TaskService()


@router.post("/tasks")
async def create_task(task: Task):
    return task_service.create_task(task)


@router.get("/tasks")
async def list_tasks():
    return task_service.list_tasks()


@router.get("/tasks/{task_id}")
async def get_task(task_id: UUID):
    try:
        return task_service.get_task(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.put("/tasks/{task_id}")
async def update_task(task_id: UUID, status: StatusEnum):
    try:
        return task_service.update_task_status(task_id, status)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: UUID):
    try:
        task_service.delete_task(task_id)
        return {"detail": "Task deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")
