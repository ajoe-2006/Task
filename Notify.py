#Modules
import customtkinter
from customtkinter import *
import mysql.connector as mysql

# Connect to MySQL database
db = mysql.connect(
    host="localhost",
    user="root",
    password="admin",
    database="task_management"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create the tasks table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        Id INT AUTO_INCREMENT PRIMARY KEY,
        Name varchar(50) not null, 
        Title VARCHAR(40) not null,
        Description TEXT,
        Due_Date DATE not null,
        Status VARCHAR(20) DEFAULT 'Not Started'
    )
""")

# Function to add a new task
def add_task(name,title,description,due_date):
    cursor.execute("""
        INSERT INTO tasks (name, title, description, due_date)
        VALUES (%s, %s, %s, %s)
    """, (name, title, description, due_date))
    db.commit()

# Function to see the list of id and its name
def see_id():
    cursor.execute("select id,name from tasks")
    task1 = cursor.fetchall()
    for see in task1:
        print(f"ID: {see[0]} , Name:{see[1]}")

# Function to view all tasks
def view_tasks(task_id):
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Name: {task[1]}, Title: {task[2]}, Description: {task[3]}, Due Date: {task[4]}, Status: {task[5]}")

# Function to update task status
def update_status(task_id,status):
    cursor.execute("""
        UPDATE tasks
        SET status = %s
        WHERE id = %s
    """, (status, task_id))
    db.commit()

# Function to delete a task
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    db.commit()

#Functions used for buttons
def button_click_Add_Task():
    dialog = CTkInputDialog(text="Enter Your Name", title="User_Name")
    A1= dialog.get_input()
    A2=str(A1)

    dialog = CTkInputDialog(text="Task Title", title="Add_Task")
    a= dialog.get_input()
    a1=str(a)

    dialog1= CTkInputDialog(text="Task Description", title="Add_Task")
    b=dialog1.get_input()
    b1=str(b)

    dialog2 = CTkInputDialog(text="Task Due_Date ", title="Add_Task")
    c=dialog2.get_input()
    c1=str(c)

    add_task(A1,a1,b1,c1)

def button_click_View_Task():
    dialog3 = CTkInputDialog(text="Enter Your ID No.", title="View_Task")
    a2= dialog3.get_input()
    a3=str(a2)
    view_tasks(a3)

def button_click_update_Task():
    dialog4 = CTkInputDialog(text="Enter Your ID No.", title="Update_Task")
    a4= dialog4.get_input()
    a5=str(a4)

    dialog5 = CTkInputDialog(text="Enter New Status", title="Update_Task")
    a6= dialog5.get_input()
    a7=str(a6)
    update_status(a5,a7)

def button_click_see_Task():
    see_id()

def button_click_delete_Task():
    dialog6 = CTkInputDialog(text="Enter Task ID to Delete", title="Delete_Task")
    a8= dialog6.get_input()
    a9=str(a8)

    delete_task(a9)

def button_click_Exit_Task():
    app1.destroy()

#To view in tab mode
class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Notify")
        self.add("Info")

        #To create Buttons on the "Notify's" homepage

        self.button = customtkinter.CTkButton(master=self.tab("Notify"), text="Add Task", command=button_click_Add_Task)
        self.button.grid(padx=20, pady=10)

        self.button = customtkinter.CTkButton(master=self.tab("Notify"), text="View Task", command=button_click_View_Task)
        self.button.grid(padx=20, pady=20)

        self.button = customtkinter.CTkButton(master=self.tab("Notify"), text="Update Task", command=button_click_update_Task)
        self.button.grid(padx=20, pady=20)

        self.button = customtkinter.CTkButton(master=self.tab("Notify"), text="Delete Task", command=button_click_delete_Task)
        self.button.grid(padx=20, pady=20)

        self.button = customtkinter.CTkButton(master=self.tab("Notify"), text="View User_Id", command=button_click_see_Task)
        self.button.grid(padx=20, pady=20)

        self.button = customtkinter.CTkButton(master=self.tab("Notify"), text="Exit", command=button_click_Exit_Task)
        self.button.grid(padx=20, pady=20)

        #To create a Label for the Info Page
        
        self.label = customtkinter.CTkLabel(master=self.tab("Info") , text=""""Notify" is an innovative and feature-rich notes application meticulously designed to enhance 
                    the note-taking experience for users across various walks of life.

                                In an increasingly digital and fast-paced world, capturing, organizing, and 
                    accessing your thoughts, ideas, and important information efficiently is more crucial than ever.

                                "Notify" was born out of the desire to provide users with a streamlined and user-friendly platform
                    that goes beyond traditional note-taking.

                                It empowers individuals, whether they are students, professionals, creatives, or anyone in need of a 
                    reliable digital companion for their notes""")
        self.label.grid(padx=20, pady=20)

#Tabs are stored under this App() class function
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        
#To execute the Class and run the program       
app1=App()
app1.mainloop()

# Close the database connection when done
db.close()
