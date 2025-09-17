# todo_functions.py
import json
import os
from typing import List, Dict

def _normalize_path(filename):
    # Accept path-like objects from pytest tmp_path
    return str(filename)

def load_tasks(filename="tasks.json"):
    """Loads tasks from a JSON file. Returns an empty list if the file is not found or invalid."""
    filename = _normalize_path(filename)
    if not os.path.exists(filename):
        return []
    try:
        if os.path.getsize(filename) == 0:
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []  # Return empty list if JSON is invalid or file can't be read

def save_tasks(task_list: List[Dict], filename="tasks.json"):
    """Saves the current tasks to a JSON file."""
    filename = _normalize_path(filename)
    # Ensure folder exists
    dirpath = os.path.dirname(filename)
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath, exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(task_list, f, ensure_ascii=False, indent=4)

def add_task(task_list, task_description):
    """Adds a new task to the list, preventing empty or whitespace-only tasks."""
    if not task_description or not task_description.strip():
        print("\n❌ Error: Task description cannot be empty.")
        return
    task = {"description": task_description, "status": "incomplete"}
    task_list.append(task)
    print(f"\n✅ Task added: '{task_description}'")

def view_tasks(task_list):
    """Displays all tasks in the list with their status and number."""
    print("\n--- Your To-Do List ---")
    if not task_list:
        print("Your list is empty. Add a task to get started!")
    else:
        for idx, task in enumerate(task_list):
            status_marker = "[X]" if task["status"] == "complete" else "[ ]"
            print(f"{idx + 1}. {status_marker} {task['description']}")
    print("-----------------------\n")

def delete_task(task_list, task_number_str):
    """Deletes a task based on its 1-based number, with error handling."""
    try:
        task_index = int(task_number_str) - 1
        if 0 <= task_index < len(task_list):
            removed_task = task_list.pop(task_index)
            print(f"\n🗑️ Task '{removed_task['description']}' has been deleted.")
        else:
            print(f"\n❌ Error: Invalid task number. Please enter a number between 1 and {len(task_list)}.")
    except ValueError:
        print("\n❌ Error: Please enter a valid number.")

def mark_task_complete(task_list, task_number_str):
    """Marks a task as complete based on its 1-based number, with error handling."""
    try:
        task_index = int(task_number_str) - 1
        if 0 <= task_index < len(task_list):
            if task_list[task_index]["status"] == "complete":
                print(f"\n🤔 Task {task_index + 1} was already marked as complete.")
            else:
                task_list[task_index]["status"] = "complete"
                print(f"\n🎉 Great job! Marked task {task_index + 1} as complete.")
        else:
            print(f"\n❌ Error: Invalid task number. Please enter a number between 1 and {len(task_list)}.")
    except ValueError:
        print("\n❌ Error: Please enter a valid number.")

def edit_task(task_list, task_number_str, new_description):
    """Edits a task, preventing empty or whitespace-only descriptions."""
    if not new_description or not new_description.strip():
        print("\n❌ Error: New task description cannot be empty.")
        return
    try:
        task_index = int(task_number_str) - 1
        if 0 <= task_index < len(task_list):
            original_description = task_list[task_index]["description"]
            task_list[task_index]["description"] = new_description
            print(f"\n✏️ Task '{original_description}' has been updated to '{new_description}'.")
        else:
            print(f"\n❌ Error: Invalid task number. No task updated.")
    except ValueError:
        print("\n❌ Error: Please enter a valid number.")

def search_tasks(task_list, keyword):
    """Searches for tasks, returning an empty list for empty or whitespace-only keywords."""
    if not keyword or not keyword.strip():
        return []

    found_tasks = [task for task in task_list if keyword.lower() in task['description'].lower()]

    # For API usage, return the matches (printing kept for CLI compatibility)
    print(f"\n--- Search Results for '{keyword}' ---")
    if not found_tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(found_tasks):
            status_marker = "[X]" if task["status"] == "complete" else "[ ]"
            print(f"{idx + 1}. {status_marker} {task['description']}")
    print("--------------------------------------")
    return found_tasks
