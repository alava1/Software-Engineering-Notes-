# todo_list.py - Intermediate Project
# Features: Add, View, Complete, Delete tasks + File persistence

import json
from datetime import datetime

TASKS_FILE = "tasks.json"

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump(self.tasks, file, indent=2)
    
    def add_task(self, description):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "completed": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            print(f"{task['id']}. [{status}] {task['description']} ({task['created']})")
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print("✅ Task marked as completed!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self.save_tasks()
        print("🗑️ Task deleted.")

# Main program
if __name__ == "__main__":
    todo = TodoList()
    print("=== Advanced To-Do List ===\n")
    
    while True:
        print("\n1. Add Task | 2. View Tasks | 3. Complete Task | 4. Delete Task | 5. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            desc = input("Task description: ")
            todo.add_task(desc)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            try:
                tid = int(input("Task ID to complete: "))
                todo.complete_task(tid)
            except ValueError:
                print("Invalid ID!")
        elif choice == "4":
            try:
                tid = int(input("Task ID to delete: "))
                todo.delete_task(tid)
            except ValueError:
                print("Invalid ID!")
        elif choice == "5":
            print("Goodbye!")
            break
