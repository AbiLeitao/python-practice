# PERSONAL TASK MANAGER

# Option 1 - view tasks from file in a individual string format
# Option 2 - append new task to end of file
# Option 3 - mark task as done
# Option 4 - delete task
# Option 5 - exit task manager

import csv 

tasks = []

#Open CSV file, transfer each row to tasks list
with open('to_do.csv', 'r', newline = '') as to_do_csv:
    to_do_list = csv.reader(to_do_csv)
    for row in to_do_list:
        tasks.append(row[0])

# Option 1 - View all tasks (both complete and incomplete)
def view_tasks():        
    print("All tasks: ")
    for i in range(0, len(tasks)):
        task_num = i + 1
        task = tasks[i]
        print(f"{task_num}. {task}")
    print("\nChoose an option from 1 - 5")

# Option 2 - Add new tasks to task manager
def add_task():  
    new_task = input("Enter task description: ")
    tasks.append("[ ] " + new_task)
    print("Task added successfully! \nChoose an option from 1 - 5")
    return tasks

# Option 3 - Mark a task as done 
def task_done(): 
    task_num = int(input("Enter the task number to mark as completed: "))
    current_task = tasks[task_num - 1]
    tasks[task_num - 1] = "[x] " + current_task[3:]
    print("Task successfully marked as completed")
    print("\nChoose an option from 1 - 5")
    return False

# Option 4 - Delete task from list
def delete_task(): # Option 4
    task_num = int(input("Enter the task number to mark as completed: "))
    task_deleted = tasks[task_num - 1]
    tasks.remove(task_deleted)
    print(f"Task '{task_deleted[4:]}' has been deleted")
    print("\nChoose an option from 1 - 5")
    return False

def main():
    
    # Opening message with action options
    print("Welcome to your task manager! Choose from one of the following options")
    print("1. View tasks")
    print("2. Add tasks")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit Task Manager")
    
    while True:
        user_inp = input("")
        # 1. View tasks
        if user_inp == "1":
            view_tasks()
        # 2. Add tasks
        elif user_inp == "2":
            add_task()
        # 3. Mark task as done
        elif user_inp == "3":
            task_done()
        # 4. Delete tasks
        elif user_inp == "4":
            delete_task()
        # 5. Close task manager
        elif user_inp == "5":
            print("Goodbye!")
            break
        # Message for incorrect input
        else:
            print("Incorrect input. Please choose from options 1-5")

main()

# Write current task list to CSV file (overwrite current contents) when task manager is closed
with open('to_do.csv', 'w', newline = '') as to_do_csv:
    output_writer = csv.writer(to_do_csv)	
    for task in tasks:
        output_writer.writerow([task])
