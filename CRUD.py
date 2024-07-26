import json

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open('todo.json', 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open('todo.json', 'w') as file:
            json.dump(self.tasks, file)

    def display_tasks(self):
        t =""
        if not self.tasks:
            t = "No tasks found."
        else:
            
            for index, task in enumerate(self.tasks, start=1):
                t+=f"{index}. {task}\n"
        return t.strip()
    
    def display_tasks_from_index(self,index):
        if 0 < index <= len(self.tasks):
            #[(1, 'apple'), (2, 'banana'), (3, 'cherry')]
            hold = list(enumerate(self.tasks, start=1))
            # (index , example task)
            result = hold[index - 1]
            return result[1] 
        else:
            return "Invalid task index."
            
    def add_task(self, new_task):
        self.tasks.append(new_task)
        self.save_tasks()
        return "Task added successfully."

    def update_task(self, index, updated_task):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1] = updated_task
            self.save_tasks()
            return "Task updated successfully."
        else:
            return "Invalid task index."

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
            self.save_tasks()
            return "Task deleted successfully."
        else:
            return "Invalid task index."
