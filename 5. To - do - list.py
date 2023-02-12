def show_list(todos):
    if not todos:
        print("No items in the To-Do List.")
        return
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")

def add_task(todos):
    task = input("Enter the task to add to the To-Do List: ")
    todos.append(task)
    print(f"{task} added to the To-Do List.")

def edit_task(todos):
    show_list(todos)
    idx = int(input("Enter the index of the task to edit: "))
    try:
        task = todos[idx - 1]
    except IndexError:
        print("Invalid index.")
        return
    new_task = input("Enter the new task: ")
    todos[idx - 1] = new_task
    print(f"Task at index {idx} edited to {new_task}.")

def delete_task(todos):
    show_list(todos)
    idx = int(input("Enter the index of the task to delete: "))
    try:
        task = todos.pop(idx - 1)
    except IndexError:
        print("Invalid index.")
        return
    print(f"Task {task} at index {idx} deleted.")

def main():
    todos = []
    while True:
        print("\n1. Show List")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_list(todos)
        elif choice == 2:
            add_task(todos)
        elif choice == 3:
            edit_task(todos)
        elif choice == 4:
            delete_task(todos)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
