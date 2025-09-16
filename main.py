# main.py
from todo_functions import add_task, view_tasks, mark_task_complete, delete_task, edit_task, search_tasks, load_tasks, save_tasks  # Ensure todo_functions.py is in the same directory

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\nChoose an action:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Edit a task")
        print("5. Search for tasks")
        print("6. Delete a task")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            description = input("Enter the task description: ").strip()
            if description:
                add_task(tasks, description)
            else:
                print("\n❌ Error: Task description cannot be empty. Please try again.")
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            if tasks:
                task_num_str = input("Enter the number of the task to mark as complete: ")
                mark_task_complete(tasks, task_num_str)
        elif choice == '4':
            view_tasks(tasks)
            if tasks:
                task_num_str = input("Enter the number of the task to edit: ")
                new_description = input("Enter the new task description: ").strip()
                if new_description:
                    edit_task(tasks, task_num_str, new_description)
                else:
                    print("\n❌ Error: Task description cannot be empty. Please try again.")
        elif choice == '5':
            keyword = input("Enter a keyword to search for: ").strip()
            if keyword:
                search_tasks(tasks, keyword)
            else:
                print("\n❌ Error: Keyword cannot be empty. Please try again.")
        elif choice == '6':
            view_tasks(tasks)
            if tasks:
                task_num_str = input("Enter the number of the task to delete: ")
                delete_task(tasks, task_num_str)
        elif choice == '7':
            save_tasks(tasks)
            print("\nHappy tasking! Goodbye. 👋")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()