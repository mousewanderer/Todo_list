

#_____________________TODO - List________________________________________________
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext  # For scrollable text area
# Built in
import CRUD

td = CRUD.TodoList()

def Display():
    task_list.insert(1.0,td.display_tasks())
    

def update_display():
    task_list.delete(1.0, END)
    task_list.insert(END, td.display_tasks())

def insert_task():
    if enter_task_field.get() == "":
        messagebox.showerror("Input Error", "Please enter a task.")
        return 
    else:
        td.add_task(enter_task_field.get())
        clear_task_field()
        update_display()

def clear_task_field():
    enter_task_field.delete(0, END)

def delete_task():
    if len(list(td.load_tasks())) == 0:
        messagebox.showerror("No tasks", "There are no tasks to delete.")
        return
    number = task_number_field.get(1.0, END).strip()
    if not number:
        messagebox.showerror("Input Error", "Please enter a task number to delete.")
        return
    try:
        task_no = int(number)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number to delete.")
        return

    if task_no > len(td.load_tasks()):
        messagebox.showerror("Input Error", "Invalid task number.")
        return

    td.delete_task(task_no)
    clear_task_number_field()
    update_display()

def clear_task_number_field():
    task_number_field.delete(1.0, END)

def update_task():
    if len(list(td.load_tasks())) == 0:
        messagebox.showerror("No tasks", "There are no tasks to update.")
        return

    task_num = update_number_field.get(1.0, END).strip()
    new_content = update_content_field.get()

    if not task_num:
        messagebox.showerror("Input Error", "Please enter a task number to update.")
        return
    if not new_content:
        messagebox.showerror("Input Error", "Please enter the new task content.")
        return

    try:
        task_no = int(task_num)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number to update.")
        return

    if task_no > len(td.load_tasks()):
        messagebox.showerror("Input Error", "Invalid task number.")
        return

    td.update_task(task_no, new_content)
    clear_update_fields()
    update_display()

def clear_update_fields():
    update_number_field.delete(1.0, END)
    update_content_field.delete(0, END)
#------------------------------------------------------------------------------------------------------
def search_task():
    if len(list(td.load_tasks())) == 0:
        messagebox.showerror("No tasks", "There are no tasks to search.")
        return
    
    number = search_field.get(1.0, END).strip()
    if not number:
        # If a number is not entered and the display already shows a search result, reset it
        if task_list.get(1.0, END).strip() != td.display_tasks().strip():
            task_list.delete(1.0, END)
            task_list.insert(END, td.display_tasks())
        else:
            messagebox.showerror("Input Error", "Please enter a task number to search.")
        return

    try:
        task_no = int(number)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number to search.")
        return

    if task_no > len(td.load_tasks()) or task_no <= 0:
        messagebox.showerror("Input Error", "Invalid task number.")
        return

    # Show the search result
    search_result = td.display_tasks_from_index(task_no)
    if task_list.get(1.0, END).strip() == search_result.strip():
        # If the search result is already displayed, reset to the full task list
        task_list.delete(1.0, END)
        task_list.insert(END, td.display_tasks())
    else:
        # Display the search result
        task_list.delete(1.0, END)
        task_list.insert(END, search_result)

    # Clear the search field
    search_field.delete(1.0, END)
#------------------------------------------------------------------------------------------------------
# UI colors
black = "#003b00" #Romanian Vampire
green =  "#008f11" #islam
green1 = "#00ff41" #Malachi

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background=black)
    gui.title("To Do List App")
    gui.geometry("720x720")

    # ----------------------- Task display(It can scroll) -----------------------
    label = Label(gui, text="Tasks:", font=("Arial", 14), bg=black, fg=green1)
    task_list = scrolledtext.ScrolledText(gui, height=10, width=50, font=("Arial", 10), bg=green, fg=green1)
    task_list.configure(state=NORMAL)

    # ----------------------- Add task part -----------------------
    enter_task_label = Label(gui, text="Enter Your Task:", bg=black, fg=green1, font=("Arial", 12, "bold"))
    enter_task_field = Entry(gui, font=("Arial", 10), bg=green, fg=green1)
    add_task_button = Button(gui, text="Add Task", fg=green1, bg=black, command=insert_task, font=("Arial", 10, "bold"))

    # ----------------------- Update task part -----------------------
    update_number_label = Label(gui, text="Update Task Number:", bg=black, fg=green1, font=("Arial", 12, "bold"))
    update_number_field = Text(gui, height=1, width=3, font=("Arial", 10), bg=green, fg=green1)
    update_content_label = Label(gui, text="Update Task Here:", bg=black, fg=green1, font=("Arial", 12, "bold"))
    update_content_field = Entry(gui, font=("Arial", 10), bg=green, fg=green1)
    update_task_button = Button(gui, text="Update Task", fg=green1, bg=black, command=update_task, font=("Arial", 10, "bold"))

    #----------------------- Delete task Part -----------------------
    task_number_label = Label(gui, text="Delete Task Number:", bg=black, fg=green1, font=("Arial", 12, "bold"))
    task_number_field = Text(gui, height=1, width=3, font=("Arial", 10), bg=green, fg=green1)
    delete_task_button = Button(gui, text="Delete Task", fg=green1, bg=black, command=delete_task, font=("Arial", 10, "bold"))

    # -----------------------Search task Part -----------------------
    search_label = Label(gui, text="Search Task Number (Click 2x to return display): ", bg=black, fg=green1, font=("Arial", 12, "bold"))
    search_field = Text(gui, height=1, width=3, font=("Arial", 10), bg=green, fg=green1)
    search_task_button = Button(gui, text="Search Task", fg=green1, bg=black, command=search_task, font=("Arial", 10, "bold"))

    # Layout
    label.pack(pady=10)
    task_list.pack(pady=(0, 20))

    enter_task_label.pack(pady=(10, 5))
    enter_task_field.pack(pady=(0, 5))
    add_task_button.pack(pady=(0, 10))

    update_number_label.pack(pady=(10, 5))
    update_number_field.pack(pady=(0, 5))
    update_content_label.pack(pady=(10, 5))
    update_content_field.pack(pady=(0, 5))
    update_task_button.pack(pady=(0, 10))

    task_number_label.pack(pady=(10, 5))
    task_number_field.pack(pady=(0, 5))
    delete_task_button.pack(pady=(0, 10))

    search_label.pack(pady=(10, 5))
    search_field.pack(pady=(0, 5))
    search_task_button.pack(pady=(0, 10))
    # Automatically display tasks on startup
    Display()

    gui.mainloop()

