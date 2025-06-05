from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        task_id = len(tasks) + 1
        tasks.append({'id': task_id, 'task': task})
        return jsonify({'message': 'Task added', 'id': task_id}), 201
    return jsonify({'error': 'No task provided'}), 400

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        new_task = request.json.get('task')
        task['task'] = new_task
        return jsonify({'message': 'Task updated'})
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)
