# To-Do List Application in Python

# List to store the tasks
tasks = []

# Function to display the menu options
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

# Function to add a new task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\nCurrent To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# Function to delete a task by its index
def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        view_tasks()
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main loop to run the application
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the To-Do List application
if __name__ == "__main__":
    main()
