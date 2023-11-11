# Initialize an empty list to store tasks
tasks = []

while True:
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Complete")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        status = "Incomplete"
        
        task = {
            "Name": name,
            "Description": description,
            "Due Date": due_date,
            "Status": status
        }
        
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Name: {task['Name']}, Description: {task['Description']}, Due Date: {task['Due Date']}, Status: {task['Status']}")

    elif choice == "3":
        index = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["Status"] = "Complete"
            print("Task marked as complete!")
        else:
            print("Invalid task number!")

    elif choice == "4":
        # Save tasks to a file (optional)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(f"{task['Name']},{task['Description']},{task['Due Date']},{task['Status']}\n")
        print("Tasks saved to 'tasks.txt'")
        break

    else:
        print("Invalid choice. Please select a valid option.")
