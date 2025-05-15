from flask import Flask, jsonify, request
import db
app = Flask(__name__)
db.init_db()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = db.get_all_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    task_id = db.add_task(data['title'])
    task = db.get_task(task_id)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id: int):
    data = request.get_json()
    task = db.get_task(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    title = data.get('title', None)
    completed = data.get('completed', None)
    db.update_task(task_id, title, completed)
    updated_task = db.get_task(task_id)
    return jsonify(updated_task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: int):
    task = db.get_task(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.delete_task(task_id)
    return jsonify({'message': 'Task deleted!'})

if __name__ == '__main__':
    app.run(debug=True)

