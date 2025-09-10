# Mini-Project 4: Simple To-Do List Manager

def add_task(task_list, task_description):
    task = {"description": task_description, "status": "incomplete"}
    task_list.append(task)
    print(f"\n✅ Task added: '{task_description}'")

# ---

def view_tasks(task_list):
    """
    Displays all tasks in the list with their status and number.
    """
    print("\n--- Your To-Do List ---")
    if not task_list:
        print("Your list is empty. Add a task to get started!")
    else:
        for idx, task in enumerate(task_list):
            # Determine the status marker
            status_marker = "[X]" if task["status"] == "complete" else "[ ]"
            # Print the formatted task string
            print(f"{idx + 1}. {status_marker} {task['description']}")
    print("-----------------------\n")

# ---
def delete_task(task_list, task_number):
    """
    Deletes a task based on its 1-based number.
    """
    try:
        task_index = int(task_number) - 1
        if 0 <= task_index < len(task_list):
            removed_task = task_list.pop(task_index)
            print(f"\n🗑️ Task '{removed_task['description']}' has been deleted.")
        else:
            print(f"\n❌ Error: Invalid task number. No task deleted.")
    except ValueError:
        print("\n❌ Error: Please enter a valid number.")
# ---
def edit_task(task_list, task_number, new_description):
    try:
        task_index = int(task_number) - 1
        if 0 <= task_index < len(task_list):
            task_list[task_index]["description"] = new_description
            print(f"\n✏️ Task {task_number} has been updated to '{new_description}'.")
        else:
            print(f"\n❌ Error: Invalid task number. No task updated.")
    except ValueError:
        print("\n❌ Error: Please enter a valid number.")
# ---
def search_tasks(task_list, keyword):
    found_tasks = [task for task in task_list if keyword.lower() in task['description'].lower()]
    print(f"\n--- Search Results for '{keyword}' ---")
    if not found_tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(found_tasks):
            status_marker = "[X]" if task["status"] == "complete" else "[ ]"
            print(f"{idx + 1}. {status_marker} {task['description']}")
    print("--------------------------------------\n")

# ---
def mark_task_complete(task_list, task_number):
    """
    Marks a task as complete based on its 1-based number.
    Includes error handling for invalid numbers.
    """
    # Convert 1-based task_number to 0-based list index
    task_index = task_number - 1

    # Debugging Focus: Check for index errors
    if 0 <= task_index < len(task_list):
        # Check if the task is already complete
        if task_list[task_index]["status"] == "complete":
            print(f"\n Task {task_number} was already marked as complete.")
        else:
            task_list[task_index]["status"] = "complete"
            print(f"\n🎉 Great job! Marked task {task_number} as complete.")
    else:
        # Handle the case where the number is out of the list's range
        print(f"\n❌ Error: Invalid task number. Please enter a number between 1 and {len(task_list)}.")

# ---

def main():
    """
    The main function to run the to-do list application loop.
    """
    # The list in memory to store our tasks
    tasks = []

    while True:
        # Display the menu to the user
        print("Choose an action:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View all tasks")
        print("4. Mark a task as complete")
        print("5. Edit a task")
        print("6. Search for tasks")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            description = input("Enter the task description: ").strip() # Clean the input
            if description: # Check if the string is not empty
                add_task(tasks, description)
            else:
                print("\n❌ Error: Task description cannot be empty. Please try again.")

        elif choice == '2':
            view_tasks(tasks)
            if tasks: # Only ask for input if there are tasks to delete
                task_num_str = input("Enter the number of the task to delete: ")
                delete_task(tasks, task_num_str)

        elif choice == '3':
            view_tasks(tasks)

        elif choice == '4':
            view_tasks(tasks)
            if not tasks:
                continue
            try:
                task_num_str = input("Enter the number of the task to mark as complete: ")
                task_num = int(task_num_str)
                mark_task_complete(tasks, task_num)
            except ValueError:
                print("\n❌ Error: Please enter a valid number.")
        elif choice == '5':
            view_tasks(tasks)
            if tasks:
                task_num_str = input("Enter the number of the task to edit: ")
                new_description = input("Enter the new task description: ").strip()
                if new_description:
                    edit_task(tasks, task_num_str, new_description)
                else:
                    print("\n❌ Error: Task description cannot be empty. Please try again.")
        elif choice == '6':
            keyword = input("Enter a keyword to search for: ").strip()
            if keyword:
                search_tasks(tasks, keyword)
            else:
                print("\n❌ Error: Keyword cannot be empty. Please try again.")
        elif choice == '7':
            print("\nHappy tasking! Goodbye. 👋")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")

# ---

# Run the main application
if __name__ == "__main__":
    main()