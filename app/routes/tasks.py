from datetime import datetime

from flask_restx import Namespace, Resource, fields

from app.database import db
from app.models import Task, TaskStatus

tasks_ns = Namespace("tasks", description="Task operations")

task_model = tasks_ns.model(
    "Task",
    {
        "id": fields.String(readonly=True),
        "title": fields.String(required=True),
        "description": fields.String,
        "due_date": fields.DateTime,
        "status": fields.String(enum=[s.value for s in TaskStatus]),
    },
)


@tasks_ns.route("/")
class TaskList(Resource):
    @tasks_ns.marshal_list_with(task_model)
    def get(self):
        """List all tasks"""
        return Task.query.all()

    @tasks_ns.expect(task_model)
    @tasks_ns.marshal_with(task_model, code=201)
    def post(self):
        """Create a new task"""
        data = tasks_ns.payload
        task = Task(
            title=data["title"],
            description=data.get("description"),
            due_date=datetime.fromisoformat(data["due_date"])
            if "due_date" in data
            else None,
            status=TaskStatus(data.get("status", "pending")),
        )
        db.session.add(task)
        db.session.commit()
        return task, 201


@tasks_ns.route("/<string:task_id>")
class TaskResource(Resource):
    @tasks_ns.marshal_with(task_model)
    def get(self, task_id):
        """Get a specific task"""
        return Task.query.get_or_404(task_id)

    @tasks_ns.expect(task_model)
    @tasks_ns.marshal_with(task_model)
    def put(self, task_id):
        """Update a task"""
        task = Task.query.get_or_404(task_id)
        data = tasks_ns.payload
        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.status = TaskStatus(data.get("status", task.status.value))
        db.session.commit()
        return task

    def delete(self, task_id):
        """Delete a task"""
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return "", 204
