# mini project 1 : to-do list manager

todo_list = []

def manage_todo():
    todo_list.append(input("Enter task: ")) # add task
    print(f"Tasks: {todo_list}")
    if len(todo_list) > 0:
        todo_list.pop(0) # remove first task
    print(f"Updated Tasks: {todo_list}")

manage_todo()

# output
"""
Enter task: hi
Tasks: ['hi']
Updated Tasks: []
"""