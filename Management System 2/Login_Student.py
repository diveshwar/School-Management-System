from tkinter import *
from tkinter import messagebox

import mysql.connector

import Menu_Student

class Student_Show:
    def __init__(self,root,ls,frame_old):
        self.frame_old = frame_old
        self.root = root
        self.ls = ls

        # Creating the variable.
        self.Roll_No_var = StringVar()
        self.password_var = StringVar()

        # Creating the first frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating the first frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0] // 7 * 2, y=ls[1] // 4, width=ls[0] // 7 * 3, height=ls[1] // 4 * 2)

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the page.
        self.title = Label(self.frame, text='TVD UNIVERSITY', font=('Algerian', 25, 'bold'), bg='LightGreen').pack(
            side=TOP)

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='STUDENT PORTAL', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(
            side=TOP)

        # Label Login
        lbl_id = Label(self.frame1, text="Roll No:", bg="white", fg="blue", font=("times new roman",15))
        lbl_id.place(x=ls[0]*130//1336, y=ls[1]*127//714)

        txt_id = Entry(self.frame1, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_id.place(x=ls[0]*230//1336, y=ls[1]*130//714)

        # Label Login
        lbl_id = Label(self.frame1, text="Password: ", bg="white", fg="blue", font=("times new roman", 15))
        lbl_id.place(x=ls[0]*130//1336, y=ls[1]*197//714)

        txt_id = Entry(self.frame1, textvariable=self.password_var,show="*", font=("times new roman", 12), bd=2,
                       relief=GROOVE)
        txt_id.place(x=ls[0]*230//1336, y=ls[1]*200//714)

        # Submit Button
        self.fees_btn = Button(self.frame1, text='LOGIN', bd=0, bg='black',fg='white',font=("times new roman", 15),
                               compound=TOP, command=self.new_page)
        self.fees_btn.place(x=ls[0]*250//1336, y=ls[1]*300//714)

    def new_page(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",passwd='79sumathi',database="employee")
            cur = conn.cursor()

            cur.execute("SELECT * FROM student_data where Roll_No=" + str(self.Roll_No_var.get()))

            rows = cur.fetchall()
            if len(rows) != 0:
                if str(self.password_var.get()) == str(rows[0][4]):
                    self.roll = str(rows[0][0])
                    firster = Menu_Student.Student_Menu(self.root, self.ls, self.frame_old, self.frame, self.roll)
                else:
                    messagebox.showerror("Error", "Wrong Password, Please Input The Correct Password.")
            else:
                messagebox.showerror("Error", "No Student Found!! Contact School Admin.")
        except:
            messagebox.showerror("Error","Your Profile Does not Exists in our Student Database")
            
    


    def exiting(self):
        self.frame.place_forget()
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass
