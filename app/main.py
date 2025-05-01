from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from app.database import db, init_db


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    init_db(app)

    from app.models import Task

    # Crea las tablas
    with app.app_context():
        db.create_all()

    api = Api(
        app,
        version="1.0",
        title="Todo API",
        description="A simple task management API",
        prefix="/api",
    )

    from app.routes.tasks import tasks_ns

    api.add_namespace(tasks_ns)

    return app


app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
