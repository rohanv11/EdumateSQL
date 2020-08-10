# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:06:48 2019

@author: mac
"""

from tkinter import *
from tkinter import messagebox
import re, pymysql
from PIL import ImageTk, Image

def adjustWindow(window):
    w= 600 
    h= 600
    ws= screen.winfo_screenwidth() #width of the screen
    hs= screen.winfo_screenheight() #height of the screen
    x= (ws/2) - (w/2)
    y= (hs/2) - (h/2)
    window.geometry("%dx%d+%d+%d" %(w, h, x, y)) #set the dimensions of the screen and where it is placed
    window.configure(background= "white") #making the background of the window white
    
#validating the values and inserting new record in database for signup
def register_user():
    #checking for all empty values in entry field
    if fullname.get() and email.get() and password.get() and repassword.get() and gender.get():
        if university.get()== " --select your university--": #checking for selection of uni
            Label(screen1, text= "Please select your university", fg= "red", font= ("Calibri", 11), width= "30", anchor= W, bg= "white").place(x=0, y= 570)
            return
        else:
            if tnc.get(): #checking for acceptance of agreement
                if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email.get()): #validating the email
                    if password.get()== repassword.get():
                        gender_value= "male"
                        if gender.get()==2:
                            gender_value= "female"
                        connection= pymysql.connect(host= "localhost", user= "root", passwd= "", database= "Edumate") #database connection
                        cursor= connection.cursor()
                        insert_query= "INSERT INTO student_details (fullname, email, password, gender, university) VALUES (' "+ fullname.get() + " ', ' "+ email.get()+ " ' , ' "+password.get()+ " ', ' "+ gender_value + " ', ' "+ university.get() + " ');" #queries for inserting values
                        cursor.execute(insert_query) #executing the queries
                        connection.commit() #commiting the connection then closing it
                        connection.close() #closing the connection of the database
                        Label(screen1, text= "Registration Success", fg= "green", font=("Calibri", 11), width= "30", anchor= W, bg= "white").place(x= 0, y= 570) #printing successful registration message
                        Button(screen1, text= "Proceed to Login ->", width= 20, font=("Open Sans", 9, "bold"), bg= "brown", fg= "white", command= screen1.destroy).place(x=170, y= 565) #button to navigate back to login page
                    else:
                        Label(screen1, text= "Password does not match", fg= "red", font=("Calibri", 11), width= "30", anchor= W, bg= "white").place(x= 0, y= 570)
                        return
                else:
                    Label(screen1, text= "Please enter valid email id", fg= "red", font= ("Calibri", 11), width= "30", anchor= W, bg= "white").place(x= 0, y= 570)
                    return
            else:
                Label(screen1, text= "Please accept the agreement", fg= "red", font= ("Calibri", 11), width= "30", anchor= W, bg= "white").place(x= 0, y= 570)
                return
    else:
        Label(screen1, text= "Please fill all the details", fg= "red", font= ("Calibri", 11), width= "30", anchor= W, bg= "white").place(x= 0, y= 570)
        pack()
        return
        
        
#registration window
def register():
    global screen1, fullname, email, password, repassword, university, gender, tnc
    fullname= StringVar()
    email= StringVar()
    password= StringVar()
    repassword= StringVar()
    university= StringVar()
    gender= StringVar()
    tnc= StringVar()
    screen1= Toplevel(screen)
    screen1.title("Registration")
    adjustWindow(screen1)
    Label(screen1, text= "Registration Form", width= "40", height= "2", font= ("Calibri", 22, "bold"), fg= "white", bg= "#d9660a").place(x=0, y=0)
    Label(screen1, text= "", bg= "#174873", width= "70", height= "28").place(x= 45, y= 120)
    Label(screen1, text= "Full Name:", font= ("Open Sans", 11, "bold"), fg= "white", bg= "#174873", anchor= W).place(x= 150, y= 160)
    Entry(screen1, textvar= fullname).place(x= 300, y= 160)
    Label(screen1, text= "Email ID:", font= ("Open Sans", 11, "bold"), fg= "white", bg= "#174873", anchor= W).place(x= 150, y= 210)
    Entry(screen1, textvar= email).place(x= 300, y= 210)
    Label(screen1, text= "Gender:", font=("Open Sans", 11, "bold"), fg= "white", bg= "#174873", anchor= W).place(x= 150, y= 260)
    Radiobutton(screen1, text= "Male", variable= gender, value= 1, bg= "#174873").place(x= 300, y= 260)
    Radiobutton(screen1, text= "Female", variable= gender, value= 2, bg= "#174873").place(x= 370, y= 260)
    Label(screen1, text= "University", font= ("Open Sans", 11, "bold"), fg= "white", bg= "#174873", anchor= W).place(x= 150, y= 310)
    list1= ["Mumbai University", "Savitribai Phule Pune University", "Gujarat Technological University", "JNTU Kakinada", "University of Delhi", "Anna University"]
    droplist= OptionMenu(screen1, university, *list1)
    droplist.config(width= 17)
    university.set("--select your university--")
    droplist.place(x= 300, y= 305)
    Label(screen1, text= "Password:", font= ("Open Sans", 11, "bold"), fg= "white", bg= "#174873", anchor= W).place(x= 150, y= 360)
    Entry(screen1, textvar= password, show= "*").place(x= 300, y= 360)
    Label(screen1, text= "Re-Password:", font= ("Open Sans", 11, "bold"), fg= "white", bg= "#174873", anchor= W).place(x= 150, y= 410)
    entry_4= Entry(screen1, textvar= repassword, show= "*")
    entry_4.place(x= 300, y= 410)
    Checkbutton(screen1, text= "I accept all terms and conditions", variable= tnc, bg= "#174873", font= ("Open Sans", 9, "bold"), fg= "brown").place(x= 175, y= 450)
    Button(screen1, text= "Submit", width= 20, font= ("Open Sans", 13, "bold"), bg= "brown", fg= "white", command= register_user).place(x= 170, y= 490)

#login credentials verification
def login_verify():
    global studentID
    connection= pymysql.connect(host= "localhost", user= "root", passwd= "", database= "Edumate")
    cursor= connection.cursor()
    select_query= "SELECT * FROM student_details where email= ' " + username_verify.get() + " ' AND password = ' " + password_verify.get() + " ';"
    cursor.execute(select_query)
    student_info= cursor.fetchall()
    connection.commit() #commiting the connection then closing it
    connection.close() #closing the connection of the database
    if student_info:
        messagebox.showinfo("Congratulations", "Login Successfull")
        studentID= student_info[0][0]
        welcome_page(student_info) #opening welcome window
    else:
        messagebox.showerror("Error", "Invalid Username or Password")
global screen
#login window
def main_screen():
    global screen, username_verify, password_verify
    screen= Tk()
    username_verify= StringVar()
    password_verify= StringVar()
    screen.title("EDUMATE")
    adjustWindow(screen)
    Label(screen, text= "EDUMATE - Student Manager", width= "500", height= "2", font=("Calibri", 22, "bold"), fg= "white", bg= "#d9660a").pack()
    Label(text= "", bg= "white").pack() #for leaving a space in between
    Label(screen, text= "", bg= "#174873", width= "65", height= "19").place(x= 60, y= 95) #blue background in the middle of the window
    Label(screen, text= "Please enter details below to login", bg= "#174873", fg= "white").pack()
    Label(screen, text= "", bg= "#174873").pack() #for leaving a space in between
    Label(screen, text= "Username *", font=("Open Sans", 10, "bold"), bg= "#174873", fg= "white").pack()
    Entry(screen, textvar= username_verify).pack()
    Label(screen, text= "", bg= "#174873").pack()
    Label(screen, text= "Password *", font= ("Open Sans", 10, "bold"), bg= "#174873", fg= "white").pack()
    Entry(screen, textvar= password_verify, show= "*").pack()
    Label(screen, text= "", bg= "#174873").pack()
    Button(screen, text= "LOGIN", bg= "#e79700", width= 15, height= 1, font= ("Open Sans", 13, "bold"), fg= "white" , command= login_verify).pack()
    Label(screen, text= "", bg= "#174873").pack()
    Button(screen, text= "New User? Register Here", height= "2", width= "30", bg= "#e79700", font=("Open Sans", 10, "bold"), fg= "white" , command= register).pack()
    screen.mainloop()


global screen2
def welcome_page(student_info):
    screen2 = Toplevel(screen)
    screen2.title("Student Page")
    adjustWindow(screen2) #configure the window
    Label(screen2, text="Welcome" ,width='32',height='2').pack()
    Label(screen2,text="HI, "+student_info[0][1],bg='#174873',).pack()
    Button(screen2, text="Enter your grades : ",width=20, font=("Open Sans",13,'bold'),bg="brown",fg="white",command=Student_new_record).place(x=200,y=200)
    Button(screen2, text="Check Result!",width=20, font=("Open Sans",13,'bold'),bg="brown",fg="white").place(x=200,y=400)

def Student_new_record():   
    semester = StringVar() 
    entryField = list() 
    screen4 = Toplevel(screen) 
    screen4.title("New Record") 
    adjustWindow(screen4) # configuring t the window
    Label(screen4, text="Enter New Record", width='31', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#d9660a').grid(row=0, sticky=W, columnspan=4) 
    Label(screen4, text="", bg='#174873', width='60', height='18').place(x=0, y=127) 
    Label(screen4, text="", bg='white').grid(row=1,column=0) 
    Label(screen4, text="Subject Name", font=("Open Sans", 12, 'bold'), fg='white', bg='#174873').grid(row=2,column=0, pady=(5,10)) 
    Label(screen4, text="Your Marks", font=("Open Sans", 12, 'bold'), fg='white', bg='#174873').grid(row=2,column=1, pady=(5,10)) 
    Label(screen4, text="Out of", font=("Open Sans", 12, 'bold'), fg='white', bg='#174873').grid(row=2,column=2, pady=(5,10)) 
    Label(screen4, text="Credits Points", font=("Open Sans", 12, 'bold'), fg='white', bg='#174873').grid(row=2,column=3, pady=(5,10)) 
  
    rowNo = 3 
    for i in range(6): # this loop will generate all input field for taking input from the user 
        temp = list() 
        for j in range(4): 
            e = Entry(screen4, width=14) 
            e.grid(row=rowNo,column=j, padx=(3,0), pady=(0,25)) 
            temp.append(e) 
        entryField.append(temp) 
        rowNo += 2
    Label(screen4, text="Select Sem:", font=("Open Sans", 12, 'bold'), fg='white', bg='#174873').grid(row=rowNo,column=0, pady=(15,0)) 
    list1 = ['1','2','3','4','5','6','7','8'] 
    droplist = OptionMenu(screen4, semester, *list1) 
    semester.set('--0--') 
    droplist.config(width=5) 
    droplist.grid(row=rowNo, column=1, pady=(15,0)) 
    Button(screen4, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=lambda: enter_new_record(entryField, semester)).grid(row=rowNo,columnspan=2,column=2, pady=(15,0))
    


main_screen()
