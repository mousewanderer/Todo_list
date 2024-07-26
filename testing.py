import CRUD

td = CRUD.TodoList()

# Main function
def main():
    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Search Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("To do List")
            print(td.display_tasks())
        elif choice == '2':
            new_task = input("Enter the new task: ")
            print(td.add_task(new_task))
        elif choice == '3':
            print(td.display_tasks())
            index = int(input("Enter the index of the task to update: "))
            updated_task = input("Enter the updated task: ")
            print(td.update_task(index, updated_task))
        elif choice == '4':
            print(td.display_tasks())
            index = int(input("Enter the index of the task to delete: "))
            print(td.delete_task(index))
        elif choice == '5':
            index = int(input("Enter the index of the task to search: "))
            print(td.display_tasks_from_index(index))   
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
