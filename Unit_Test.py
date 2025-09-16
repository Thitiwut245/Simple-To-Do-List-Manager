# test_todo_functions.py
import pytest
from todo_functions import add_task, delete_task, mark_task_complete, edit_task, search_tasks, load_tasks, save_tasks

# A simple test fixture to ensure each test starts with a clean list
@pytest.fixture
def empty_tasks():
    return []

@pytest.fixture
def sample_tasks():
    tasks = [{"description": "Task 1", "status": "incomplete"}, 
             {"description": "Task 2", "status": "incomplete"}]
    return tasks

def test_add_task(empty_tasks):
    add_task(empty_tasks, "Test Task")
    assert len(empty_tasks) == 1
    assert empty_tasks[0]['description'] == "Test Task"

def test_delete_task_success(sample_tasks):
    initial_len = len(sample_tasks)
    delete_task(sample_tasks, "1")
    assert len(sample_tasks) == initial_len - 1
    assert sample_tasks[0]['description'] == "Task 2"

def test_mark_task_complete_success(sample_tasks):
    mark_task_complete(sample_tasks, "1")
    assert sample_tasks[0]['status'] == "complete"

def test_edit_task_success(sample_tasks):
    edit_task(sample_tasks, "1", "Updated Task")
    assert sample_tasks[0]['description'] == "Updated Task"

def test_search_tasks_finds_item(sample_tasks):
    results = search_tasks(sample_tasks, "Task 1")
    assert len(results) == 1
    assert results[0]['description'] == "Task 1"
def test_delete_task_invalid_index(sample_tasks):
    """Tests that deleting a task with an out-of-bounds index does not change the list."""
    initial_tasks = list(sample_tasks)  # Make a copy to compare against
    delete_task(sample_tasks, "99")  # "99" is an invalid index
    assert sample_tasks == initial_tasks

def test_delete_task_non_numeric_input(sample_tasks):
    """Tests that deleting a task with non-numeric input does not change the list."""
    initial_tasks = list(sample_tasks)
    delete_task(sample_tasks, "abc")  # "abc" is not a number
    assert sample_tasks == initial_tasks
def test_search_tasks_no_results(sample_tasks):
    """Tests that searching for a non-existent task returns an empty list."""
    results = search_tasks(sample_tasks, "nonexistent")
    assert results == []
def test_save_and_load_tasks(tmp_path):
    """Tests that tasks can be saved to and loaded from a file correctly."""
    # 1. Setup
    tasks_to_save = [{"description": "Check file saving", "status": "complete"}]
    test_file = tmp_path / "temp_tasks.json" # Creates a temporary file path

    # 2. Action: Save and then load the tasks
    save_tasks(tasks_to_save, test_file)
    loaded_tasks = load_tasks(test_file)

    # 3. Assert: The loaded data should be the same as the original
    assert loaded_tasks == tasks_to_save
def test_mark_task_complete_invalid_index(sample_tasks):
    """Tests that marking a task complete with an out-of-bounds index does not change the task status."""
    initial_status = sample_tasks[0]['status']
    mark_task_complete(sample_tasks, "99")  # "99" is an invalid index
    assert sample_tasks[0]['status'] == initial_status
def test_edit_task_invalid_index(sample_tasks):
    """Tests that editing a task with an out-of-bounds index does not change the list."""
    initial_tasks = list(sample_tasks)
    edit_task(sample_tasks, "99", "This should not work")
    assert sample_tasks == initial_tasks

def test_edit_task_non_numeric_input(sample_tasks):
    """Tests that editing a task with non-numeric input does not change the list."""
    initial_tasks = list(sample_tasks)
    edit_task(sample_tasks, "abc", "This should not work")
    assert sample_tasks == initial_tasks
def test_add_task_empty_description(empty_tasks):
    """Tests that adding a task with an empty description does not add to the list."""
    initial_len = len(empty_tasks)
    add_task(empty_tasks, "")
    assert len(empty_tasks) == initial_len
def test_add_task_whitespace_description(empty_tasks):
    """Tests that adding a task with only whitespace does not add to the list."""
    initial_len = len(empty_tasks)
    add_task(empty_tasks, "   ")
    assert len(empty_tasks) == initial_len
def test_load_tasks_nonexistent_file(tmp_path):
    """Tests that loading tasks from a non-existent file returns an empty list."""
    non_existent_file = tmp_path / "nonexistent.json"
    loaded_tasks = load_tasks(non_existent_file)
    assert loaded_tasks == []
def test_load_tasks_invalid_json(tmp_path):
    """Tests that loading tasks from a file with invalid JSON returns an empty list."""
    invalid_json_file = tmp_path / "invalid.json"
    invalid_json_file.write_text("This is not JSON")
    loaded_tasks = load_tasks(invalid_json_file)
    assert loaded_tasks == []
def test_save_tasks_creates_file(tmp_path):
    """Tests that saving tasks creates a file."""
    tasks_to_save = [{"description": "Check file creation", "status": "incomplete"}]
    test_file = tmp_path / "created_tasks.json"
    save_tasks(tasks_to_save, test_file)
    assert test_file.exists()
def test_save_tasks_overwrites_file(tmp_path):
    """Tests that saving tasks overwrites an existing file."""
    tasks_to_save = [{"description": "First task", "status": "incomplete"}]
    test_file = tmp_path / "overwrite_tasks.json"
    save_tasks(tasks_to_save, test_file)

    # Save again with different content
    new_tasks_to_save = [{"description": "Second task", "status": "complete"}]
    save_tasks(new_tasks_to_save, test_file)

    loaded_tasks = load_tasks(test_file)
    assert loaded_tasks == new_tasks_to_save
def test_mark_task_complete_already_complete(sample_tasks):
    """Tests that marking an already complete task does not change its status."""
    mark_task_complete(sample_tasks, "1")  # Mark first task as complete
    initial_status = sample_tasks[0]['status']
    mark_task_complete(sample_tasks, "1")  # Try to mark it complete again
    assert sample_tasks[0]['status'] == initial_status
def test_edit_task_empty_description(sample_tasks):
    """Tests that editing a task to have an empty description does not change the task."""
    initial_description = sample_tasks[0]['description']
    edit_task(sample_tasks, "1", "")  # Attempt to set description to empty
    assert sample_tasks[0]['description'] == initial_description
def test_edit_task_whitespace_description(sample_tasks):
    """Tests that editing a task to have only whitespace does not change the task."""
    initial_description = sample_tasks[0]['description']
    edit_task(sample_tasks, "1", "   ")  # Attempt to set description to whitespace
    assert sample_tasks[0]['description'] == initial_description
def test_search_tasks_case_insensitive(sample_tasks):
    """Tests that searching for tasks is case-insensitive."""
    results = search_tasks(sample_tasks, "task 1")
    assert len(results) == 1
    assert results[0]['description'] == "Task 1"
def test_search_tasks_partial_match(sample_tasks):
    """Tests that searching for a partial match returns the correct tasks."""
    results = search_tasks(sample_tasks, "Task")
    assert len(results) == 2  # Both tasks contain "Task"
def test_search_tasks_empty_keyword(sample_tasks):
    """Tests that searching with an empty keyword returns an empty list."""
    results = search_tasks(sample_tasks, "")
    assert results == []
def test_search_tasks_whitespace_keyword(sample_tasks):
    """Tests that searching with a whitespace keyword returns an empty list."""
    results = search_tasks(sample_tasks, "   ")
    assert results == []
def test_load_tasks_empty_file(tmp_path):
    """Tests that loading tasks from an empty file returns an empty list."""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("")  # Create an empty file
    loaded_tasks = load_tasks(empty_file)
    assert loaded_tasks == []
def test_save_tasks_empty_list(tmp_path):
    """Tests that saving an empty task list creates a file with an empty list."""
    empty_tasks = []
    test_file = tmp_path / "empty_tasks.json"
    save_tasks(empty_tasks, test_file)
    loaded_tasks = load_tasks(test_file)
    assert loaded_tasks == empty_tasks
def test_save_tasks_special_characters(tmp_path):
    """Tests that saving tasks with special characters works correctly."""
    tasks_to_save = [{"description": "Task with emoji 😊", "status": "incomplete"},
                     {"description": "Task with newline\nSecond line", "status": "complete"}]
    test_file = tmp_path / "special_char_tasks.json"
    save_tasks(tasks_to_save, test_file)
    loaded_tasks = load_tasks(test_file)
    assert loaded_tasks == tasks_to_save
def test_load_tasks_large_file(tmp_path):
    """Tests that loading a large number of tasks works correctly."""
    large_tasks = [{"description": f"Task {i}", "status": "incomplete"} for i in range(1000)]
    test_file = tmp_path / "large_tasks.json"
    save_tasks(large_tasks, test_file)
    loaded_tasks = load_tasks(test_file)
    assert loaded_tasks == large_tasks