from models.todo_model import Todo, db

class TodoService:
    def get_all_tasks(self):
        return [task.to_dict() for task in Todo.query.all()]

    def add_task(self, task_text):
        new_task = Todo(task=task_text)
        db.session.add(new_task)
        db.session.commit()
        return new_task.to_dict()
