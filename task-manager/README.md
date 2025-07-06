# Task Manager CLI

A simple command-line task manager built in Python.
This app allows you to add, view, complete, and delete tasks, storing them in a CSV file so your tasks persist between runs.

## Features
* View all tasks (completed and incomplete)
* Add new tasks
* Mark tasks as completed
* Delete tasks
* Save tasks to a CSV file (to_do.csv)

## Getting Started
**Requirements**
Python 3.x

**Run the Program**

    python task_manager.py

The program will open a simple text-based menu where you can select options by typing numbers.

**Example**

    Welcome to your task manager! Choose from one of the following options
    1. View tasks
    2. Add tasks
    3. Mark task as done
    4. Delete a task
    5. Exit Task Manager

    1
    All tasks:
    1. [ ] Walk dog
    2. [x] Dishes
    3. [ ] Laundry

    Choose an option from 1 - 5

## Future Improvements (Ideas)
- Improve CSV file structure (split into separate columns for status and description)
- Add a search/filter feature
- Save data as JSON instead of CSV
- Create a GUI or web interface
- Add unit tests


## Why This Project?
This was built as a small project to practice:
* Reading and writing CSV files
* Using lists and loops
* Creating functions and basic program structure
* Building simple command-line interfaces
* Saving and loading data persistently

## License
This project is free to use and modify for learning purposes.