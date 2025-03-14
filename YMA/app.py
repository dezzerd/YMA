from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Хранение задач в памяти
tasks = {
    "Даша": [],
    "Соня": [],
    "Кирилл": [],
    "Сделанные": []
}

# Главная страница
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Добавление задачи
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    column = data['column']
    task = data['task']
    tasks[column].append({"text": task, "done": False})
    return jsonify(success=True)

# Перемещение задачи в "Сделанные"
@app.route('/complete_task', methods=['POST'])
def complete_task():
    data = request.json
    column = data['column']
    task_index = data['task_index']
    task = tasks[column].pop(task_index)
    tasks["Сделанные"].append(task)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
