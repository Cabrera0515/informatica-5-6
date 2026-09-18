def main():
    tasks = []
    while True:
        print(f"You have {len(tasks)} tasks to do.")
        print(tasks)
        command = input("what do you want to do? (add, complete, or end): ").lower()
        command == "add"
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        elif command == "change task position":
            new_task = input("Enter task: ")
        elif command == "stop":
            break

if __name__ == "__main__":
        main()
