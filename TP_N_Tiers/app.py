from flask import Flask
from flask_restful import Api
from config import Config
from models.todo_model import db
from api.todo_api import TaskList

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db.init_app(app)

with app.app_context():
    db.create_all()

api.add_resource(TaskList, '/api/tasks')

if __name__ == '__main__':
    app.run(debug=True)
