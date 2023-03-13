# __________CLOCK____________

import datetime

logs = []

def log():
    global logs
    now = datetime.datetime.now()
    command = input("Enter your command: ")
    logs.append("{}.{}.{} :: {}:{} ==> {}".format(now.year, now.month, now.day, now.hour, now.minute, command))

def print_logs(l):
    for log in l:
        print(log)

def main():
    while True:
        choice = input("Main Menu:\n"
                       "Enter 1 to write the log\n"
                       "Enter 2 to print the logs\n"
                       "Enter 3 to exit\n"
                       "Enter your choice: ")
        if choice == "1":
            log()
        elif choice == "2":
            print_logs(logs)
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
