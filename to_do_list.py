# File: todo_list.py

# Function to load tasks from the file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]  # Remove any extra spaces/newlines
    except FileNotFoundError:
        tasks = []  # If the file doesn't exist, start with an empty list
    return tasks

# Function to save tasks to the file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main function
def todo_list():
    filename = "tasks.txt"
    tasks = load_tasks(filename)  # Load tasks from file if they exist
    
    while True:
        print("\nChoose an option:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # View tasks
            display_tasks(tasks)
        
        elif choice == '2':
            # Add a new task
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added to the list.")
        
        elif choice == '3':
            # Remove a task
            display_tasks(tasks)
            if tasks:
                try:
                    task_number = int(input("Enter the task number to remove: "))
                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed from the list.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == '4':
            # Save tasks and exit
            save_tasks(filename, tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

# Run the to-do list application
todo_list()


