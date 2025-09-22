from flask import Blueprint, request, jsonify
from backend.services.task_service import (
    add_task, get_tasks, get_task, update_task, delete_task,
    mark_task_complete, search_tasks
)   
from backend.services.ai_integration import categorize_text

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/", methods=["GET"])
def list_tasks():
    return jsonify(get_tasks())

@tasks_bp.route("/<int:task_id>", methods=["GET"])
def get_task_route(task_id):
    t = get_task(task_id)
    if not t:
        return jsonify({"error":"not found"}), 404
    return jsonify(t)

@tasks_bp.route("/", methods=["POST"])
def create_task_route():
    data = request.get_json() or {}
    title = data.get("title")
    if not title:
        return jsonify({"error":"title required"}), 400
    task = add_task(title, description=data.get("description",""), priority=data.get("priority","normal"), tags=data.get("tags",""))
    return jsonify(task), 201

@tasks_bp.route("/<int:task_id>", methods=["PUT"])
def update_task_route(task_id):
    data = request.get_json() or {}
    task = update_task(task_id, **data)
    if not task:
        return jsonify({"error":"not found"}), 404
    return jsonify(task)

@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task_route(task_id):
    ok = delete_task(task_id)
    return ("", 204) if ok else (jsonify({"error":"not found"}), 404)

@tasks_bp.route("/categorize", methods=["POST"])
def categorize_route():
    data = request.get_json() or {}
    text = data.get("text","")
    if not text:
        return jsonify({"error":"text required"}), 400
    return jsonify({"category": categorize_text(text)})
@tasks_bp.route("/<int:task_id>/complete", methods=["PUT"])
def complete_task_route(task_id):
    task = mark_task_complete(task_id)
    if not task:
        return jsonify({"error": "not found"}), 404
    return jsonify(task)

@tasks_bp.route("/search", methods=["GET"])
def search_tasks_route():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "query required"}), 400
    return jsonify(search_tasks(query))        