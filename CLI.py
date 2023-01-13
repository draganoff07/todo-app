#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%a %d %b %Y - %H:%M")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith("complete"):

        try:
            complete = int(user_action[9:])
            index = complete - 1
            completed = todos[index].strip("\n")
            todos = functions.get_todos()
            todos.pop(index)
            functions.write_todos(todos)
            message = f"{completed}  was done"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    else:
        print("Try again")
print("Bye!")
