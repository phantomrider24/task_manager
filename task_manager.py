#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
user_names = []
pass_words = []

with open("user.txt", "r") as users_file:
    
    for line in users_file:
        temp = line.strip()
        temp = line.split(", ")

        user_names.append(temp[0])
        pass_words.append(temp[1].strip("\n"))
    users_file.close()


while True:    
    login_username = input("Username: ")
    login_password = input("Password: ")
    if (login_username in user_names) and (login_password in pass_words):
        print("Access Granted!\n")
        break
    elif (login_username in user_names) and (login_password not in pass_words):
        print("Username exist. Password is incorrect! Please try again")
    else:
        print("User does not exist. Please try again")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if login_username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - Statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()


    if (menu == 'r') and (login_username ==  "admin"):
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        user_name = input("Enter New username: ")
        pass_word = input("Enter New password: ")
        pass_word_confirmation = input("Enter password confirmation: ")
        if pass_word == pass_word_confirmation:
            user_string = f"\n{user_name}, {pass_word_confirmation}"

            with open("user.txt", "a") as users_file:
                users_file.write(user_string)
                users_file.close()
            print("User registered successfully!")
        else:
            print("Password confirmation doesn't match! Please try again")

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        user_name = input("Please enter the username you want to assign a task to: ")
        task_title = input("Task title: ")
        description_task = input("Task Description: ")
        due_date = input("Due Date of task(dd mon yyyy): ")
        current_date = datetime.now()
        date_format = current_date.strftime("%d %b %Y")

        with open("tasks.txt", "a") as tasks_file:
            task_string = f"\n{user_name}, {task_title}, {description_task}, {date_format}, {due_date}, No"
            tasks_file.write(task_string)
            tasks_file.close()

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        print("________________________________________________________________________________________________")
        with open("tasks.txt","r") as tasks_file:
            
            for line in tasks_file:
                temp = line.strip()
                temp = line.split(", ")

                user_name = temp[0]
                task_title = temp[1]
                description_task = temp[2]
                date_assigned = temp[3]
                due_date = temp[4]
                completion_check = temp[5].strip("\n")
                
                task_string = f"\nTask:\t\t\t{task_title}\nAssigned to:\t\t{user_name}\nDate assigned:\t\t{date_assigned}\nDue date:\t\t{due_date}\nTask Complete:\t\t{completion_check}\nTask description:\n {description_task}"
                print(task_string)
                print("________________________________________________________________________________________________")
            tasks_file.close()


    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        with open("tasks.txt","r") as tasks_file:
            print("________________________________________________________________________________________________")
            for line in tasks_file:
                temp = line.strip()
                temp = line.split(", ")

                user_name = temp[0]
                if user_name == login_username:
                    task_title = temp[1]
                    description_task = temp[2]
                    date_assigned = temp[3]
                    due_date = temp[4]
                    completion_check = temp[5].strip("\n")

                    task_string = f"\nTask:\t\t\t{task_title}\nAssigned to:\t\t{user_name}\nDate assigned:\t\t{date_assigned}\nDue date:\t\t{due_date}\nTask Complete:\t\t{completion_check}\nTask description:\n {description_task}"
                    print(task_string)
                    print("________________________________________________________________________________________________")

            tasks_file.close()

    elif menu == 's':
        pass
        users_counter = 0 
        task_counter = 0

        with open("tasks.txt","r") as tasks_file:
            for line in tasks_file:
                task_counter += 1
            tasks_file.close()

        with open("user.txt","r") as users_file:
            for line in users_file:
                users_counter +=1
        print("________________________________________________________________________________________________")        
        print(f"Number of Users:\t\t{users_counter}\nNumber of tasks:\t\t{task_counter}")
        print("________________________________________________________________________________________________\n")
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")