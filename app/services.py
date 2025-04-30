from typing import List
from uuid import UUID

from .models import StatusEnum, Task


class TaskService:
    def __init__(self):
        self.tasks_db: List[Task] = []

    def create_task(self, task: Task) -> Task:
        self.tasks_db.append(task)
        return task

    def list_tasks(self) -> List[Task]:
        return self.tasks_db

    def get_task(self, task_id: UUID) -> Task:
        for task in self.tasks_db:
            if task.id == task_id:
                return task
        raise ValueError("Task not found")

    def update_task_status(self, task_id: UUID, status: StatusEnum) -> Task:
        task = self.get_task(task_id)
        task.status = status
        return task

    def delete_task(self, task_id: UUID) -> None:
        task = self.get_task(task_id)
        self.tasks_db.remove(task)
