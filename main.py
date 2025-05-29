from flask import Flask, jsonify, request
from models import db, Tasks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tim:4200@localhost:5432/flask_todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Tasks.query.all()
    result = []
    for task in tasks:
        result.append({
            'id': task.id,
            'title': task.title,
            'completed': task.completed
        })
    return jsonify(result)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    new_task = Tasks(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({
        'id': new_task.id,
        'title': new_task.title,
        'completed': new_task.completed
    }), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id: int):
    task = Tasks.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    if 'title' in data:
        task.title = data['title']
    if 'completed' in data:
        task.completed = data['completed']
    db.session.commit()

    return jsonify({
        'id': task.id,
        'title': task.title,
        'completed': task.completed
    })


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: int):
    task = Tasks.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted!'})

if __name__ == '__main__':
    app.run(debug=True)

