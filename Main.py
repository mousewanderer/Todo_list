from tkinter import *
from tkinter import messagebox
#Built in
import CRUD

td = CRUD.TodoList()

def Display():
    label.config(text=f"{td.display_tasks()}")


def insertTask():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Please enter a task.")
        return 
    else:
        td.add_task(enterTaskField.get())
        clear_taskField()
        label.config(text=f"{td.display_tasks()}")
    

def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_taskField():
    enterTaskField.delete(0, END)


def delete():
    if len(list(td.load_tasks())) == 0:
        messagebox.showerror("No tasks", "There are no tasks to delete.")
        return
    number = taskNumberField.get(1.0, END)
    if number == "\n":
        messagebox.showerror("Input Error", "Please enter a task number to delete.")
        return
    else:
        try:
            task_no = int(number)
        except:
            messagebox.showerror("Input Error", "Please enter a number to delete.")
            
    clear_taskNumberField()
    try:
        if task_no > len(td.load_tasks()):
            messagebox.showerror("Input Error", "Invalid task number.")
            return
        td.delete_task(task_no)

        TextArea.delete(1.0, END)
        label.config(text=f"{td.display_tasks()}")
    except:
        pass

def Updatation():
    if len(list(td.load_tasks())) == 0:
        messagebox.showerror("No tasks", "There are no tasks to update.")
        return

    try:
        tasknum = Update_NumberField.get(1.0, END)
        con = UpdateContent.get()
    except:
        pass
    
    if tasknum == "\n":
        messagebox.showerror("Input Error", "Please enter a task number to update.")
        return
    else:
        try:
            no = int(tasknum)
        except:
            messagebox.showerror("Input Error", "Please enter a number to update.")


    try:
        if no > len(td.load_tasks()):
            messagebox.showerror("Input Error", "Invalid task number.")
            return

        if con == "":
            messagebox.showerror("Input Error", "Please enter task to update.")
            return

        td.update_task(no,con)
        UpdateContent.delete(0, END)
        label.config(text=f"{td.display_tasks()}")
    except:
        pass



def search():
    if len(list(td.load_tasks())) == 0:
        messagebox.showerror("No tasks", "There are no tasks to Search.")
        return
    number = searchField.get(1.0, END)
    if number == "\n":
        messagebox.showerror("Input Error", "Please enter a task number to search.")
        return
    else:
        try:
            task_no = int(number)
        except:
            messagebox.showerror("Input Error", "Please enter a number to search.")
            
    searchField.delete(0.0, END)
    
    try:
        if task_no > len(td.load_tasks()):
            messagebox.showerror("Input Error", "Invalid task number.")
            return
        label.config(text=f"{td.display_tasks_from_index(task_no)}")
    except:
        pass
        
black = "#003b00"
green =  "#008f11" #islam
green1 = "#00ff41" #Malachi

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background=black)  
    gui.title("To Do List App ")
    gui.geometry("720x720")
    
#display            
    label = Label(gui, text="Blank", font=("Arial", 14), bg=black, fg=green1)
    displayButton = Button(gui, text="Display", command=Display , bg=black, fg=green1, font=("Arial", 12, "bold"))
    TextArea = Text(gui, height=8, width=30, font=("Arial", 10), bg=green, fg=green1)


 
    
#Add task 
    enterTask = Label(gui, text="Enter Your Task:", bg=black, fg=green1, font=("Arial", 12, "bold"))
    enterTaskField = Entry(gui, font=("Arial", 10), bg=green, fg=green1)
    Submit = Button(gui, text="Add Task", fg=green1, bg=black, command=insertTask, font=("Arial", 10, "bold"))
#_______________________________________________________________________________________________________________

# update task:
    
    Update_number = Label(gui, text="Update Task Number:", bg=black, fg=green1, font=("Arial", 12, "bold"))
    Update_NumberField = Text(gui, height=1, width=3, font=("Arial", 10),bg=green,fg=green1)
    Update_text = Label(gui, text="Update Task", bg=black, fg=green1, font=("Arial", 12, "bold"))
    UpdateContent = Entry(gui, font=("Arial", 10), bg=green, fg=green1)
    update = Button(gui, text="Update", fg=green1, bg=black, command=Updatation, font=("Arial", 10, "bold"))


#_______________________________________________________________________________________________________________

# Delete task
    taskNumber = Label(gui, text="Delete Task Number:", bg=black, fg=green1, font=("Arial", 12, "bold"))
    taskNumberField = Text(gui, height=1, width=3, font=("Arial", 10),bg=green,fg=green1)
    delete = Button(gui, text="Delete", fg=green1, bg=black, command=delete, font=("Arial", 10, "bold"))

#_______________________________________________________________________________________________________________

#Search task
    searchNumber = Label(gui, text="Search Task Number:", bg=black, fg=green1, font=("Arial", 12, "bold"))
    searchField = Text(gui, height=1, width=3, font=("Arial", 10),bg=green,fg=green1)
    searcher = Button(gui, text="Search", fg=green1, bg=black, command=search, font=("Arial", 10, "bold"))


    #_____position area________
    label.pack(pady=10)
    
    #display part
    displayButton.pack(pady=(0,10))
    enterTask.pack(pady=(20,5))
    enterTaskField.pack(pady=(0,10))
    Submit.pack(pady=(0,10))

    #update part
    Update_number.pack(pady=(0,5))
    Update_NumberField.pack(pady=(0,10))
    Update_text.pack(pady=(0,10))
    UpdateContent.pack(pady=(0,10))    
    update.pack(pady=(0,10))

    #delete part
    taskNumber.pack(pady=(0,5))
    taskNumberField.pack(pady=(0,10))
    delete.pack(pady=(0,10))

    #search part
    searchNumber.pack(pady=(0,5))
    searchField.pack(pady=(0,10))
    searcher.pack(pady=(0,10))
    

    gui.mainloop()
