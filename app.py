# app.py
from flask import Flask, jsonify, request, abort
from todo_functions import load_tasks, save_tasks, add_task, edit_task, delete_task, mark_task_complete, search_tasks
import threading
import os

app = Flask(__name__)
DATA_FILE = os.environ.get("TASKS_FILE", "tasks.json")
_lock = threading.Lock()

def read_tasks():
    with _lock:
        return load_tasks(DATA_FILE)

def write_tasks(tasks):
    with _lock:
        save_tasks(tasks, DATA_FILE)

@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"status": "ok"}), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    q = request.args.get("q", "").strip()
    tasks = read_tasks()
    if q:
        results = search_tasks(tasks, q)
        return jsonify(results), 200
    return jsonify(tasks), 200

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    tasks = read_tasks()
    if 0 <= task_id < len(tasks):
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "task not found"}), 404

@app.route("/tasks", methods=["POST"])
def create_task():
    payload = request.get_json() or {}
    description = payload.get("description", "").strip()
    if not description:
        return jsonify({"error": "description required"}), 400
    tasks = read_tasks()
    add_task(tasks, description)
    write_tasks(tasks)
    return jsonify(tasks[-1]), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def replace_task(task_id):
    payload = request.get_json() or {}
    new_description = payload.get("description", "").strip()
    if not new_description:
        return jsonify({"error": "description required"}), 400
    tasks = read_tasks()
    if 0 <= task_id < len(tasks):
        edit_task(tasks, str(task_id + 1), new_description)
        write_tasks(tasks)
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "task not found"}), 404

@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    tasks = read_tasks()
    if 0 <= task_id < len(tasks):
        mark_task_complete(tasks, str(task_id + 1))
        write_tasks(tasks)
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    tasks = read_tasks()
    if 0 <= task_id < len(tasks):
        delete_task(tasks, str(task_id + 1))
        write_tasks(tasks)
        return jsonify({"status": "deleted"}), 200
    return jsonify({"error": "task not found"}), 404

# Simple search endpoint alternative (GET /search?q=)
@app.route("/search", methods=["GET"])
def search_endpoint():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify([]), 200
    tasks = read_tasks()
    return jsonify(search_tasks(tasks, q)), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
