#=====importing libraries===========
from datetime import date
from datetime import datetime

#====== Defining Functions ===========

# Function to return the contents of user.txt as a dictionary
def update_user_dict() :
    user_file = open("user.txt", 'r+', encoding='utf-8')
    user_dict = {}
    for line in user_file:
        line_list = line.split(", ")
        user_dict[line_list[0].strip()] = line_list[1].strip()
    user_file.close()
    # returns username + password list from txt file into dictionary for use in program
    return user_dict

# Function to write text to file
def write_txt_file(file_name, text) :
    ''' This function will take file_name, text as arguments
        Open the file_name.txt ->  write the whole string to the file'''

    with open(file_name, 'w', encoding='utf-8') as write_file :
        write_file.write(text)


# Function to write changes to txt file after each Edit
def update_txt_file(file_name, old_text, new_text) :
    ''' This function will take file_name, old_text and new_text as arguments
        Open the file_name.txt -> read the whole file into string variable
         In the string variable find and replace the old_text with the new_text
         Then write the whole string back to the file'''

    with open(file_name, 'r+', encoding='utf-8') as read_file :
        whole_txt_file = read_file.read()

    whole_txt_file = whole_txt_file.replace(old_text , new_text)

    with open(file_name, 'w+', encoding='utf-8') as write_file :
        write_file.write(whole_txt_file)


# Function to register new username and password to user.txt and return updated username dictionary
def reg_user(user_dict, new_username) :
    while True:
        if (new_username in user_dict):
            print("This username already taken. Select register user again and choose a different username! ")
            break
        else:
            #    - When new username is avaiable, request input of a new password
            print(f"Username {new_username} is available. ")
            new_password = input("Enter password for new user : ")
            #    - Request re-enter password for confirmation and write to file if both are same
            confirm_password = input("Re-enter password to confirm : ")
            if (new_password == confirm_password):
                print("New passwords match!!")
                # Open txt file in append mode to add new username and password to file
                user_file = open("user.txt", 'a', encoding='utf-8')
                user_file.write("\n" + new_username + ", " + new_password)
                user_file.close()
                print(f"New User {new_username} registered successfully!!")
                user_dict = update_user_dict()
            else:
                print("Passwords do not match. Choose register option and try again! ")
            break
    return user_dict

# Function to add new task to tasks.txt
def add_task() :
    task_title = input("Enter the title of the task being assigned : ")
    task_descr = input("Enter a description about the task being assigned : ")
    assigned_date = date.today().strftime('%d %b %Y')
    print(f"Date of task assignment is : {assigned_date}")
    due_date = input("Enter due date of completion for the task being assigned (dd mmm yyyy): ")
    task_completed = "No"
    #  - Writing entered data on new task to tasks.txt file
    task_file = open("tasks.txt", 'a', encoding='utf-8')
    task_file.write("\n" + assigned_to + ", " + task_title + ", " + task_descr + ", " +
                    assigned_date + ", " + due_date + ", " + task_completed)
    task_file.close()
    

# Function to view all tasks in tasks.txt
def view_all() :
    task_file = open("tasks.txt", 'r+', encoding='utf-8')
    print("All task in the file are displayed below : ")
    count = 1
    for line in task_file:  # - Read a line from the file.
        task_list = line.split(", ")  # - Split that line where there is comma and space.
        # - assign the items in the list to variables as per content/ position in txt file line
        assigned_to = task_list[0].strip()
        task_title = task_list[1].strip()
        task_descr = task_list[2].strip()
        assigned_date = task_list[3].strip()
        due_date = task_list[4].strip()
        task_completed = task_list[5].strip()
        print(f"\nTask No.  {count}")
        count += 1
        # - Print details of each task in a proper format
        print(f"-------------------------------------------------\n"
              f"Task : \t\t\t\t {task_title} \n"
              f"Assigned to : \t\t {assigned_to}\n"
              f"Date assigned : \t {assigned_date}\n"
              f"Due date : \t\t\t {due_date}\n"
              f"Task Complete? \t\t {task_completed}\n"
              f"Task Description : \t {task_descr}\n"
              f"-------------------------------------------------")
    task_file.close()  # close the txt file after read operation is done

# Function to read tasks.txt file and display tasks alloted to a username and return list of Tasks for the username
# with task number inserted in the front of each task in user_tasks list
def update_user_task(username) :
    task_file = open("tasks.txt", 'r', encoding='utf-8')
    print(f"\nDisplaying tasks assigned to {username} : ")
    count = 1
    user_tasks = []
    for line in task_file:  # - Read a line from the file.
        task_list = line.split(", ")  # - Split that line where there is comma and space.
        # - assign the items in the list to variables as per content/ position in txt file line
        assigned_to = task_list[0].strip()
        task_title = task_list[1].strip()
        task_descr = task_list[2].strip()
        assigned_date = task_list[3].strip()
        due_date = task_list[4].strip()
        task_completed = task_list[5].strip()
        # - check if the username logged in is the same as given in this task, then print the task details
        if username == assigned_to:
            print(f"\nTask No.  {count}")
            task_list.insert(0, str(count))  # Add Task No in front to identify each task
            # Add all tasks assigned to this username in a list user_tasks
            user_tasks.append(", ".join(task_list))
            count += 1
            # - Print details of each task in a proper format
            print(f"-------------------------------------------------\n"
                  f"Task : \t\t\t\t {task_title} \n"
                  f"Assigned to : \t\t {assigned_to}\n"
                  f"Date assigned : \t {assigned_date}\n"
                  f"Due date : \t\t\t {due_date}\n"
                  f"Task Complete? \t\t {task_completed}\n"
                  f"Task Description : \t {task_descr}\n"
                  f"-------------------------------------------------")
    # If there are no tasks assigned to the username display message
    if count == 1:
        print("No tasks assigned to this user!!")
    task_file.close()  # close the txt file after read operation is done
    # At the end of reading the txt file, all tasks assigned to specific user are stored in user_tasks list with TaskNo
    return(user_tasks)


# Function to view Tasks assigned to a specific username
def view_mine(username) :
    # Call Function to read tasks.txt file, display the tasks and return list of Tasks for the username
    # The returned tasks_list will contain task number as displayed to user
    user_tasks_list = update_user_task(username)
    # Asking user to select if they want to edit any task or go back to main menu
    selected_task_number = int(0)
    while (selected_task_number != -1):
        selected_task_number = int(
            input("Enter Task No to select task for editing (Enter -1 to return to main menu): "))
        if selected_task_number == -1:
            break
        elif selected_task_number > (len(user_tasks_list) + 1) or selected_task_number < 1:
            print("Sorry!! you have not selected Task No for tasks as displayed above!!!")
        else:
            selected_task = user_tasks_list[selected_task_number - 1]
            selected_task_txt_file = selected_task[3:]  # original text related to task as in tasks.txt file ,
            # will use this to find and replace with new data to tasks.txt

            selected_task_split = selected_task.split(", ")     # Splitting the selected task into its parameters
            print(f"You have selected Task No. {selected_task_split[0]}  having title \"{selected_task_split[2]}\" "
                  f"and due date for completion is {selected_task_split[5]}")
            # Asking user to mark complete or Edit the task
            complete_or_edit = int(
                input("Input 1 to mark this Task as completed or Input 2 if you want to edit this Task : "))
            if complete_or_edit == 1:
                selected_task_split[6] = "Yes\n"  # Changing the parameter in the list of selected Task
                # merging the list without Task No as comma seperated to write back to txt file
                edited_task_txt_file = ", ".join(selected_task_split)[3:]
                # Writing to txt file using function
                update_txt_file("tasks.txt", selected_task_txt_file, edited_task_txt_file)
                print("The selected task has been marked as completed!")
                user_tasks_list = update_user_task(username)

            elif complete_or_edit == 2:
                # Task can be edited only if it is not marked completed already
                if selected_task_split[6] == "Yes\n":
                    print(f"Task is already marked completed! Cannot edit!!")
                else:
                    edit_task = int(input("Enter 1 to change the alloted user for this Task or \n"
                                          "Enter 2 to change the due date of completion for this Task : "))
                    if edit_task == 1:
                        new_user = input(f"This task is currently allotted to {selected_task_split[1]}.\n"
                                         f"Enter username to re-allot this task to : ")
                        # Checking if new_user is an existing user or not
                        user_dict = update_user_dict()
                        if new_user not in user_dict:
                            print("Username does not exist!!")
                        else:
                            selected_task_split[1] = new_user  # Changing the parameter in the list of selected Task
                            # merging the list without Task No as comma seperated to write back to txt file
                            edited_task_txt_file = ", ".join(selected_task_split)[3:]
                            # Writing to txt file using function
                            update_txt_file("tasks.txt", selected_task_txt_file, edited_task_txt_file)
                            print(f" Task no {selected_task_split[0]} re-allotted to {selected_task_split[1]}")
                            user_tasks_list = update_user_task(username)

                    elif edit_task == 2:
                        new_date = input(f"Current due date for completion of this task is {selected_task_split[5]}.\n"
                                         f"Enter new due date for completion (dd mmm yyyy) : ")
                        selected_task_split[5] = new_date  # Changing the parameter in the list of selected Task
                        # merging the list without Task No as comma seperated to write back to txt file
                        edited_task_txt_file = ", ".join(selected_task_split)[3:]
                        # Writing to txt file using function
                        update_txt_file("tasks.txt", selected_task_txt_file, edited_task_txt_file)
                        print(f" Task no {selected_task_split[0]} due date changed to {selected_task_split[5]}")
                        user_tasks_list = update_user_task(username)

                    else:
                        print("You have not made correct selection !!!")

            else:
                print("You have not made correct selection !!!")


# function task_overview() will also return a 2D list of all tasks and having different parameters of one task
# this 2D list will be used to generate the user_overview.txt file using the function user_overview()

def task_overview() :
    task_file = open("tasks.txt", 'r', encoding='utf-8')
    tasks_list = task_file.read().split("\n")       # this will have all parameters of one task as an item of the list
    task_file.close()
    total_number_tasks = len(tasks_list)  # length of this list is the number of tasks

    # split each item of the above list at ", " to get different parameters of one task into a 2D list
    tasks_list_details = []
    for i in range (0,len(tasks_list)):
        tasks_list_details.append(tasks_list[i].split(", "))

    completed_task = int(0)
    pending_task = int(0)
    overdue_task = int(0)

    for i in range(0,len(tasks_list_details)) :
        if tasks_list_details[i][5] == "Yes" :
            completed_task =+ 1
        if tasks_list_details[i][5] == "No" :
            pending_task += 1
        due_date = datetime.strptime(tasks_list_details[i][4] , "%d %b %Y")
        date_today = datetime.now()
        if due_date < date_today and tasks_list_details[i][5] == "No":
            overdue_task += 1
    percent_incomplete = pending_task / total_number_tasks * 100
    percent_overdue = overdue_task / total_number_tasks * 100

    output_str = f'''    The total number of tasks that have been generated and tracked : {total_number_tasks}\n
    The total number of completed tasks : {completed_task}\n
    The total number of uncompleted tasks : {pending_task}\n
    The total number of tasks that haven’t been completed and that are overdue : {overdue_task}\n
    The percentage of total tasks that are incomplete : {percent_incomplete}\n
    The percentage of total tasks that are overdue : {percent_overdue}'''

    write_txt_file("task_overview.txt" , output_str )

    return(tasks_list_details)


def user_overview(tasks_list_details) :
    user_dict = update_user_dict()  # function that returns username and password as a dictionary
    total_users = len(user_dict)       #length of the dictionary will be total number of users
    total_tasks = len(tasks_list_details)
    user_task_summary = []
    for username in user_dict :
        user_task_summary.append([username, 0, 0, 0, 0, 0, 0, 0, 0])

    for i in range(0, len(user_dict)) :
        for j in range(0, len(tasks_list_details)) :
            if user_task_summary[i][0] == tasks_list_details[j][0] :
                user_task_summary[i][1] += 1        # increase task assigned to user count
                if tasks_list_details[j][5] == "Yes":
                    user_task_summary[i][2] += 1        # increase task completed by user count
                if tasks_list_details[j][5] == "No":
                    user_task_summary[i][3] += 1        # increase task pending for user count
                    due_date = datetime.strptime(tasks_list_details[j][4], "%d %b %Y")
                    date_today = datetime.now()
                    if due_date < date_today:
                        user_task_summary[i][4] += 1    # increase task overdue for user count
        user_task_summary[i][5] = user_task_summary[i][1] / total_tasks * 100    # % task to user
        if user_task_summary[i][1] != 0 :
            user_task_summary[i][6] = user_task_summary[i][2] / user_task_summary[i][1] *100   # %task completed by user
            user_task_summary[i][7] = user_task_summary[i][3] / user_task_summary[i][1] *100   # %task pending for user
            user_task_summary[i][8] = user_task_summary[i][4] / user_task_summary[i][1] *100   # %task overdue for user

    output_str = f"{'Username' : ^12}{'Tasks' : ^13}{'Completed' : ^12}{'Pending' : ^12}{'Overdue' : ^12}" \
                 f"{'%Assignment' : ^13}{'%Completion' : ^13}{'%Pending' : ^12}{'%Overdue' : ^12}"

    for i in range(0, len(user_task_summary)):
        temp_str = "  "
        for j in range(0, 9):
            temp_str += f"{str(user_task_summary[i][j]) : ^12}"
        output_str += '\n' + '-' * 115 + '\n' + temp_str

    write_txt_file("user_overview.txt", output_str)



#==========Login Section=========
#    Read usernames and password from the user.txt file and stores them in a dictionary
user_dict = update_user_dict()

#    only when login_success indicates True after validation of username and password, program will move to menu
login_success = False

#    login_counter terminates program if incorrect login attempt is made 3 times
login_counter = 0

#    - Using a while loop to validate username and password.
while (login_success == False):
    login_counter += 1
    username = input("Enter Username : ")
    if(username not in user_dict) :
        print("User does not exist!! Please try again!! (Username is case sensitive)")
    elif(username in user_dict) :
        password = input("Enter Password : ")
        if(password != user_dict[username]):
            print("Password Incorrect!! Please try again!! (Password is case sensitive)")
        elif(password == user_dict[username]):
            login_success = True
            print(f"Welcome {username}")
            break

    if(login_counter >= 3):
        print("\nYou have made too many incorrect login attempts!!!! \nProgram will now terminate!!!")
        exit()


#====Menu Section====
# - Code to display the options available to user and input response
menu = "x"
if(login_success == True) :
    while(menu != "e") :
        if username == "admin" :
            menu = input('''\nSelect one of the following Options below:
            r - Registering a user (admin User Only)
            a - Adding a task
            va - View all tasks
            vm - View my task
            gr - Generate Reports (admin User Only)
            ds - Display Statistics (admin user Only)
            e - Exit
            : ''').lower()

        if username != "admin" :
            menu = input('''\nSelect one of the following Options below:
            a - Adding a task
            va - View all tasks
            vm - View my task
            e - Exit
            : ''').lower()

        if menu == 'r':
            #   This block is to Register a new user to the user.txt file
            if username == "admin" :
                # Only If admin is currently logged in, request input of a new username
                new_username = input("Enter username for new user : ")
                # Call function to register new username and return updated username password dictionary
                user_dict = reg_user(user_dict, new_username)

            else :
                print("This option is only available to admin user!!")

        elif menu == 'a':
            #  This block is to allow a user to add a new task to task.txt file
            print("To add a new task to the File please enter the following details about the task: ")
            assigned_to = input("Enter username of the person this task is assigned to : ")
            #  - Checking for existing username
            if assigned_to not in user_dict :
                print("Username does not exist !! \n You will now be redirected to Menu. "
                      "Please select Adding a task option to try with valid username!")
            else :
                add_task()
                print("Task added successfully!")

        elif menu == 'va':
            # Call function to read the task from tasks.txt file and print to console in proper format
            view_all()

        elif menu == 'vm':
            # Call function to read the task from tasks.txt file and
            # display only those tasks which are assigned to the user who is logged in
            view_mine(username)

        elif menu == 'gr' :
            tasks_list_details = task_overview()
            user_overview(tasks_list_details)
            print("Reports have been generated.")

        elif menu == 'ds' :
            tasks_list_details = task_overview()
            user_overview(tasks_list_details)

            print("\n-------------------------TASK OVERVIEW REPORT-------------------------------\n")
            with open("task_overview.txt", 'r', encoding="utf-8") as read_file:
                print(read_file.read())

            print("\n\n-------------------------USER OVERVIEW REPORT-------------------------------\n")
            with open("user_overview.txt", 'r', encoding="utf-8") as read_file:
                print(read_file.read())

        elif menu == 'e' :
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
            
            