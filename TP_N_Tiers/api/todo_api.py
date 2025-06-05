from flask_restful import Resource, reqparse
from services.todo_service import TodoService

service = TodoService()
parser = reqparse.RequestParser()
parser.add_argument('task', type=str, required=True, help='Task text is required')

class TaskList(Resource):
    def get(self):
        return service.get_all_tasks()

    def post(self):
        args = parser.parse_args()
        return service.add_task(args['task']), 201
